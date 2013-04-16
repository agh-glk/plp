# coding=utf-8
import unittest
from plp import PLP


class PLPTestCase(unittest.TestCase):
    def setUp(self):
        self.plp = PLP('/usr/local/clp/lib/libclp_2.6.so')

    def test_ver(self):
        self.assertIsInstance(self.plp.ver() , unicode)

    def test_rec(self):
        self.assertEqual(self.plp.rec(u'żółwiem'), [18660912])

    def test_orec(self):
        self.assertEqual(self.plp.rec(u'zolwiem'), [])
        self.assertEqual(self.plp.orec(u'zolwiem'), [18660912])

    def test_bform(self):
        self.assertEqual(self.plp.bform(18660912), u'żółw')

    def test_label(self):
        self.assertEqual(self.plp.label(18660912)[0], PLP.CZESCI_MOWY.RZECZOWNIK)
        self.assertEqual(self.plp.label(self.plp.rec(u'idę')[0])[0], PLP.CZESCI_MOWY.CZASOWNIK)

    def test_ogonkify(self):
        self.assertItemsEqual(self.plp.ogonkify(u'gzo'), [u'gzó', u'gżo', u'gźo', u'gźó', u'gżó'])

    def test_forms(self):
        self.assertEqual(self.plp.forms(17786048), [
            u'pogoda',
            u'pogody',
            u'pogodzie',
            u'pogodę',
            u'pogodą',
            u'pogodo',
            u'pogód',
            u'pogodom',
            u'pogodami',
            u'pogodach'
        ])

    def test_vec(self):
        self.assertEqual(self.plp.vec(18660912, u'żółwiem')[0], 5)

if __name__ == '__main__':
    unittest.main()