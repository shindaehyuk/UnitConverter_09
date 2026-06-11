from unit_converter.parser import ValidationError
from unit_converter.registry import UnitRegistry


class UnitConverter:
    def __init__(self, registry: UnitRegistry) -> None:
        self._registry = registry

    def convert(self, unit: str, value: float) -> dict[str, float]:
        if not self._registry.has_unit(unit):
            raise ValidationError(f"Unknown unit: {unit}")

        meter_value = value / self._registry.get_ratio(unit)
        results: dict[str, float] = {}

        for target_unit in self._registry.list_units():
            if target_unit == unit:
                continue
            results[target_unit] = meter_value * self._registry.get_ratio(target_unit)

        return results
