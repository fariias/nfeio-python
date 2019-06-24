import json

import requests

from nfeio import endpoints


class NfeClient(object):
    def __init__(self, api_key, company_id, proxies={}):

        self.api_key = api_key
        self.company_id = company_id
        self.proxies = proxies

    def fetch_json(self,
            endpoint,
            http_method="GET",
            headers={},
            query_params={},
            post_args={},
            files=None,
    ):

        data = None
        if files is None:
            data = json.dumps(post_args)

        # if http_method in ("POST", "PUT", "DELETE") and not files:
        # headers['Content-Type'] = 'application/json; charset=utf-8'

        headers = {"authorization": self.api_key}

        response = requests.request(
            http_method,
            endpoint,
            headers=headers,
            json=post_args,
        )

        if response.status_code == 401:
            return f"Unauthorized: {response.text} - {endpoint} - {response}"

        return response

    #########################
    # SERVICE INVOICE
    #########################

    def create_service_invoice(self, invoice_data):

        endpoint = endpoints.SERVICE_INVOICE.format(self.company_id)

        new_invoice = self.fetch_json(endpoint, "POST", post_args=invoice_data)

        return new_invoice

    def create_product_invoice(self, invoice_data):
        endpoint = endpoints.PRODUCT_INVOICE.format(self.company_id)

        new_invoice = self.fetch_json(endpoint, "POST", post_args=invoice_data)

        return new_invoice