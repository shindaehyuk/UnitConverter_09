import json

import pytest

from unit_converter.converter import UnitConverter
from unit_converter.formatter import OutputFormatter
from unit_converter.registry import UnitRegistry


@pytest.fixture
def formatter() -> OutputFormatter:
    return OutputFormatter()


@pytest.fixture
def sample_results() -> dict[str, float]:
    return {"feet": 8.2, "yard": 2.7}


def test_tc01_table_output_format(
    formatter: OutputFormatter,
    default_registry: UnitRegistry,
) -> None:
    converter = UnitConverter(default_registry)
    results = converter.convert("meter", 2.5)
    output = formatter.format("meter", 2.5, results, fmt="table")
    assert "2.5 meter = 8.2 feet" in output
    assert "2.5 meter = 2.7 yard" in output


def test_tc08_table_output_excludes_source_unit(
    formatter: OutputFormatter,
    default_registry: UnitRegistry,
) -> None:
    converter = UnitConverter(default_registry)
    results = converter.convert("meter", 2.5)
    output = formatter.format("meter", 2.5, results, fmt="table")
    assert "= 2.5 meter" not in output


def test_tc13_json_output_format(
    formatter: OutputFormatter,
    sample_results: dict[str, float],
) -> None:
    output = formatter.format("meter", 2.5, sample_results, fmt="json")
    data = json.loads(output)
    assert data["source_unit"] == "meter"
    assert data["source_value"] == 2.5
    assert data["conversions"]["feet"] == pytest.approx(8.2, abs=0.05)
    assert data["conversions"]["yard"] == pytest.approx(2.7, abs=0.05)


def test_tc14_csv_output_format(
    formatter: OutputFormatter,
    sample_results: dict[str, float],
) -> None:
    output = formatter.format("meter", 2.5, sample_results, fmt="csv")
    lines = output.strip().splitlines()
    assert lines[0] == "source_unit,source_value,target_unit,target_value"
    assert "meter,2.5,feet,8.2" in lines
    assert "meter,2.5,yard,2.7" in lines
