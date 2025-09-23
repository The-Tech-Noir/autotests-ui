import pytest


SYSTEM_VERSION = "Windows" # Для примера укажем версию тестируемой OS

@pytest.mark.skipif(
    SYSTEM_VERSION == "Linux",     # Пропустим автотест, если версия системы Linux(дало нам False => PASSED)
    reason="Тест не может быть запущен на Linux"
)
def test_system_version_valid():
    ...

@pytest.mark.skipif(
    SYSTEM_VERSION == "Windows",    # Пропустим автотест, если версия системы Windows(дало нам True => SKIPPED)
    reason="Тест не может быть запущен на Windows"
)
def test_system_version_invalid():
    ...