import json


class UnitRegistry:
    DEFAULT_UNITS = {
        "meter": 1.0,
        "feet": 3.28084,
        "yard": 1.09361,
    }
    BASE_UNIT = "meter"

    def __init__(self, units: dict[str, float] | None = None) -> None:
        self._units = dict(units or self.DEFAULT_UNITS)

    @classmethod
    def from_config(cls, config_path: str) -> "UnitRegistry":
        with open(config_path, encoding="utf-8") as config_file:
            data = json.load(config_file)
        return cls(data["units"])

    def register(self, name: str, meter_ratio: float) -> None:
        self._units[name] = meter_ratio

    def register_from_expression(self, expression: str) -> None:
        left_part, right_part = (part.strip() for part in expression.split("=", 1))
        left_qty_str, left_unit = left_part.split(maxsplit=1)
        right_qty_str, right_unit = right_part.split(maxsplit=1)
        left_qty = float(left_qty_str)
        right_qty = float(right_qty_str)

        if left_unit == self.BASE_UNIT:
            self.register(right_unit, right_qty / left_qty)
        elif right_unit == self.BASE_UNIT:
            self.register(left_unit, left_qty / right_qty)
        else:
            raise ValueError(
                f"Expression must reference base unit '{self.BASE_UNIT}': {expression}"
            )

    def get_ratio(self, name: str) -> float:
        return self._units[name]

    def list_units(self) -> list[str]:
        return list(self._units.keys())

    def has_unit(self, name: str) -> bool:
        return name in self._units
