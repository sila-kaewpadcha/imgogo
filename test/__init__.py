from django.test import TestCase
from imapp.views import cal_impower

class BaseTestCase(TestCase):
    def setUp(self):
        "set up"
    
    def test_cal_impower_case1(self):
        num = 1
        res = cal_impower(num)
        self.assertEqual(res, ["1"])

    def test_cal_impower_case2(self):
        num = 3
        res = cal_impower(num)
        self.assertEqual(res, ["1", "2", "IM"])
    
    def test_cal_impower_case3(self):
        num = 5
        res = cal_impower(num)
        self.assertEqual(res, ["1", "2", "IM", "4", "IMPOWER"])
        
    def test_cal_impower_case4(self):
        num = 15
        res = cal_impower(num)
        self.assertEqual(res, ["1", "2", "IM", "4", "IMPOWER", "IM", "7", "8", "IM", "IMPOWER", "11", "IM", "13", "14", "IM IMPOWER"])
