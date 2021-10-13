from randum.providers.job import Provider as JobProvider
from randum.providers.job.de_DE import Provider as DeDeJobProvider
from randum.providers.job.el_GR import Provider as ElGrJobProvider
from randum.providers.job.fr_FR import Provider as FrFrJobProvider
from randum.providers.job.hu_HU import Provider as HuHuJobProvider
from randum.providers.job.hy_AM import Provider as HyAmJobProvider
from randum.providers.job.ja_JP import Provider as JaJpJobProvider
from randum.providers.job.ko_KR import Provider as KoKrJobProvider
from randum.providers.job.pt_BR import Provider as PtBrJobProvider
from randum.providers.job.pt_PT import Provider as PtPtJobProvider
from randum.providers.job.ro_RO import Provider as RoRoJobProvider
from randum.providers.job.sk_SK import Provider as SkSkJobProvider
from randum.providers.job.th_TH import Provider as ThThJobProvider
from randum.providers.job.tr_TR import Provider as TrTrJobProvider


class TestJobProvider:
    """Test job provider methods"""

    def test_job(self, randum, num_samples):
        for _ in range(num_samples):
            assert randum.job() in JobProvider.jobs


class TestJaJp:
    """Test ja_JP job provider"""

    def test_job(self, randum, num_samples):
        for _ in range(num_samples):
            assert randum.job() in JaJpJobProvider.jobs


class TestKoKr:
    """Test ko_KR job provider"""

    def test_job(self, randum, num_samples):
        for _ in range(num_samples):
            assert randum.job() in KoKrJobProvider.jobs


class TestHuHu:
    """Test hu_HU job provider"""

    def test_job(self, randum, num_samples):
        for _ in range(num_samples):
            assert randum.job() in HuHuJobProvider.jobs


class TestHyAm:
    """Test hy_AM job provider"""

    def test_job(self, randum, num_samples):
        for _ in range(num_samples):
            assert randum.job() in HyAmJobProvider.jobs


class TestDeDe:
    """Test de_DE job provider"""

    def test_job(self, randum, num_samples):
        for _ in range(num_samples):
            assert randum.job() in DeDeJobProvider.jobs


class TestFrFr:
    """Test fr_FR job provider"""

    def test_job(self, randum, num_samples):
        for _ in range(num_samples):
            assert randum.job() in FrFrJobProvider.jobs


class TestElGr:
    """Test el_GR job provider"""

    def test_job(self, randum, num_samples):
        for _ in range(num_samples):
            assert randum.job() in ElGrJobProvider.jobs


class TestPtPt:
    """Test pt_PT job provider"""

    def test_job(self, randum, num_samples):
        for _ in range(num_samples):
            assert randum.job() in PtPtJobProvider.jobs


class TestPtBr:
    """Test pt_BR job provider"""

    def test_job(self, randum, num_samples):
        for _ in range(num_samples):
            assert randum.job() in PtBrJobProvider.jobs


class TestSkSk:
    """Test sk_SK job provider"""

    def test_job(self, randum, num_samples):
        for _ in range(num_samples):
            job = randum.job()
            assert isinstance(job, str)
            assert job in SkSkJobProvider.jobs


class TestThTh:
    """Test th_TH job provider"""

    def test_job(self, randum, num_samples):
        assert randum.job() in ThThJobProvider.jobs


class TestTrTr:
    """Test tr_TR job provider"""

    def test_job(self, randum, num_samples):
        assert randum.job() in TrTrJobProvider.jobs


class TestRoRo:
    """Test tr_TR job provider"""

    def test_job(self, randum, num_samples):
        assert randum.job() in RoRoJobProvider.jobs
