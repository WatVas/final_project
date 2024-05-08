import configuration
import requests


def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=body)


def get_order(track_id):
    get_order_url = f'{configuration.URL_SERVICE}/api/v1/orders/track?t={track_id}'
    response = requests.get(get_order_url)
    return response
