class ValidationError(Exception):
    """입력 검증 실패."""


class InputParser:
    def parse(self, input_str: str) -> tuple[str, float]:
        raise NotImplementedError
