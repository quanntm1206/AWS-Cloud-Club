from scripts.validate_sources import validate_sources


def test_source_registry_is_valid() -> None:
    assert validate_sources() == []

