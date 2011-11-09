import random
import unittest
from quix.pay.transaction import *
from quix.pay.gateway.paymentsgateway import PaymentsGateway

class TestPaymentsGateway(unittest.TestCase):

    def setUp(self):
        pass

    def test_shuffle(self):
        check = Check("121000358", "26009593", account_type="C")
        pg = PaymentsGateway()
        pg.use_test_url = True
        pg.eft_credit("10.00", check, None)

if __name__ == '__main__':
    unittest.main()

