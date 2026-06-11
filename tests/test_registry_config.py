import pytest

from unit_converter.converter import UnitConverter
from unit_converter.registry import UnitRegistry

CONFIG_PATH = "config/units.json"


def test_tc11_load_units_from_json() -> None:
    registry = UnitRegistry.from_config(CONFIG_PATH)
    converter = UnitConverter(registry)
    result = converter.convert("meter", 2.5)
    assert result["feet"] == pytest.approx(8.2, abs=0.05)
    assert result["yard"] == pytest.approx(2.7, abs=0.05)
