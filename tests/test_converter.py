import pytest

from unit_converter.converter import UnitConverter
from unit_converter.parser import ValidationError
from unit_converter.registry import UnitRegistry


@pytest.fixture
def converter(default_registry: UnitRegistry) -> UnitConverter:
    return UnitConverter(default_registry)


def test_tc01_meter_to_feet_and_yard(converter: UnitConverter) -> None:
    result = converter.convert("meter", 2.5)
    assert result["feet"] == pytest.approx(8.2, abs=0.05)
    assert result["yard"] == pytest.approx(2.7, abs=0.05)


def test_tc02_feet_to_meter(converter: UnitConverter) -> None:
    result = converter.convert("feet", 3.28084)
    assert result["meter"] == pytest.approx(1.0, abs=0.05)


def test_tc03_yard_to_meter(converter: UnitConverter) -> None:
    result = converter.convert("yard", 1.09361)
    assert result["meter"] == pytest.approx(1.0, abs=0.05)


def test_tc07_unknown_unit_error(converter: UnitConverter) -> None:
    with pytest.raises(ValidationError) as exc_info:
        converter.convert("inch", 1.0)
    assert str(exc_info.value) == "Unknown unit: inch"


def test_tc08_excludes_source_unit_from_result(converter: UnitConverter) -> None:
    result = converter.convert("meter", 2.5)
    assert "meter" not in result


def test_tc09_conversion_goes_through_meter(converter: UnitConverter) -> None:
    result = converter.convert("feet", 3.28084)
    meter_value = 3.28084 / 3.28084
    expected_yard = meter_value * 1.09361
    assert result["yard"] == pytest.approx(expected_yard, abs=0.001)


def test_tc10_registry_extension_without_converter_change(
    default_registry: UnitRegistry,
) -> None:
    default_registry.register("inch", 39.3701)
    converter = UnitConverter(default_registry)
    result = converter.convert("inch", 39.3701)
    assert result["meter"] == pytest.approx(1.0, abs=0.05)
