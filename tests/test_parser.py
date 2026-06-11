import pytest

from unit_converter.parser import InputParser, ValidationError


@pytest.fixture
def parser() -> InputParser:
    return InputParser()


def test_tc04_negative_value_rejected(parser: InputParser) -> None:
    with pytest.raises(ValidationError) as exc_info:
        parser.parse("meter:-1")
    assert str(exc_info.value) == "Negative value not allowed: -1.0"


def test_tc05_missing_colon_format_error(parser: InputParser) -> None:
    with pytest.raises(ValidationError) as exc_info:
        parser.parse("meter")
    assert str(exc_info.value) == "Invalid format. Use unit:value (ex: meter:2.5)"


def test_tc06_invalid_number_error(parser: InputParser) -> None:
    with pytest.raises(ValidationError) as exc_info:
        parser.parse("meter:abc")
    assert str(exc_info.value) == "Invalid number: abc"


def test_tc01_parse_meter_input(parser: InputParser) -> None:
    unit, value = parser.parse("meter:2.5")
    assert unit == "meter"
    assert value == pytest.approx(2.5)
