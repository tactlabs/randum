import re

from unittest import mock

import pytest

from randum import Randum, providers
from randum.providers.address.cs_CZ import Provider as CsCzAddressProvider
from randum.providers.address.da_DK import Provider as DaDkAddressProvider
from randum.providers.address.de_AT import Provider as DeAtAddressProvider
from randum.providers.address.de_CH import Provider as DeChAddressProvider
from randum.providers.address.de_DE import Provider as DeDeAddressProvider
from randum.providers.address.el_GR import Provider as ElGrAddressProvider
from randum.providers.address.en_AU import Provider as EnAuAddressProvider
from randum.providers.address.en_CA import Provider as EnCaAddressProvider
from randum.providers.address.en_GB import Provider as EnGbAddressProvider
from randum.providers.address.en_IE import Provider as EnIeAddressProvider
from randum.providers.address.en_IN import Provider as EnInAddressProvider
from randum.providers.address.en_PH import Provider as EnPhAddressProvider
from randum.providers.address.en_US import Provider as EnUsAddressProvider
from randum.providers.address.es_ES import Provider as EsEsAddressProvider
from randum.providers.address.es_MX import Provider as EsMxAddressProvider
from randum.providers.address.fa_IR import Provider as FaIrAddressProvider
from randum.providers.address.fi_FI import Provider as FiFiAddressProvider
from randum.providers.address.fr_FR import Provider as FrFrAddressProvider
from randum.providers.address.he_IL import Provider as HeIlAddressProvider
from randum.providers.address.hi_IN import Provider as HiInAddressProvider
from randum.providers.address.hr_HR import Provider as HrHrAddressProvider
from randum.providers.address.hy_AM import Provider as HyAmAddressProvider
from randum.providers.address.ja_JP import Provider as JaJpAddressProvider
from randum.providers.address.ne_NP import Provider as NeNpAddressProvider
from randum.providers.address.no_NO import Provider as NoNoAddressProvider
from randum.providers.address.pt_BR import Provider as PtBrAddressProvider
from randum.providers.address.pt_PT import Provider as PtPtAddressProvider
from randum.providers.address.ro_RO import Provider as RoRoAddressProvider
from randum.providers.address.ru_RU import Provider as RuRuAddressProvider
from randum.providers.address.sk_SK import Provider as SkSkAddressProvider
from randum.providers.address.ta_IN import Provider as TaInAddressProvider
from randum.providers.address.th_TH import Provider as ThThAddressProvider
from randum.providers.address.zh_CN import Provider as ZhCnAddressProvider
from randum.providers.address.zh_TW import Provider as ZhTwAddressProvider


class TestBaseProvider:
    """Test address provider methods"""

    def test_alpha_2_country_codes(self, randum, num_samples):
        for _ in range(num_samples):
            country_code = randum.country_code(representation='alpha-2')
            assert len(country_code) == 2
            assert country_code.isalpha()

    def test_alpha_2_country_codes_as_default(self, randum, num_samples):
        for _ in range(num_samples):
            country_code = randum.country_code()
            assert len(country_code) == 2
            assert country_code.isalpha()

    def test_alpha_3_country_codes(self, randum, num_samples):
        for _ in range(num_samples):
            country_code = randum.country_code(representation='alpha-3')
            assert len(country_code) == 3
            assert country_code.isalpha()

    def test_bad_country_code_representation(self, randum, num_samples):
        for _ in range(num_samples):
            with pytest.raises(ValueError):
                randum.country_code(representation='hello')

    def _collect_randums_for_locales(self):
        cached_locales = []
        language_locale_codes = providers.BaseProvider.language_locale_codes
        for code, countries in language_locale_codes.items():
            for country in countries:
                name = f"{code}_{country}"
                try:
                    randum = Randum(name)
                    cached_locales.append(randum)
                except AttributeError as e:
                    print(f"Cannot generate randum for {name}: {e}. Skipped")

        return cached_locales

    def _randums_for_locales(self):
        if not hasattr(self.__class__, "cached_locales"):
            self.__class__.cached_locales = self._collect_randums_for_locales()
        return self.cached_locales

    def test_administrative_unit_all_locales(self):
        for randum in self._randums_for_locales():
            if randum.current_country_code() not in ["IL", "GE", "TW", "UA", "NZ"]:
                try:
                    assert isinstance(randum.administrative_unit(), str)
                except Exception as e:
                    raise e.__class__(randum.current_country_code(), *e.args)

    def test_country_code_all_locales(self):
        for randum in self._randums_for_locales():
            assert isinstance(randum.current_country(), str)

    def test_current_country_errors(self):
        dt = providers.date_time
        countries_duplicated = [*dt.Provider.countries, *dt.Provider.countries]
        with mock.patch.object(dt.Provider, "countries", countries_duplicated), pytest.raises(ValueError) as e:
            Randum("en_US").current_country()
        assert "Ambiguous" in str(e)
        country_code = "randum.providers.address.Provider.current_country_code"
        with pytest.raises(ValueError), mock.patch(country_code, lambda self: "en_ZZ"):
            Randum("en_US").current_country()


class TestCsCz:
    """Test cs_CZ address provider methods"""

    def test_street_suffix_short(self, randum, num_samples):
        for _ in range(num_samples):
            street_suffix_short = randum.street_suffix_short()
            assert isinstance(street_suffix_short, str)
            assert street_suffix_short in CsCzAddressProvider.street_suffixes_short

    def test_street_suffix_long(self, randum, num_samples):
        for _ in range(num_samples):
            street_suffix_long = randum.street_suffix_long()
            assert isinstance(street_suffix_long, str)
            assert street_suffix_long in CsCzAddressProvider.street_suffixes_long

    def test_city_name(self, randum, num_samples):
        for _ in range(num_samples):
            city = randum.city_name()
            assert isinstance(city, str)
            assert city in CsCzAddressProvider.cities

    def test_street_name(self, randum, num_samples):
        for _ in range(num_samples):
            street_name = randum.street_name()
            assert isinstance(street_name, str)
            assert street_name in CsCzAddressProvider.streets

    def test_state(self, randum, num_samples):
        for _ in range(num_samples):
            state = randum.state()
            assert isinstance(state, str)
            assert state in CsCzAddressProvider.states

    def test_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            postcode = randum.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'\d{3} \d{2}', postcode)

    def test_city_with_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            city_with_postcode = randum.city_with_postcode()
            assert isinstance(city_with_postcode, str)
            match = re.fullmatch(r'\d{3} \d{2} (?P<city>.*)', city_with_postcode)
            assert match.group('city') in CsCzAddressProvider.cities


class TestDaDk:
    """Test dk_DK address provider methods"""

    def test_street_prefix(self, randum, num_samples):
        for _ in range(num_samples):
            street_prefix = randum.street_prefix()
            assert isinstance(street_prefix, str)
            assert street_prefix in DaDkAddressProvider.street_prefixes

    def test_city_name(self, randum, num_samples):
        for _ in range(num_samples):
            city = randum.city_name()
            assert isinstance(city, str)
            assert city in DaDkAddressProvider.cities

    def test_state(self, randum, num_samples):
        for _ in range(num_samples):
            state = randum.state()
            assert isinstance(state, str)
            assert state in DaDkAddressProvider.states

    def test_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            postcode = randum.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r"\d{4}", postcode)


class TestDeAt:
    """Test de_AT address provider methods"""

    def test_city(self, randum, num_samples):
        for _ in range(num_samples):
            city = randum.city()
            assert isinstance(city, str)
            assert city in DeAtAddressProvider.cities

    def test_state(self, randum, num_samples):
        for _ in range(num_samples):
            state = randum.state()
            assert isinstance(state, str)
            assert state in DeAtAddressProvider.states

    def test_street_suffix_short(self, randum, num_samples):
        for _ in range(num_samples):
            street_suffix_short = randum.street_suffix_short()
            assert isinstance(street_suffix_short, str)
            assert street_suffix_short in DeAtAddressProvider.street_suffixes_short

    def test_street_suffix_long(self, randum, num_samples):
        for _ in range(num_samples):
            street_suffix_long = randum.street_suffix_long()
            assert isinstance(street_suffix_long, str)
            assert street_suffix_long in DeAtAddressProvider.street_suffixes_long

    def test_country(self, randum, num_samples):
        for _ in range(num_samples):
            country = randum.country()
            assert isinstance(country, str)
            assert country in DeAtAddressProvider.countries

    def test_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            postcode = randum.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'\d{4}', postcode)

    def test_city_with_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            city_with_postcode = randum.city_with_postcode()
            assert isinstance(city_with_postcode, str)
            match = re.fullmatch(r'\d{4} (?P<city>.*)', city_with_postcode)
            assert match.groupdict()['city'] in DeAtAddressProvider.cities


class TestDeDe:
    """Test de_DE address provider methods"""

    def test_city(self, randum, num_samples):
        for _ in range(num_samples):
            city = randum.city()
            assert isinstance(city, str)
            assert city in DeDeAddressProvider.cities

    def test_state(self, randum, num_samples):
        for _ in range(num_samples):
            state = randum.state()
            assert isinstance(state, str)
            assert state in DeDeAddressProvider.states

    def test_street_suffix_short(self, randum, num_samples):
        for _ in range(num_samples):
            street_suffix_short = randum.street_suffix_short()
            assert isinstance(street_suffix_short, str)
            assert street_suffix_short in DeDeAddressProvider.street_suffixes_short

    def test_street_suffix_long(self, randum, num_samples):
        for _ in range(num_samples):
            street_suffix_long = randum.street_suffix_long()
            assert isinstance(street_suffix_long, str)
            assert street_suffix_long in DeDeAddressProvider.street_suffixes_long

    def test_country(self, randum, num_samples):
        for _ in range(num_samples):
            country = randum.country()
            assert isinstance(country, str)
            assert country in DeDeAddressProvider.countries

    def test_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            postcode = randum.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'\d{5}', postcode)

    def test_city_with_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            city_with_postcode = randum.city_with_postcode()
            assert isinstance(city_with_postcode, str)
            match = re.fullmatch(r'\d{5} (?P<city>.*)', city_with_postcode)
            assert match.groupdict()['city'] in DeDeAddressProvider.cities


class TestElGr:
    """Test el_GR address provider methods"""

    def test_line_address(self, randum, num_samples):
        for _ in range(num_samples):
            address = randum.line_address()
            assert isinstance(address, str)

    def test_street_prefix_short(self, randum, num_samples):
        for _ in range(num_samples):
            street_prefix_short = randum.street_prefix_short()
            assert isinstance(street_prefix_short, str)
            assert street_prefix_short in ElGrAddressProvider.street_prefixes_short

    def test_street_prefix_long(self, randum, num_samples):
        for _ in range(num_samples):
            street_prefix_long = randum.street_prefix_long()
            assert isinstance(street_prefix_long, str)
            assert street_prefix_long in ElGrAddressProvider.street_prefixes_long

    def test_street(self, randum, num_samples):
        for _ in range(num_samples):
            street = randum.street()
            assert isinstance(street, str)
            assert street in ElGrAddressProvider.localities

    def test_city(self, randum, num_samples):
        for _ in range(num_samples):
            city = randum.city()
            assert isinstance(city, str)
            assert city in ElGrAddressProvider.cities

    def test_region(self, randum, num_samples):
        for _ in range(num_samples):
            region = randum.region()
            assert isinstance(region, str)
            assert region in ElGrAddressProvider.regions


class TestEnAu:
    """Test en_AU address provider methods"""

    def test_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            postcode = randum.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'\d{4}', postcode)

    def test_state(self, randum, num_samples):
        for _ in range(num_samples):
            state = randum.state()
            assert isinstance(state, str)
            assert state in EnAuAddressProvider.states

    def test_city_prefix(self, randum, num_samples):
        for _ in range(num_samples):
            city_prefix = randum.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in EnAuAddressProvider.city_prefixes

    def test_state_abbr(self, randum, num_samples):
        for _ in range(num_samples):
            state_abbr = randum.state_abbr()
            assert isinstance(state_abbr, str)
            assert state_abbr in EnAuAddressProvider.states_abbr
            assert state_abbr.isupper()


class TestEnNz:
    """Test en_NZ address provider methods"""

    def test_state(self, randum, num_samples):
        for _ in range(num_samples):
            # No states in New Zealand
            with pytest.raises(AttributeError):
                randum.state()

    def test_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            postcode = randum.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r"\d{4}", postcode)


class TestEnCa:
    """Test en_CA address provider methods"""

    valid_postcode_letter_re = r'[{}]'.format(
        ''.join(EnCaAddressProvider.postal_code_letters))
    valid_postcode_re = r"{0}[0-9]{0} ?[0-9]{0}[0-9]".format(valid_postcode_letter_re)

    def test_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            postcode = randum.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(self.valid_postcode_re, postcode)

    def test_postcode_in_province(self, randum, num_samples):
        for _ in range(num_samples):
            for province_abbr in EnCaAddressProvider.provinces_abbr:
                code = randum.postcode_in_province(province_abbr)
                assert code[0] in EnCaAddressProvider.provinces_postcode_prefixes[province_abbr]
                with pytest.raises(Exception):
                    randum.postcode_in_province('XX')

    def test_postalcode(self, randum, num_samples):
        for _ in range(num_samples):
            postalcode = randum.postalcode()
            assert isinstance(postalcode, str)
            assert re.fullmatch(self.valid_postcode_re, postalcode)

    def test_postal_code_letter(self, randum, num_samples):
        for _ in range(num_samples):
            postal_code_letter = randum.postal_code_letter()
            assert isinstance(postal_code_letter, str)
            assert re.fullmatch(self.valid_postcode_letter_re, postal_code_letter)

    def test_province(self, randum, num_samples):
        for _ in range(num_samples):
            province = randum.province()
            assert isinstance(province, str)
            assert province in EnCaAddressProvider.provinces

    def test_province_abbr(self, randum, num_samples):
        for _ in range(num_samples):
            province_abbr = randum.province_abbr()
            assert isinstance(province_abbr, str)
            assert province_abbr in EnCaAddressProvider.provinces_abbr

    def test_city_prefix(self, randum, num_samples):
        for _ in range(num_samples):
            city_prefix = randum.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in EnCaAddressProvider.city_prefixes

    def test_secondary_address(self, randum, num_samples):
        for _ in range(num_samples):
            secondary_address = randum.secondary_address()
            assert isinstance(secondary_address, str)
            assert re.fullmatch(r'(?:Apt\.|Suite) \d{3}', secondary_address)


class TestEnGb:
    """Test en_GB address provider methods"""

    def test_postcode(self, randum, num_samples):
        ukpcp = pytest.importorskip('ukpostcodeparser.parser')
        for _ in range(num_samples):
            assert isinstance(ukpcp.parse_uk_postcode(randum.postcode()), tuple)

    def test_county(self, randum, num_samples):
        for _ in range(num_samples):
            county = randum.county()
            assert isinstance(county, str)
            assert county in EnGbAddressProvider.counties


class TestEnIe:
    """Test en_IE address provider methods"""

    def test_postcode(self, randum, num_samples):
        """https://stackoverflow.com/questions/33391412/validation-for-irish-eircode"""
        for _ in range(num_samples):
            postcode = randum.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'(?:^[AC-FHKNPRTV-Y][0-9]{2}|D6W)[ -]?[0-9AC-FHKNPRTV-Y]{4}$', postcode)

    def test_county(self, randum, num_samples):
        for _ in range(num_samples):
            county = randum.county()
            assert isinstance(county, str)
            assert county in EnIeAddressProvider.counties


class TestEnUS:
    """Test en_US address provider methods"""

    def test_city_prefix(self, randum, num_samples):
        for _ in range(num_samples):
            city_prefix = randum.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in EnUsAddressProvider.city_prefixes

    def test_state(self, randum, num_samples):
        for _ in range(num_samples):
            state = randum.state()
            assert isinstance(state, str)
            assert state in EnUsAddressProvider.states

    def test_state_abbr(self, randum, num_samples):
        for _ in range(num_samples):
            state_abbr = randum.state_abbr()
            assert isinstance(state_abbr, str)
            states_and_territories = EnUsAddressProvider.states_and_territories_abbr
            assert state_abbr in states_and_territories

    def test_state_abbr_no_territories(self, randum, num_samples):
        for _ in range(num_samples):
            state_abbr = randum.state_abbr(include_territories=False)
            assert isinstance(state_abbr, str)
            assert state_abbr in EnUsAddressProvider.states_abbr

    def test_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            code = randum.postcode()
            assert isinstance(code, str) and len(code) == 5
            assert 501 <= int(code) <= 99950

    def test_postcode_in_state(self, randum, num_samples):
        for _ in range(num_samples):
            for state_abbr in EnUsAddressProvider.states_abbr:
                code = randum.postcode_in_state(state_abbr)
                assert re.fullmatch(r'\d{5}', code)
                assert int(code) >= EnUsAddressProvider.states_postcode[state_abbr][0]
                assert int(code) <= EnUsAddressProvider.states_postcode[state_abbr][1]

        with pytest.raises(Exception):
            randum.postcode_in_state('XX')

    def test_zipcode(self, randum, num_samples):
        for _ in range(num_samples):
            zipcode = randum.zipcode()
            assert isinstance(zipcode, str) and len(zipcode) == 5
            assert 501 <= int(zipcode) <= 99950

    def test_zipcode_in_state(self, randum, num_samples):
        for _ in range(num_samples):
            for state_abbr in EnUsAddressProvider.states_abbr:
                code = randum.zipcode_in_state(state_abbr)
                assert re.fullmatch(r"\d{5}", code)
                assert int(code) >= EnUsAddressProvider.states_postcode[state_abbr][0]
                assert int(code) <= EnUsAddressProvider.states_postcode[state_abbr][1]

        with pytest.raises(Exception):
            randum.zipcode_in_state('XX')

    def test_zipcode_plus4(self, randum, num_samples):
        for _ in range(num_samples):
            zipcode_plus4 = randum.zipcode_plus4()
            assert isinstance(zipcode_plus4, str)
            zipcode, plus4 = zipcode_plus4.split('-')
            assert 501 <= int(zipcode) <= 99950
            assert 1 <= int(plus4) <= 9999

    def test_military_ship(self, randum, num_samples):
        for _ in range(num_samples):
            military_ship = randum.military_ship()
            assert isinstance(military_ship, str)
            assert military_ship in EnUsAddressProvider.military_ship_prefix

    def test_military_state(self, randum, num_samples):
        for _ in range(num_samples):
            military_state = randum.military_state()
            assert isinstance(military_state, str)
            assert military_state in EnUsAddressProvider.military_state_abbr

    def test_military_apo(self, randum, num_samples):
        for _ in range(num_samples):
            military_apo = randum.military_apo()
            assert isinstance(military_apo, str)
            assert re.fullmatch(r'PSC \d{4}, Box \d{4}', military_apo)

    def test_military_dpo(self, randum, num_samples):
        for _ in range(num_samples):
            military_dpo = randum.military_dpo()
            assert isinstance(military_dpo, str)
            assert re.fullmatch(r'Unit \d{4} Box \d{4}', military_dpo)

    def test_postalcode(self, randum, num_samples):
        for _ in range(num_samples):
            postalcode = randum.postalcode()
            assert isinstance(postalcode, str) and len(postalcode) == 5
            assert 501 <= int(postalcode) <= 99950

    def test_postalcode_in_state(self, randum, num_samples):
        for _ in range(num_samples):
            for state_abbr in EnUsAddressProvider.states_abbr:
                code = randum.postalcode_in_state(state_abbr)
                assert re.fullmatch(r"\d{5}", code)
                assert int(code) >= EnUsAddressProvider.states_postcode[state_abbr][0]
                assert int(code) <= EnUsAddressProvider.states_postcode[state_abbr][1]

        with pytest.raises(Exception):
            randum.postalcode_in_state('XX')


class TestEsEs:
    """Test es_ES address provider methods"""

    def test_state_name(self, randum, num_samples):
        for _ in range(num_samples):
            state_name = randum.state_name()
            assert isinstance(state_name, str)
            assert state_name in EsEsAddressProvider.states

    def test_street_prefix(self, randum, num_samples):
        for _ in range(num_samples):
            street_prefix = randum.street_prefix()
            assert isinstance(street_prefix, str)
            assert street_prefix in EsEsAddressProvider.street_prefixes

    def test_secondary_address(self, randum, num_samples):
        for _ in range(num_samples):
            secondary_address = randum.secondary_address()
            assert isinstance(secondary_address, str)
            assert re.fullmatch(r'Apt\. \d{2}|Piso \d|Puerta \d', secondary_address)

    def test_regions(self, randum, num_samples):
        for _ in range(num_samples):
            region = randum.region()
            assert isinstance(region, str)
            assert region in EsEsAddressProvider.regions

    def test_autonomous_community(self, randum, num_samples):
        for _ in range(num_samples):
            # Spanish regions, also known as "autonomous communities"
            autonomous_community = randum.autonomous_community()
            assert isinstance(autonomous_community, str)
            assert autonomous_community in EsEsAddressProvider.regions


class TestEsMx:
    """Test es_MX address provider methods"""

    def test_city_prefix(self, randum, num_samples):
        for _ in range(num_samples):
            city_prefix = randum.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in EsMxAddressProvider.city_prefixes

    def test_city_suffix(self, randum, num_samples):
        for _ in range(num_samples):
            city_suffix = randum.city_suffix()
            assert isinstance(city_suffix, str)
            assert city_suffix in EsMxAddressProvider.city_suffixes

    def test_city_adjective(self, randum, num_samples):
        for _ in range(num_samples):
            city_adjective = randum.city_adjective()
            assert isinstance(city_adjective, str)
            assert city_adjective in EsMxAddressProvider.city_adjectives

    def test_street_prefix(self, randum, num_samples):
        for _ in range(num_samples):
            street_prefix = randum.street_prefix()
            assert isinstance(street_prefix, str)
            assert street_prefix in EsMxAddressProvider.street_prefixes

    def test_secondary_address(self, randum, num_samples):
        for _ in range(num_samples):
            secondary_address = randum.secondary_address()
            assert isinstance(secondary_address, str)
            assert re.fullmatch(
                r'\d{3} \d{3}|\d{3} Interior \d{3}|\d{3} Edif\. \d{3} , Depto\. \d{3}',
                secondary_address,
            )

    def test_state(self, randum, num_samples):
        states = [state_name for state_abbr, state_name in EsMxAddressProvider.states]
        for _ in range(num_samples):
            state = randum.state()
            assert isinstance(state, str)
            assert state in states

    def test_state_abbr(self, randum, num_samples):
        state_abbrs = [state_abbr for state_abbr, state_name in EsMxAddressProvider.states]
        for _ in range(num_samples):
            state_abbr = randum.state_abbr()
            assert isinstance(state_abbr, str)
            assert state_abbr in state_abbrs


class TestFaIr:
    """Test fa_IR address provider methods"""

    def test_city_prefix(self, randum, num_samples):
        for _ in range(num_samples):
            city_prefix = randum.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in FaIrAddressProvider.city_prefixes

    def test_secondary_address(self, randum, num_samples):
        for _ in range(num_samples):
            secondary_address = randum.secondary_address()
            assert isinstance(secondary_address, str)
            assert re.fullmatch(r'(?:سوئیت|واحد) \d{3}', secondary_address)

    def test_state(self, randum, num_samples):
        for _ in range(num_samples):
            state = randum.state()
            assert isinstance(state, str)
            assert state in FaIrAddressProvider.states


class TestFrFr:
    """Test fr_FR address provider methods"""

    def test_street_prefix(self, randum, num_samples):
        for _ in range(num_samples):
            street_prefix = randum.street_prefix()
            assert isinstance(street_prefix, str)
            assert street_prefix in FrFrAddressProvider.street_prefixes

    def test_city_prefix(self, randum, num_samples):
        for _ in range(num_samples):
            city_prefix = randum.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in FrFrAddressProvider.city_prefixes

    def test_region(self, randum, num_samples):
        for _ in range(num_samples):
            region = randum.region()
            assert isinstance(region, str)
            assert region in FrFrAddressProvider.regions

    def test_department(self, randum, num_samples):
        for _ in range(num_samples):
            department = randum.department()
            assert isinstance(department, tuple)
            assert department in FrFrAddressProvider.departments

    def test_department_name(self, randum, num_samples):
        department_names = [dept_name for dept_num, dept_name in FrFrAddressProvider.departments]
        for _ in range(num_samples):
            department_name = randum.department_name()
            assert isinstance(department_name, str)
            assert department_name in department_names

    def test_department_number(self, randum, num_samples):
        department_numbers = [dept_num for dept_num, dept_name in FrFrAddressProvider.departments]
        for _ in range(num_samples):
            department_number = randum.department_number()
            assert isinstance(department_number, str)
            assert department_number in department_numbers


class TestHeIl:
    """Test he_IL address provider methods"""

    def test_city_name(self, randum, num_samples):
        for _ in range(num_samples):
            city_name = randum.city_name()
            assert isinstance(city_name, str)
            assert city_name in HeIlAddressProvider.city_names

    def test_street_title(self, randum, num_samples):
        for _ in range(num_samples):
            street_title = randum.street_title()
            assert isinstance(street_title, str)
            assert street_title in HeIlAddressProvider.street_titles


class TestHiIn:
    """Test hi_IN address provider methods"""

    def test_city_name(self, randum, num_samples):
        for _ in range(num_samples):
            city_name = randum.city_name()
            assert isinstance(city_name, str)
            assert city_name in HiInAddressProvider.cities

    def test_state(self, randum, num_samples):
        for _ in range(num_samples):
            state = randum.state()
            assert isinstance(state, str)
            assert state in HiInAddressProvider.states


class TestTaIn:
    """Test ta_IN address provider methods"""

    def test_city_name(self, randum, num_samples):
        for _ in range(num_samples):
            city_name = randum.city_name()
            assert isinstance(city_name, str)
            assert city_name in TaInAddressProvider.cities

    def test_state(self, randum, num_samples):
        for _ in range(num_samples):
            state = randum.state()
            assert isinstance(state, str)
            assert state in TaInAddressProvider.states


class TestFiFi:
    """Test fi_FI address provider methods"""

    def test_city(self, randum, num_samples):
        for _ in range(num_samples):
            city = randum.city()
            assert isinstance(city, str)
            assert city in FiFiAddressProvider.cities

    def test_street_suffix(self, randum, num_samples):
        for _ in range(num_samples):
            suffix = randum.street_suffix()
            assert isinstance(suffix, str)
            assert suffix in FiFiAddressProvider.street_suffixes

    def test_state(self, randum, num_samples):
        for _ in range(num_samples):
            state = randum.state()
            assert isinstance(state, str)
            assert state in FiFiAddressProvider.states


class TestHrHr:
    """Test hr_HR address provider methods"""

    def test_city_name(self, randum, num_samples):
        for _ in range(num_samples):
            city_name = randum.city_name()
            assert isinstance(city_name, str)
            assert city_name in HrHrAddressProvider.cities

    def test_street_name(self, randum, num_samples):
        for _ in range(num_samples):
            street_name = randum.street_name()
            assert isinstance(street_name, str)
            assert street_name in HrHrAddressProvider.streets

    def test_state(self, randum, num_samples):
        for _ in range(num_samples):
            state = randum.state()
            assert isinstance(state, str)
            assert state in HrHrAddressProvider.states


class TestHuHu:
    """Test hu_HU address provider methods"""

    def test_postcode(self, randum, num_samples):
        # Hungarian postcodes begin with 'H-' followed by 4 digits.
        # The first digit may not begin with a zero.
        for _ in range(num_samples):
            pcd = randum.postcode()
            assert re.fullmatch(r'H-[1-9]\d{3}', pcd)

    def test_street_address(self, randum, num_samples):
        """
        Tests street address.

        A street address must consist of a street name, a place type and a number, and end in a period point.
        """
        for _ in range(num_samples):
            address = randum.street_address()
            assert address[-1] == '.'
            # Check for correct capitalisation of place type
            assert address.split(" ")[-2][0].islower()
            # Check for street number format
            assert re.fullmatch(r"\d{1,4}\.", address.split(" ")[-1])

    def test_street_address_with_county(self, randum, num_samples):
        """Tests street address with country. A street address must be:
        - in three rows,
        - starting with a valid street address,
        - contain a valid post code,
        - contain the place name validly capitalized.
        """
        for _ in range(num_samples):
            address = randum.street_address_with_county()
            # Number of rows
            assert len(address.split("\n")) == 3
            first, second, last = address.split("\n")

            # Test street address
            assert first[0].isupper()
            assert first.split(" ")[-2][0].islower()
            assert re.fullmatch(r"\d{1,4}\.", first.split(" ")[-1])

            # Test county line
            assert second.split(" ")[-1][0].islower()
            assert second.split(" ")[0][0].isupper()

            # Test postcode
            assert re.fullmatch(r"H-[1-9]\d{3}", last.split(" ")[0])

            # Test place name capitalization
            assert last.split(" ")[-1][0].isupper()

    def test_address(self, randum, num_samples):
        for _ in range(num_samples):
            address = randum.address()
            assert isinstance(address, str)
            address_with_county = randum.street_address_with_county()
            assert isinstance(address_with_county, str)


class TestHyAm:
    """Test hy_AM address provider methods"""

    def test_address(self, randum, num_samples):
        for _ in range(num_samples):
            address = randum.address()
            assert isinstance(address, str)

    def test_building_number(self, randum, num_samples):
        for _ in range(num_samples):
            building_number = randum.building_number()
            assert isinstance(building_number, str)
            assert 0 <= int(building_number) <= 999

    def test_city(self, randum, num_samples):
        for _ in range(num_samples):
            city = randum.city()
            assert isinstance(city, str)
            assert city in HyAmAddressProvider.cities

    def test_city_prefix(self, randum, num_samples):
        for _ in range(num_samples):
            city_prefix = randum.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in HyAmAddressProvider.city_prefixes

    def test_country(self, randum, num_samples):
        for _ in range(num_samples):
            country = randum.country()
            assert isinstance(country, str)
            assert country in HyAmAddressProvider.countries

    def test_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            postcode = randum.postcode()
            assert isinstance(postcode, str)
            assert 200 <= int(postcode) <= 4299

    def test_postcode_in_state(self, randum, num_samples):
        for _ in range(num_samples):
            for state_abbr in HyAmAddressProvider.states_abbr:
                code = randum.postcode_in_state(state_abbr)
                assert re.fullmatch(r"\d{4}", code)
                assert int(code) >= HyAmAddressProvider.states_postcode[state_abbr][0]
                assert int(code) <= HyAmAddressProvider.states_postcode[state_abbr][1]

        with pytest.raises(Exception):
            randum.postcode_in_state('XX')

    def test_secondary_address(self, randum, num_samples):
        for _ in range(num_samples):
            secondary_address = randum.secondary_address()
            assert isinstance(secondary_address, str)
            assert re.fullmatch(r'բն\. \d{1,2}', secondary_address)

    def test_state(self, randum, num_samples):
        for _ in range(num_samples):
            state = randum.state()
            assert isinstance(state, str)
            assert state in HyAmAddressProvider.states

    def test_state_abbr(self, randum, num_samples):
        for _ in range(num_samples):
            state_abbr = randum.state_abbr()
            assert isinstance(state_abbr, str)
            assert state_abbr in HyAmAddressProvider.states_abbr
            assert state_abbr.isupper()

    def test_street(self, randum, num_samples):
        for _ in range(num_samples):
            street = randum.street()
            assert isinstance(street, str)
            assert street in HyAmAddressProvider.streets

    def test_street_address(self, randum, num_samples):
        for _ in range(num_samples):
            street_address = randum.street_address()
            assert isinstance(street_address, str)

    def test_street_name(self, randum, num_samples):
        for _ in range(num_samples):
            street_name = randum.street_name()
            assert isinstance(street_name, str)

    def test_street_prefix(self, randum, num_samples):
        for _ in range(num_samples):
            street_prefix = randum.street_prefix()
            assert isinstance(street_prefix, str)
            assert street_prefix in HyAmAddressProvider.street_prefixes

    def test_street_suffix(self, randum, num_samples):
        for _ in range(num_samples):
            suffix = randum.street_suffix()
            assert isinstance(suffix, str)
            assert suffix in HyAmAddressProvider.street_suffixes

    def test_village(self, randum, num_samples):
        for _ in range(num_samples):
            village = randum.village()
            assert isinstance(village, str)
            assert village in HyAmAddressProvider.villages

    def test_village_prefix(self, randum, num_samples):
        for _ in range(num_samples):
            village_prefix = randum.village_prefix()
            assert isinstance(village_prefix, str)
            assert village_prefix in HyAmAddressProvider.village_prefixes


class TestJaJp:
    """Test ja_JP address provider methods"""

    def test_chome(self, randum, num_samples):
        for _ in range(num_samples):
            chome = randum.chome()
            assert isinstance(chome, str)
            match = re.fullmatch(r"(?P<chome_number>\d{1,2})丁目", chome)
            assert match
            assert 1 <= int(match.group('chome_number')) <= 42

    def test_ban(self, randum, num_samples):
        for _ in range(num_samples):
            ban = randum.ban()
            assert isinstance(ban, str)
            match = re.fullmatch(r"(?P<ban_number>\d{1,2})番", ban)
            assert match
            assert 1 <= int(match.group('ban_number')) <= 27

    def test_gou(self, randum, num_samples):
        for _ in range(num_samples):
            gou = randum.gou()
            assert isinstance(gou, str)
            match = re.fullmatch(r"(?P<gou_number>\d{1,2})号", gou)
            assert match
            assert 1 <= int(match.group('gou_number')) <= 20

    def test_town(self, randum, num_samples):
        for _ in range(num_samples):
            town = randum.town()
            assert isinstance(town, str)
            assert town in JaJpAddressProvider.towns

    def test_prefecture(self, randum, num_samples):
        for _ in range(num_samples):
            prefecture = randum.prefecture()
            assert isinstance(prefecture, str)
            assert prefecture in JaJpAddressProvider.prefectures

    def test_city(self, randum, num_samples):
        for _ in range(num_samples):
            city = randum.city()
            assert isinstance(city, str)
            assert city in JaJpAddressProvider.cities

    def test_country(self, randum, num_samples):
        for _ in range(num_samples):
            country = randum.country()
            assert isinstance(country, str)
            assert country in JaJpAddressProvider.countries

    def test_building_name(self, randum, num_samples):
        for _ in range(num_samples):
            building_name = randum.building_name()
            assert isinstance(building_name, str)
            assert building_name in JaJpAddressProvider.building_names

    def test_address(self, randum, num_samples):
        for _ in range(num_samples):
            address = randum.address()
            assert isinstance(address, str)

    def test_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            postcode = randum.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'\d{3}-\d{4}', postcode)

    def test_zipcode(self, randum, num_samples):
        for _ in range(num_samples):
            zipcode = randum.zipcode()
            assert isinstance(zipcode, str)
            assert re.fullmatch(r'\d{3}-\d{4}', zipcode)


class TestKoKr:
    """Test ko_KR address provider methods"""

    def test_old_postal_code(self, randum, num_samples):
        for _ in range(num_samples):
            old_postal_code = randum.old_postal_code()
            assert isinstance(old_postal_code, str)
            assert re.fullmatch(r'\d{3}-\d{3}', old_postal_code)

    def test_postal_code(self, randum, num_samples):
        for _ in range(num_samples):
            postal_code = randum.postal_code()
            assert isinstance(postal_code, str)
            assert re.fullmatch(r'\d{5}', postal_code)

    def test_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            postcode = randum.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'\d{5}', postcode)


class TestNeNp:
    """Test ne_NP address provider methods"""

    def test_province(self, randum, num_samples):
        for _ in range(num_samples):
            province = randum.province()
            assert isinstance(province, str)
            assert province in NeNpAddressProvider.provinces

    def test_district(self, randum, num_samples):
        for _ in range(num_samples):
            district = randum.district()
            assert isinstance(district, str)
            assert district in NeNpAddressProvider.districts

    def test_city(self, randum, num_samples):
        for _ in range(num_samples):
            city = randum.city()
            assert isinstance(city, str)
            assert city in NeNpAddressProvider.cities

    def test_country(self, randum, num_samples):
        for _ in range(num_samples):
            country = randum.country()
            assert isinstance(country, str)
            assert country in NeNpAddressProvider.countries


class TestNoNo:
    """Test no_NO address provider methods"""

    def test_postcode(self, randum):
        for _ in range(100):
            assert re.fullmatch(r'^[0-9]{4}$', randum.postcode())

    def test_city_suffix(self, randum, num_samples):
        for _ in range(num_samples):
            city_suffix = randum.city_suffix()
            assert isinstance(city_suffix, str)
            assert city_suffix in NoNoAddressProvider.city_suffixes

    def test_street_suffix(self, randum, num_samples):
        for _ in range(num_samples):
            street_suffix = randum.street_suffix()
            assert isinstance(street_suffix, str)
            assert street_suffix in NoNoAddressProvider.street_suffixes

    def test_address(self, randum, num_samples):
        for _ in range(num_samples):
            address = randum.address()
            assert isinstance(address, str)


class TestZhTw:
    """Test zh_TW address provider methods"""

    def test_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            postcode = randum.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'[1-9]\d{2}(?:\d{2})?', postcode)

    def test_city_name(self, randum, num_samples):
        for _ in range(num_samples):
            city_name = randum.city_name()
            assert isinstance(city_name, str)
            assert city_name in ZhTwAddressProvider.cities

    def test_city_suffix(self, randum, num_samples):
        for _ in range(num_samples):
            city_suffix = randum.city_suffix()
            assert isinstance(city_suffix, str)
            assert city_suffix in ZhTwAddressProvider.city_suffixes

    def test_city(self, randum, num_samples):
        city_pattern = re.compile(r'(?P<city_name>.*?)[市縣]?')
        for _ in range(num_samples):
            city = randum.city()
            assert isinstance(city, str)
            match = city_pattern.fullmatch(city)
            assert match
            assert match.group('city_name') in ZhTwAddressProvider.cities

    def test_country(self, randum, num_samples):
        for _ in range(num_samples):
            country = randum.country()
            assert isinstance(country, str)
            assert country in ZhTwAddressProvider.countries

    def test_street_name(self, randum, num_samples):
        for _ in range(num_samples):
            street_name = randum.street_name()
            assert isinstance(street_name, str)
            assert street_name in ZhTwAddressProvider.street_names

    def test_address(self, randum, num_samples):
        for _ in range(num_samples):
            address = randum.address()
            assert isinstance(address, str)


class TestZhCn:
    """Test zh_CN address provider methods"""

    def test_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            postcode = randum.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'[1-9]\d{5}', postcode)

    def test_city_name(self, randum, num_samples):
        for _ in range(num_samples):
            city_name = randum.city_name()
            assert isinstance(city_name, str)
            assert city_name in ZhCnAddressProvider.cities

    def test_city_suffix(self, randum, num_samples):
        for _ in range(num_samples):
            city_suffix = randum.city_suffix()
            assert isinstance(city_suffix, str)
            assert city_suffix in ZhCnAddressProvider.city_suffixes

    def test_city(self, randum, num_samples):
        city_pattern = re.compile(r'.*?[市县]')
        for _ in range(num_samples):
            city = randum.city()
            assert isinstance(city, str)
            assert city_pattern.fullmatch(city)

    def test_province(self, randum, num_samples):
        for _ in range(num_samples):
            province = randum.province()
            assert isinstance(province, str)
            assert province in ZhCnAddressProvider.provinces

    def test_district(self, randum, num_samples):
        for _ in range(num_samples):
            district = randum.district()
            assert isinstance(district, str)
            assert district in ZhCnAddressProvider.districts

    def test_country(self, randum, num_samples):
        for _ in range(num_samples):
            country = randum.country()
            assert isinstance(country, str)
            assert country in ZhCnAddressProvider.countries

    def test_street_name(self, randum, num_samples):
        for _ in range(num_samples):
            street_name = randum.street_name()
            assert isinstance(street_name, str)

    def test_address(self, randum, num_samples):
        for _ in range(num_samples):
            address = randum.address()
            assert isinstance(address, str)


class TestPtBr:
    """Test pt_BR address provider methods"""

    def test_country(self, randum, num_samples):
        for _ in range(num_samples):
            country = randum.country()
            assert isinstance(country, str)
            assert country in PtBrAddressProvider.countries

    def test_bairro(self, randum, num_samples):
        for _ in range(num_samples):
            bairro = randum.bairro()
            assert isinstance(bairro, str)
            assert bairro in PtBrAddressProvider.bairros

    def test_neighborhood(self, randum, num_samples):
        for _ in range(num_samples):
            neighborhood = randum.neighborhood()
            assert isinstance(neighborhood, str)
            assert neighborhood in PtBrAddressProvider.bairros

    def test_estado(self, randum, num_samples):
        for _ in range(num_samples):
            estado = randum.estado()
            assert isinstance(estado, tuple)
            assert estado in PtBrAddressProvider.estados

    def test_estado_nome(self, randum, num_samples):
        state_names = [state_name for state_abbr, state_name in PtBrAddressProvider.estados]
        for _ in range(num_samples):
            estado_nome = randum.estado_nome()
            assert isinstance(estado_nome, str)
            assert estado_nome in state_names

    def test_estado_sigla(self, randum, num_samples):
        state_abbrs = [state_abbr for state_abbr, state_name in PtBrAddressProvider.estados]
        for _ in range(num_samples):
            estado_sigla = randum.estado_sigla()
            assert isinstance(estado_sigla, str)
            assert estado_sigla in state_abbrs

    def test_address(self, randum, num_samples):
        for _ in range(num_samples):
            street = randum.street_name()
            assert isinstance(street, str)
            city = randum.street_address()
            assert isinstance(city, str)
            address = randum.address()
            assert isinstance(address, str)

    def test_raw_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            postcode = randum.postcode(formatted=False)
            assert isinstance(postcode, str)
            assert re.fullmatch(r'\d{8}', postcode)

    def test_formatted_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            postcode = randum.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'\d{5}-?\d{3}', postcode)


class TestPtPt:
    """Test pt_PT address provider methods"""

    def test_distrito(self, randum, num_samples):
        for _ in range(num_samples):
            distrito = randum.distrito()
            assert isinstance(distrito, str)
            assert distrito in PtPtAddressProvider.distritos

    def test_concelho(self, randum, num_samples):
        for _ in range(num_samples):
            concelho = randum.concelho()
            assert isinstance(concelho, str)
            assert concelho in PtPtAddressProvider.concelhos

    def test_freguesia(self, randum, num_samples):
        for _ in range(num_samples):
            freguesia = randum.freguesia()
            assert isinstance(freguesia, str)
            assert freguesia in PtPtAddressProvider.freguesias

    def test_place_name(self, randum, num_samples):
        for _ in range(num_samples):
            place_name = randum.place_name()
            assert isinstance(place_name, str)
            assert place_name in PtPtAddressProvider.places


class TestEnPh:
    """Test en_PH address provider methods"""

    @classmethod
    def setup_class(cls):
        cls.building_number_pattern = re.compile(
            r'(?:[1-9]|[1-9]\d{1,3})(?:[A-J]|\s[A-J]|-[A-J]|\sUnit\s[A-J])?',
        )
        cls.address_pattern = re.compile(
            r'(?P<street_address>.*), (?P<lgu>.*?), (?P<postcode>\d{4}) (?P<province>.*?)',
        )
        cls.metro_manila_postcodes = EnPhAddressProvider.metro_manila_postcodes
        cls.luzon_province_postcodes = EnPhAddressProvider.luzon_province_postcodes
        cls.visayas_province_postcodes = EnPhAddressProvider.visayas_province_postcodes
        cls.mindanao_province_postcodes = EnPhAddressProvider.mindanao_province_postcodes
        cls.postcodes = EnPhAddressProvider.postcodes
        cls.provinces = EnPhAddressProvider.provinces
        cls.province_lgus = EnPhAddressProvider.province_lgus
        cls.metro_manila_lgus = EnPhAddressProvider.metro_manila_lgus

    def test_metro_manila_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            assert int(randum.metro_manila_postcode()) in self.metro_manila_postcodes

    def test_luzon_province_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            assert int(randum.luzon_province_postcode()) in self.luzon_province_postcodes

    def test_visayas_province_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            assert int(randum.visayas_province_postcode()) in self.visayas_province_postcodes

    def test_mindanao_province_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            assert int(randum.mindanao_province_postcode()) in self.mindanao_province_postcodes

    def test_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            assert int(randum.postcode()) in self.postcodes

    def test_building_number(self, randum, num_samples):
        for _ in range(num_samples):
            assert self.building_number_pattern.fullmatch(randum.building_number())

    def test_floor_unit_number(self, randum, num_samples):
        for _ in range(num_samples):
            number = randum.floor_unit_number()
            assert 2 <= int(number[:-2]) <= 99
            assert 1 <= int(number[-2:]) <= 40

    def test_ordinal_floor_number(self, randum, num_samples):
        for _ in range(num_samples):
            floor_number = randum.ordinal_floor_number()
            assert floor_number[-2:] in ['th', 'st', 'nd', 'rd']

    def test_address(self, randum, num_samples):
        for _ in range(num_samples):
            address = randum.address()
            match = self.address_pattern.fullmatch(address)
            street_address = match.group('street_address')
            lgu = match.group('lgu')
            postcode = match.group('postcode')
            province = match.group('province')
            assert match
            assert street_address
            assert lgu in self.province_lgus or lgu in self.metro_manila_lgus
            assert int(postcode) in self.postcodes
            assert province in self.provinces or province == 'Metro Manila'


class TestFilPh(TestEnPh):
    """Test fil_PH address provider methods"""
    pass


class TestTlPh(TestEnPh):
    """Test tl_PH address provider methods"""
    pass


class TestRuRu:
    """Test ru_RU address provider methods"""

    def test_city_name(self, randum, num_samples):
        for _ in range(num_samples):
            city = randum.city_name()
            assert isinstance(city, str)
            assert city in RuRuAddressProvider.city_names

    def test_country(self, randum, num_samples):
        for _ in range(num_samples):
            country = randum.country()
            assert isinstance(country, str)
            assert country in RuRuAddressProvider.countries

    def test_region(self, randum, num_samples):
        region_pattern = re.compile(
            r'(?:респ\. (?P<region_republic>.*))|'
            r'(?:(?P<region_krai>.*?) край)|'
            r'(?:(?P<region_oblast>.*?) обл.)|'
            r'(?:(?P<region_ao>.*?) АО)',
        )
        for _ in range(num_samples):
            region = randum.region()
            assert isinstance(region, str)
            match = region_pattern.fullmatch(region)
            assert match
            groupdict = match.groupdict()
            assert any([
                groupdict.get('region_republic') in RuRuAddressProvider.region_republics,
                groupdict.get('region_krai') in RuRuAddressProvider.region_krai,
                groupdict.get('region_oblast') in RuRuAddressProvider.region_oblast,
                groupdict.get('region_ao') in RuRuAddressProvider.region_ao,
            ])

    def test_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            postcode = randum.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'\d{6}', postcode)

    def test_city_prefix(self, randum, num_samples):
        for _ in range(num_samples):
            city_prefix = randum.city_prefix()
            assert isinstance(city_prefix, str)
            assert city_prefix in RuRuAddressProvider.city_prefixes

    def test_street_suffix(self, randum, num_samples):
        for _ in range(num_samples):
            street_suffix = randum.street_suffix()
            assert isinstance(street_suffix, str)
            assert street_suffix in RuRuAddressProvider.street_suffixes

    def test_street_title(self, randum, num_samples):
        for _ in range(num_samples):
            street_title = randum.street_title()
            assert isinstance(street_title, str)

    def test_street_name(self, randum, num_samples):
        for _ in range(num_samples):
            street_name = randum.street_name()
            assert isinstance(street_name, str)

    @pytest.mark.parametrize("street_title,street_suffix,expected", [
        ("Фрунзе", "ул.", "ул. Фрунзе"),
        ("Ставропольская", "ул.", "ул. Ставропольская"),
        ("Фрунзе", "пр.", "пр. Фрунзе"),
        ("Осенняя", "пр.", "пр. Осенний"),
        ("Гвардейская", "пр.", "пр. Гвардейский"),
        ("Рыбацкая", "пр.", "пр. Рыбацкий"),
        ("Безымянная", "пр.", "пр. Безымянный"),
        ("Проезжая", "ш.", "ш. Проезжее"),
        ("Магистральная", "ш.", "ш. Магистральное"),
    ], ids=[
        "feminine_suffix_and_noflex_title",
        "feminine_suffix_and_flex_title",
        "non_feminine_suffix_and_noflex_title",
        "masc_suffix_and_irregular_masc_title",
        "masc_suffix_and_ck_street_stem",
        "masc_suffix_and_uk_street_stem",
        "masc_suffix_and_other_stem",
        "neu_suffx_and_iregular_neu_street_title",
        "neu_suffix_and_regular_street_title",
    ])
    def test_street_name_lexical(self, randum, street_title, street_suffix, expected):
        """Test that random street names are formed correctly, given
        the case of suffixes and streets that have been randomly selected.
        """
        title_patch = mock.patch(
            "randum.providers.address.ru_RU.Provider.street_title",
            autospec=True,
            return_value=street_title,
        )
        suffix_patch = mock.patch(
            "randum.providers.address.ru_RU.Provider.street_suffix",
            autospec=True,
            return_value=street_suffix,
        )

        with title_patch, suffix_patch:
            result = randum.street_name()
            assert result == expected


class TestThTh:
    """Test th_TH address provider methods"""

    def test_country(self, randum, num_samples):
        for _ in range(num_samples):
            country = randum.country()
            assert isinstance(country, str)
            assert country in ThThAddressProvider.countries

    def test_city_name(self, randum, num_samples):
        for _ in range(num_samples):
            city = randum.city_name()
            assert isinstance(city, str)
            assert city in ThThAddressProvider.cities

    def test_province(self, randum, num_samples):
        for _ in range(num_samples):
            province = randum.province()
            assert isinstance(province, str)
            assert province in ThThAddressProvider.provinces

    def test_amphoe(self, randum, num_samples):
        for _ in range(num_samples):
            amphoe = randum.amphoe()
            assert isinstance(amphoe, str)
            assert amphoe in ThThAddressProvider.amphoes

    def test_tambon(self, randum, num_samples):
        for _ in range(num_samples):
            tambon = randum.tambon()
            assert isinstance(tambon, str)

    def test_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            postcode = randum.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'[1-9]\d{4}', postcode)


class TestEnIn:
    """Test en_IN address provider methods"""

    def test_city_name(self, randum, num_samples):
        for _ in range(num_samples):
            city_name = randum.city_name()
            assert isinstance(city_name, str)
            assert city_name in EnInAddressProvider.cities

    def test_state(self, randum, num_samples):
        for _ in range(num_samples):
            state = randum.state()
            assert isinstance(state, str)
            assert state in EnInAddressProvider.states


class TestSkSk:
    """Test sk_SK address provider methods"""

    def test_street_suffix_short(self, randum, num_samples):
        for _ in range(num_samples):
            street_suffix_short = randum.street_suffix_short()
            assert isinstance(street_suffix_short, str)
            assert street_suffix_short in SkSkAddressProvider.street_suffixes_short

    def test_street_suffix_long(self, randum, num_samples):
        for _ in range(num_samples):
            street_suffix_long = randum.street_suffix_long()
            assert isinstance(street_suffix_long, str)
            assert street_suffix_long in SkSkAddressProvider.street_suffixes_long

    def test_city_name(self, randum, num_samples):
        for _ in range(num_samples):
            city = randum.city_name()
            assert isinstance(city, str)
            assert city in SkSkAddressProvider.cities

    def test_street_name(self, randum, num_samples):
        for _ in range(num_samples):
            street_name = randum.street_name()
            assert isinstance(street_name, str)
            assert street_name in SkSkAddressProvider.streets

    def test_state(self, randum, num_samples):
        for _ in range(num_samples):
            state = randum.state()
            assert isinstance(state, str)
            assert state in SkSkAddressProvider.states

    def test_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            postcode = randum.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'\d{3} \d{2}', postcode)

    def test_city_with_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            city_with_postcode = randum.city_with_postcode()
            assert isinstance(city_with_postcode, str)
            match = re.fullmatch(r'\d{3} \d{2} (?P<city>.*)',
                                 city_with_postcode)
            assert match.group('city') in SkSkAddressProvider.cities


class TestDeCh:
    """Test de_CH address provider methods"""

    def test_canton_name(self, randum, num_samples):
        for _ in range(num_samples):
            canton_name = randum.canton_name()
            assert isinstance(canton_name, str)
            assert any(canton_name == cantons[1] for cantons in DeChAddressProvider.cantons)

    def test_canton_code(self, randum, num_samples):
        for _ in range(num_samples):
            canton_code = randum.canton_code()
            assert isinstance(canton_code, str)
            assert any(canton_code == cantons[0] for cantons in DeChAddressProvider.cantons)

    def test_canton(self, randum, num_samples):
        for _ in range(num_samples):
            canton = randum.canton()
            assert isinstance(canton, tuple)
            assert canton in DeChAddressProvider.cantons


class TestRoRo:
    """Test ro_RO address provider methods"""

    def test_address(self, randum, num_samples):
        for _ in range(num_samples):
            address = randum.address()
            assert isinstance(address, str)

    def test_street_address(self, randum, num_samples):
        for _ in range(num_samples):
            street_address = randum.street_address()
            assert isinstance(street_address, str)

    def test_street_name(self, randum, num_samples):
        for _ in range(num_samples):
            street_name = randum.street_name()
            assert isinstance(street_name, str)

    def test_street_prefix(self, randum, num_samples):
        for _ in range(num_samples):
            street_prefix = randum.street_prefix()
            assert isinstance(street_prefix, str)
            assert street_prefix in RoRoAddressProvider.street_prefixes

    def test_building_number(self, randum, num_samples):
        for _ in range(num_samples):
            building_number = randum.building_number()
            assert isinstance(building_number, str)
            assert building_number[:3] == 'Nr.'

    def test_secondary_address(self, randum, num_samples):
        for _ in range(num_samples):
            secondary_address = randum.secondary_address()
            assert isinstance(secondary_address, str)
            assert re.fullmatch(
                r'Bl. \d{2}  Sc. \d{2} Ap. \d{3}',
                secondary_address,
            )

    def test_city(self, randum, num_samples):
        for _ in range(num_samples):
            city = randum.city()
            assert isinstance(city, str)
            assert city in RoRoAddressProvider.cities

    def test_city_name(self, randum, num_samples):
        for _ in range(num_samples):
            city = randum.city_name()
            assert isinstance(city, str)
            assert city in RoRoAddressProvider.cities

    def test_state(self, randum, num_samples):
        states = [state_name for state_abbr, state_name in RoRoAddressProvider.states]
        for _ in range(num_samples):
            state = randum.state()
            assert isinstance(state, str)
            assert state in states

    def test_state_abbr(self, randum, num_samples):
        state_abbrs = [state_abbr for state_abbr, state_name in RoRoAddressProvider.states]
        for _ in range(num_samples):
            state_abbr = randum.state_abbr()
            assert isinstance(state_abbr, str)
            assert state_abbr in state_abbrs
            assert state_abbr.isupper()

    def test_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            postcode = randum.postcode()
            assert isinstance(postcode, str)
            assert re.fullmatch(r'\d{6}', postcode)

    def test_city_with_postcode(self, randum, num_samples):
        for _ in range(num_samples):
            city_with_postcode = randum.city_with_postcode()
            assert isinstance(city_with_postcode, str)
            match = re.fullmatch(r'\d{6} (?P<city>.*)',
                                 city_with_postcode)
            assert match.group('city') in RoRoAddressProvider.cities
