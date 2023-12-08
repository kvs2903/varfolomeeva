import configuration
import requests
import data

# создание нового заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body)


# сохраняем трек заказа
def get_order_track():
    order_track = post_new_order().json()['track']
    return order_track


# получаем информацию о заказе
def get_order_id():
    track = {"t":get_order_track()}
    response = requests.get(configuration.URL_SERVICE + configuration.ORDER_ID_PATH, params=track)
    return response




