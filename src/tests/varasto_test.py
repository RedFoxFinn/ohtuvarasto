import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

class TestVarasto2(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(-1,-2)

    def test_varasto_on_tyhja(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 0)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varastoa_ei_voi_tayttaa(self):
        self.varasto.lisaa_varastoon(2)
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)
        self.assertEqual(self.varasto.__str__(),'saldo = 0.0, vielä tilaa 0.0')

    def test_varastosta_ei_voi_ottaa(self):
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

class TestVarasto3(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(20,18)

    def test_varasto_on_alustettu_annetuilla_arvoilla(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 20)
        self.assertAlmostEqual(self.varasto.saldo, 18)

    def test_varaston_lisays_ja_vahennys(self):
        self.varasto.lisaa_varastoon(2)
        self.assertAlmostEqual(self.varasto.saldo, 20)
        self.varasto.ota_varastosta(5)
        self.assertAlmostEqual(self.varasto.saldo, 15)
        self.assertEqual(self.varasto.__str__(), 'saldo = 15, vielä tilaa 5')

    def test_lisaa_varastoon_negatiivinen(self):
        self.varasto.lisaa_varastoon(-2)
        self.assertAlmostEqual(self.varasto.saldo, 18)

    def test_ota_varastosta_negatiivinen_arvo(self):
        self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(self.varasto.saldo, 18)

class TestVarasto4(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(20,50)

    def test_varasto_on_alustettu_tayteen(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 20)
        self.assertAlmostEqual(self.varasto.saldo, 20)

    def test_varastoon_ei_voi_lisata(self):
        self.varasto.lisaa_varastoon(5)
        self.assertAlmostEqual(self.varasto.saldo, 20)

    def test_lisaa_varastoon_negatiivinen(self):
        self.varasto.lisaa_varastoon(-2)
        self.assertAlmostEqual(self.varasto.saldo, 20)

    def test_ota_varastosta_negatiivinen_arvo(self):
        self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(self.varasto.saldo, 20)

    def test_varastosta_voi_vahentaa(self):
        self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(self.varasto.saldo, 10)
        self.assertEqual(self.varasto.__str__(), 'saldo = 10, vielä tilaa 10')