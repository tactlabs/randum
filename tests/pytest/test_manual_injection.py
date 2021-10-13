"""TEST NOTES:

The following tests cover cases where a ``randum_session_locale`` fixture was not
defined by the user, but non-autouse ``randum_locale`` and ``randum_seed`` fixtures
were defined. The resulting behavior of the ``randum`` fixture will vary dependening
on which fixtures are injected.
"""


from random import Random

import pytest

from randum.contrib.pytest.plugin import DEFAULT_LOCALE, DEFAULT_SEED


@pytest.fixture()
def randum_locale():
    return ['it_IT']


@pytest.fixture()
def randum_seed():
    return 4761


def test_no_injection(_session_randum, randum):
    random = Random(DEFAULT_SEED)
    assert randum == _session_randum
    assert randum.locales == [DEFAULT_LOCALE]
    assert randum.random != random
    assert randum.random.getstate() == random.getstate()


def test_inject_randum_locale(_session_randum, randum, randum_locale):
    random = Random(DEFAULT_SEED)
    assert randum != _session_randum
    assert randum.locales == randum_locale
    assert randum.random != random
    assert randum.random.getstate() == random.getstate()


def test_inject_randum_seed(_session_randum, randum, randum_seed):
    random = Random(randum_seed)
    assert randum == _session_randum
    assert randum.locales == [DEFAULT_LOCALE]
    assert randum.random != random
    assert randum.random.getstate() == random.getstate()


def test_inject_randum_seed_and_locale(_session_randum, randum, randum_locale, randum_seed):
    random = Random(randum_seed)
    assert randum != _session_randum
    assert randum.locales == randum_locale
    assert randum.random != random
    assert randum.random.getstate() == random.getstate()
