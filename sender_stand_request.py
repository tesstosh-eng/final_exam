# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data 

# Запрос на создание заказа.
# Определение функции create_order для отправки POST-запроса на создание нового заказа
def post_create_order(body):
    # Выполнение POST-запроса на создание заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body,
                         headers=data.headers)
    
# Выполняет запрос на получение заказа по трек-номеру.
# Определение функции для отправки GET-запроса получение номера заказа. С параметром track_number.
def get_order_by_track(track):
    # Выполнение GET-запроса на получение заказа
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK, 
                        headers=data.headers, 
                        params={"t": track})

# Функция для позитивной проверки
def positive_assert_order():
    # В переменную order_body сохраняется тело запроса на создание заказа
    order_body = data.order_body
    # В переменную create_response сохраняется результат запроса на создание заказа
    create_response = post_create_order(order_body)

    # Проверяется, что код ответа равен 200 или 201
    assert create_response.status_code in (200, 201), "Не удалось создать заказ"

    # Сохранение трек-номера
    track_number = create_response.json().get("track")
    print("Заказ создан, Номер трека:", track_number)

    # Проверяется, что трек-номер получен и не является пустым
    assert track_number, "Трек-номер не получен"

    # Получение заказа по трек-номеру
    get_response = get_order_by_track(track_number)

    # Проверка статуса ответа
    assert get_response.status_code == 200, "Заказ не найден"
    print("Тест успешно пройден. Код 200.")

if __name__ == "__main__":
    positive_assert_order()