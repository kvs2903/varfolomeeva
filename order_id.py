import configuration
import requests
import data

# создание нового заказа
def post_new_order (body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)
response = post_new_order (data.order_body)


# сохраняем трек заказа в переменную
order_track = response.json()
headers_track = str(response.json()['track'])


def get_order_id():
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_ID_PATH + headers_track)
response = get_order_id()
print(response.status_code)
print(response.json())
