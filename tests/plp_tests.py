# coding=utf-8
import unittest
from plp import PLP


class PLPTestCase(unittest.TestCase):
    def setUp(self):
        self.plp = PLP()

    def test_ver(self):
        self.assertIsInstance(self.plp.ver(), str)

    def test_rec(self):
        self.assertEqual(self.plp.rec('żółwiem'), [18660912])

    def test_orec(self):
        self.assertEqual(self.plp.rec('zolwiem'), [])
        self.assertEqual(self.plp.orec('zolwiem'), [18660912])

    def test_bform(self):
        self.assertEqual(self.plp.bform(18660912), 'żółw')

    def test_label(self):
        self.assertEqual(self.plp.label(18660912)[0], PLP.CZESCI_MOWY.RZECZOWNIK)
        self.assertEqual(self.plp.label(self.plp.rec('idę')[0])[0], PLP.CZESCI_MOWY.CZASOWNIK)

    def test_ogonkify(self):
        self.assertCountEqual(self.plp.ogonkify('gzo'), ['gzó', 'gżo', 'gźo', 'gźó', 'gżó'])

    def test_forms(self):
        self.assertEqual(self.plp.forms(17786048), [
            'pogoda',
            'pogody',
            'pogodzie',
            'pogodę',
            'pogodą',
            'pogodo',
            'pogód',
            'pogodom',
            'pogodami',
            'pogodach'
        ])

    def test_vec(self):
        self.assertEqual(self.plp.vec(18660912, 'żółwiem')[0], 5)

if __name__ == '__main__':
    unittest.main()