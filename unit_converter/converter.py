from unit_converter.registry import UnitRegistry


class UnitConverter:
    def __init__(self, registry: UnitRegistry) -> None:
        self._registry = registry

    def convert(self, unit: str, value: float) -> dict[str, float]:
        """입력 단위를 제외한 모든 단위로 변환한 결과를 반환한다."""
        raise NotImplementedError
