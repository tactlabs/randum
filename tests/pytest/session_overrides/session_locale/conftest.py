import pytest

from tests.pytest.session_overrides.session_locale import _MODULE_LOCALES


@pytest.fixture(scope='session', autouse=True)
def randum_session_locale():
    return _MODULE_LOCALES
