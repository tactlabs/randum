"""TEST NOTES:

The following tests cover cases where a ``randum_session_locale`` fixture was defined
by the user as well as a user-defined ``randum_seed`` autouse fixture. In this setup,
the plugin's ``DEFAULT_SEED`` will be ignored, and ``Randum`` instances will be seeded
using the value of ``randum_seed``. Said instances are still chosen in accordance to
how ``randum_locale`` and ``randum_session_locale`` interact with each other.
"""

from random import Random

import pytest

from tests.pytest.session_overrides.session_locale import _MODULE_LOCALES

_CHANGED_SEED = 4761


@pytest.fixture()
def randum_locale():
    return ['it_IT']


@pytest.fixture(autouse=True)
def randum_seed():
    return _CHANGED_SEED


def test_no_injection(_session_randum, randum):
    random = Random(_CHANGED_SEED)
    assert randum == _session_randum
    assert randum.locales == _MODULE_LOCALES
    assert randum.random != random
    assert randum.random.getstate() == random.getstate()


def test_inject_randum_locale(_session_randum, randum, randum_locale):
    random = Random(_CHANGED_SEED)
    assert randum != _session_randum
    assert randum.locales == randum_locale
    assert randum.random != random
    assert randum.random.getstate() == random.getstate()
