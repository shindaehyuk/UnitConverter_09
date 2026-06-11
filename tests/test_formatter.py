import pytest

from unit_converter.converter import UnitConverter
from unit_converter.formatter import OutputFormatter
from unit_converter.registry import UnitRegistry


@pytest.fixture
def formatter() -> OutputFormatter:
    return OutputFormatter()


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
