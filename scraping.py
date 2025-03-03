
import requests
import os
import time

download_path = os.path.expanduser("~/Downloads/pages_a1")
os.makedirs(download_path, exist_ok=True)

for p in range(1, 101):
    url = f"https://www.avito.ru/all/vakansii/chastichnaya_zanyatost-ASgBAgICAUSkgxXk2oUV?cd=1&p={p}"
    response = requests.get(url)
    if response.status_code == 200:
        path = os.path.join(download_path, f"chastichnaya_zanyatost_{p}.txt")
        with open(path, 'w', encoding="utf-8") as f:
            f.write(response.text)
        print(f"chastichnaya_zanyatost_{p}")
        time.sleep(40)
    else:
        print("Не удалось обработать файл")
        time.sleep(40)
