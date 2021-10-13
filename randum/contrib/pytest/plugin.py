import pytest

from randum import Randum
from randum.config import DEFAULT_LOCALE

DEFAULT_SEED = 0


@pytest.fixture(scope='session', autouse=True)
def _session_randum(request):
    """Fixture that stores the session level ``Randum`` instance.

    This fixture is internal and is only meant for use within the project.
    Third parties should instead use the ``randum`` fixture for their tests.
    """
    if 'randum_session_locale' in request.fixturenames:
        locale = request.getfixturevalue('randum_session_locale')
    else:
        locale = [DEFAULT_LOCALE]
    return Randum(locale=locale)


@pytest.fixture()
def randum(request):
    """Fixture that returns a seeded and suitable ``Randum`` instance."""
    if 'randum_locale' in request.fixturenames:
        locale = request.getfixturevalue('randum_locale')
        fake = Randum(locale=locale)
    else:
        fake = request.getfixturevalue('_session_randum')

    seed = DEFAULT_SEED
    if 'randum_seed' in request.fixturenames:
        seed = request.getfixturevalue('randum_seed')
    fake.seed_instance(seed=seed)
    fake.unique.clear()

    return fake
