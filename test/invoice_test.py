from nfeio.nfeio import NfeClient
from test import dictionaries
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        super(Test, self).setUp()

        self.nfeclient = NfeClient('ic73EBApwJgw0PDZhP3EaMvuQRmjBFBlxE2MiEz23dN05xATpbfS3jVl1UArw6ZhcYH',
                          '5cffdf168a319831844c11c8')

    def test_create_service_invoice(self):

        invoice_data = dictionaries.SERVICE_INVOICE_JSON
        newinvoice = self.nfeclient.create_service_invoice(invoice_data)

        assert newinvoice.status_code == 202

    def test_create_product_invoice(self):

        nfeclient = NfeClient('ic73EBApwJgw0PDZhP3EaMvuQRmjBFBlxE2MiEz23dN05xATpbfS3jVl1UArw6ZhcYH',
                              '07a17ab6197a446b8a2e2ffe1bc8b109')

        invoice_data = dictionaries.PRODUCT_INVOICE_JSON
        newinvoice = nfeclient.create_product_invoice(invoice_data)

        assert newinvoice.status_code == 200

    def tearDown(self):
        super(Test, self).tearDown()


if __name__ == '__main__':
    unittest.main()