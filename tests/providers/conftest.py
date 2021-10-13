import locale as pylocale
import re

import pytest

from randum import Randum
from randum.contrib.pytest.plugin import DEFAULT_SEED

LOCALE_TEST_CLASS_NAME_REGEX = re.compile(
    r'^Test(?P<language>[A-Z][a-z]{1,2})(?P<region>[A-Z][a-z])$',
)


@pytest.fixture(scope='class', autouse=True)
def _class_locale_randum(request):
    if not request.cls:
        return None
    class_name = request.cls.__name__
    match = LOCALE_TEST_CLASS_NAME_REGEX.fullmatch(class_name)
    if not match:
        return None
    locale = f'{match.group("language")}_{match.group("region")}'
    locale = pylocale.normalize(locale).split('.')[0]
    return Randum(locale=locale)


@pytest.fixture(autouse=True)
def randum(_class_locale_randum, randum):
    if not _class_locale_randum:
        return randum
    _class_locale_randum.seed_instance(DEFAULT_SEED)
    return _class_locale_randum


@pytest.fixture(scope='class', autouse=True)
def num_samples(request):
    try:
        num = int(request.cls.num_samples)
    except AttributeError:
        num = 100
    return num
