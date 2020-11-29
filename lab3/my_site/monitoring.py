import requests
import json
import logging
import time

logging.basicConfig(
#     filename="server.log",
#     filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def main(url):
    r = requests.get(url)
    if r.status_code != 200:
        logger.error(f'Сервіс не доступний. Статус код: {r.status_code}')

    data = json.loads(r.content)
    logger.info("Сервер доступний. Час на сервері: %s", data['date'])
    logger.info("Запитувана сторінка: : %s", data['current_page'])
    logger.info("Відповідь сервера місти наступні поля:")
    for key in data.keys():
        logger.info("Ключ: %s, Значення: %s", key, data[key])


if __name__ == '__main__':
    delay_secs = 60
    while True:
        main("http://localhost:8000/health/")  
        time.sleep(delay_secs)
    