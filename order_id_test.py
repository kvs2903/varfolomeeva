
# Катя Варфоломеева — Финальный проект. Инженер по тестированию плюс

import order_id

# проверка получения id заказа по треку
def test_success_order_id():
    response = order_id.get_order_id()
    assert response.status_code == 200

