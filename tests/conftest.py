import pytest

from unit_converter.registry import UnitRegistry


@pytest.fixture
def default_registry() -> UnitRegistry:
    return UnitRegistry()
