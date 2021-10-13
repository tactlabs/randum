import re

import pytest

from randum.providers.bank import Provider as BankProvider
from randum.providers.bank.de_CH import Provider as DeChBankProvider
from randum.providers.bank.el_GR import Provider as ElGrBankProvider
from randum.providers.bank.en_GB import Provider as EnGbBankProvider
from randum.providers.bank.en_IE import Provider as EnIeBankProvider
from randum.providers.bank.en_PH import Provider as EnPhBankProvider
from randum.providers.bank.es_ES import Provider as EsEsBankProvider
from randum.providers.bank.fi_FI import Provider as FiFiBankProvider
from randum.providers.bank.fr_FR import Provider as FrFrBankProvider
from randum.providers.bank.no_NO import Provider as NoNoBankProvider
from randum.providers.bank.pl_PL import Provider as PlPlBankProvider
from randum.providers.bank.pt_PT import Provider as PtPtBankProvider
from randum.providers.bank.th_TH import Provider as ThThBankProvider
from randum.providers.bank.tr_TR import Provider as TrTrBankProvider


def is_valid_iban(iban):
    check = iban[4:] + iban[:4]
    check = int(''.join(BankProvider.ALPHA.get(c, c) for c in check))
    return check % 97 == 1


def is_valid_aba(aba):
    d = [int(n) for n in aba]
    chkdgt = (3*(d[0]+d[3]+d[6]) + 7*(d[1]+d[4]+d[7]) + (d[2]+d[5]+d[8]))
    if chkdgt % 10 == 0:
        return True
    return False


class TestNoNo:
    """Test no_NO bank provider"""
    def test_aba(self, randum, num_samples):
        for _ in range(num_samples):
            aba = randum.aba()
            assert len(aba) == 9
            assert is_valid_aba(aba)

    def test_bban(self, randum, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{11}", randum.bban())

    def test_iban(self, randum, num_samples):
        for _ in range(num_samples):
            iban = randum.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == NoNoBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{11}", iban[2:])


class TestFiFi:
    """Test fi_FI bank provider"""

    def test_bban(self, randum, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{14}", randum.bban())

    def test_iban(self, randum, num_samples):
        for _ in range(num_samples):
            iban = randum.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == FiFiBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{14}", iban[2:])


class TestPlPl:
    """Test pl_PL bank provider"""

    def test_bban(self, randum, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{26}", randum.bban())

    def test_iban(self, randum, num_samples):
        for _ in range(num_samples):
            iban = randum.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == PlPlBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{26}", iban[2:])


class TestEnGb:
    """Test en_GB bank provider"""

    def test_bban(self, randum, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"[A-Z]{4}\d{14}", randum.bban())

    def test_iban(self, randum, num_samples):
        for _ in range(num_samples):
            iban = randum.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == EnGbBankProvider.country_code
            assert re.fullmatch(r"\d{2}[A-Z]{4}\d{14}", iban[2:])


class TestEnIe:
    """Test en_IE bank provider"""

    def test_bban(self, randum, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{23}", randum.bban())

    def test_iban(self, randum, num_samples):
        for _ in range(num_samples):
            iban = randum.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == EnIeBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{23}", iban[2:])


class TestRuRu:
    """Test ru_RU bank provider"""

    def test_bic(self, randum, num_samples):
        for _ in range(num_samples):
            assert re.match(r"04\d{7,9}", randum.bic())

    def test_correspondent_account(self, randum, num_samples):
        for _ in range(num_samples):
            assert re.match(r"301\d{17}", randum.correspondent_account())

    def test_checking_account(self, randum, num_samples):
        for _ in range(num_samples):
            assert re.match(r"\d{3}0\d{16}", randum.checking_account())

    def test_bank(self, randum, num_samples):
        for _ in range(num_samples):
            assert re.match(r"\D{3,41}", randum.bank())


class TestPtPt:
    """Test pt_PT bank provider"""

    def test_bban(self, randum, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{21}", randum.bban())

    def test_iban(self, randum, num_samples):
        for _ in range(num_samples):
            iban = randum.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == PtPtBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{21}", iban[2:])


class TestEsEs:
    """Test es_ES bank provider"""

    def test_bban(self, randum, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{20}", randum.bban())

    def test_iban(self, randum, num_samples):
        for _ in range(num_samples):
            iban = randum.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == EsEsBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{20}", iban[2:])


class TestFrFr:
    """Test fr_FR bank provider"""

    def test_bban(self, randum, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{23}", randum.bban())

    def test_iban(self, randum, num_samples):
        for _ in range(num_samples):
            iban = randum.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == FrFrBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{23}", iban[2:])


class TestEnPh:
    """Test en_PH bank provider"""

    def test_swift(self, randum, num_samples):
        regex = re.compile('[A-Z]{4}PH[A-Z0-9]{2}(?:[A-Z0-9]{3})?')
        for _ in range(num_samples):
            code = randum.swift()
            assert regex.fullmatch(code) is not None

    def test_swift_invalid_length(self, randum):
        randum.swift(length=8)
        randum.swift(length=11)
        with pytest.raises(AssertionError):
            randum.swift(length=5)

    def test_swift8_use_dataset(self, randum, num_samples):
        for _ in range(num_samples):
            code = randum.swift8(use_dataset=True)
            assert len(code) == 8
            assert code[:4] in EnPhBankProvider.swift_bank_codes
            assert code[4:6] == EnPhBankProvider.country_code
            assert code[6:8] in EnPhBankProvider.swift_location_codes

    def test_swift11_use_dataset(self, randum, num_samples):
        for _ in range(num_samples):
            code = randum.swift11(use_dataset=True)
            assert len(code) == 11
            assert code[:4] in EnPhBankProvider.swift_bank_codes
            assert code[4:6] == EnPhBankProvider.country_code
            assert code[6:8] in EnPhBankProvider.swift_location_codes
            assert code[8:11] in EnPhBankProvider.swift_branch_codes

    def test_swift11_is_primary(self, randum, num_samples):
        for _ in range(num_samples):
            code = randum.swift11(primary=True)
            assert len(code) == 11
            assert code[8:11] == 'XXX'


class TestFilPh(TestEnPh):
    """Test fil_PH bank provider"""
    pass


class TestTlPh(TestEnPh):
    """Test tl_PH bank provider"""
    pass


class TestTrTr:
    """Test tr_TR bank provider"""

    def test_bban(self, randum, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{22}", randum.bban())

    def test_iban(self, randum, num_samples):
        for _ in range(num_samples):
            iban = randum.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == TrTrBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{22}", iban[2:])


class TestDeCh:
    """Test de_CH bank provider"""

    def test_bban(self, randum, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{17}", randum.bban())

    def test_iban(self, randum, num_samples):
        for _ in range(num_samples):
            iban = randum.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == DeChBankProvider.country_code
            assert re.fullmatch(r"\d{19}", iban[2:])


class TestFrCh(TestDeCh):
    """Test fr_CH bank provider"""
    pass


class TestItCh(TestDeCh):
    """Test it_CH bank provider"""
    pass


class TestThTh:
    """Test th_TH bank provider"""

    def test_bban(self, randum, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{10}", randum.bban())

    def test_iban(self, randum, num_samples):
        for _ in range(num_samples):
            iban = randum.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == ThThBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{10}", iban[2:])


class TestElGr:
    """Test el_GR bank provider"""
    def test_bban(self, randum, num_samples):
        for _ in range(num_samples):
            assert re.fullmatch(r"\d{23}", randum.bban())

    def test_iban(self, randum, num_samples):
        for _ in range(num_samples):
            iban = randum.iban()
            assert is_valid_iban(iban)
            assert iban[:2] == ElGrBankProvider.country_code
            assert re.fullmatch(r"\d{2}\d{23}", iban[2:])
