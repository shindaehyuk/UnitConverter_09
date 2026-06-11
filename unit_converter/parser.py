class ValidationError(Exception):
    """입력 검증 실패."""


class InputParser:
    def parse(self, input_str: str) -> tuple[str, float]:
        if ":" not in input_str:
            raise ValidationError("Invalid format. Use unit:value (ex: meter:2.5)")

        unit, value_str = input_str.split(":", 1)

        try:
            value = float(value_str)
        except ValueError:
            raise ValidationError(f"Invalid number: {value_str}")

        if value < 0:
            raise ValidationError(f"Negative value not allowed: {value}")

        return unit, value
