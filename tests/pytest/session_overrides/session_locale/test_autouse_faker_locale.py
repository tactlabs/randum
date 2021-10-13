"""TEST NOTES:

The following tests cover cases where a ``randum_session_locale`` fixture was defined
by the user as well as a user-defined ``randum_locale`` autouse fixture. In this setup,
the value of ``randum_session_locale`` will be ignored, since the plugin's session level
``Randum`` instance will not be used. Each test will instead generate a new instance using
the value of ``randum_locale``. These new instances will be still seeded in accordance to
the plugin's seeding rules.
"""

from random import Random

import pytest

from randum.contrib.pytest.plugin import DEFAULT_SEED

_CHANGED_LOCALE = ['it_IT']


@pytest.fixture(autouse=True)
def randum_locale():
    return _CHANGED_LOCALE


@pytest.fixture()
def randum_seed():
    return 4761


def test_no_injection(_session_randum, randum):
    random = Random(DEFAULT_SEED)
    assert randum != _session_randum
    assert randum.locales == _CHANGED_LOCALE
    assert randum.random != random
    assert randum.random.getstate() == random.getstate()


def test_inject_randum_seed(_session_randum, randum, randum_seed):
    random = Random(randum_seed)
    assert randum != _session_randum
    assert randum.locales == _CHANGED_LOCALE
    assert randum.random != random
    assert randum.random.getstate() == random.getstate()
