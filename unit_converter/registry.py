class UnitRegistry:
    DEFAULT_UNITS = {
        "meter": 1.0,
        "feet": 3.28084,
        "yard": 1.09361,
    }

    def __init__(self, units: dict[str, float] | None = None) -> None:
        self._units = dict(units or self.DEFAULT_UNITS)

    def register(self, name: str, meter_ratio: float) -> None:
        raise NotImplementedError

    def get_ratio(self, name: str) -> float:
        raise NotImplementedError

    def list_units(self) -> list[str]:
        return list(self._units.keys())

    def has_unit(self, name: str) -> bool:
        return name in self._units
