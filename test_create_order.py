# Юрий Шестаков, 16-я когорта — Финальный проект. Инженер по тестированию плюс
import data
from sendor_stand_request import create_order, get_order


def test_create_order_positive_check():
    response = create_order(data.body_json)
    track_id = response.json()['track']
    response_get_order = get_order(track_id)
    assert response_get_order.status_code == 200, f'Произошла ошибка {response_get_order.status_code}'