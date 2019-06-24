import json

import requests


def post(endpoint, token,  data={}):
    headers = {'authorization': f'Authorization: {token}'}

    response = requests.post(endpoint, json=data, headers=headers)

    return response


def get(endpoint, token, data={}):
    headers = {'authorization': f'Authorization: {token}'}

    response = requests.get(endpoint, headers=headers)

    return response
