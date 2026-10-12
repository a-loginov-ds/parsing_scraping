import curl_cffi
import math
from datetime import datetime, timezone
import random
import vk_api

lat_min, lat_max = 53.17, 53.3
lon_min, lon_max = 50.05, 50.35
zoom = 16
USER_ID = 856651602
TOKEN = "vk1.a.wLdfexOUjVniS7Yinq8dvoK5Doja1mE_6DHykloRfwjTjeo2Y1RY20DYAgjGyhtqonKzRSalm2Nw-tJIRm_4VpLqqFbgvxWVPyFBuG8mdep5EXsuSEkHa1rQJ9M0AR8XBvef4P3engcXKRqqvzcDMhDsX7cOerjRxnqCT7TubLULD3tqm8ohJYQ5HAaBLMoQbxhX-remX_z4IxVTWhq8DA"


def send_vk_notification(token, user_id, message):
    try:
        vk_session = vk_api.VkApi(token=token)
        vk = vk_session.get_api()

        vk.messages.send(
            peer_id=user_id,
            message=message,
            random_id=random.randint(1, 2147483647),
        )
        print("Уведомление успешно отправлено!")

    except vk_api.exceptions.ApiError as error:
        print(f"Ошибка VK API: {error}")


def deg2num_yandex(lat, lon, zoom):
    a = 6378137.0
    b = 6356752.3142
    e = math.sqrt(1 - (b / a) ** 2)
    n = 2**zoom
    x = int((lon + 180) / 360 * n)
    lat_rad = math.radians(lat)
    y_m = a * math.log(
        math.tan(math.pi / 4 + lat_rad / 2)
        * ((1 - e * math.sin(lat_rad)) / (1 + e * math.sin(lat_rad))) ** (e / 2)
    )
    max_merc = a * math.pi
    y = int((max_merc - y_m) * n / (2 * max_merc))
    return x, y


x_min, y_max = deg2num_yandex(lat_min, lon_min, zoom)
x_max, y_min = deg2num_yandex(lat_max, lon_max, zoom)


base_url = "https://core-road-events-renderer.maps.yandex.net/1.1/tiles"
for x in range(x_min, x_max + 1):
    for y in range(y_min, y_max + 1):

        params = {
            "trf": "1",
            "l": "trje",
            "lang": "ru",
            "x": str(x),
            "y": str(y),
            "z": str(zoom),
            "scale": "1",
            "format": "json",
            "v": datetime.now(timezone.utc).strftime("%Y.%m.%d.%H.%M.00"),
        }

        resp = curl_cffi.get(url=base_url, params=params)
        if "ДТП" in resp.text:
            print('Fi')
            send_vk_notification(TOKEN, USER_ID, resp.text)
