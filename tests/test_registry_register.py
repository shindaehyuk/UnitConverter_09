import pytest

from unit_converter.converter import UnitConverter
from unit_converter.registry import UnitRegistry


def test_tc12_register_cubit_from_expression(default_registry: UnitRegistry) -> None:
    default_registry.register_from_expression("1 cubit = 0.4572 meter")
    converter = UnitConverter(default_registry)
    result = converter.convert("cubit", 2.0)
    assert result["meter"] == pytest.approx(0.9, abs=0.05)
