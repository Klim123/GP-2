import requests
import os
import time

os.makedirs(r"C:\Users\dzebo\Downloads\pages_a1", exist_ok = True)

for p in range(1, 101):
    url = f"https://www.avito.ru/all/vakansii/polnaya_zanyatost-ASgBAgICAUSkgxWS2YUV?cd=1&p={p}"
    response = requests.get(url)
    if response.status_code == 200:
        path = os.path.join(r"C:\Users\dzebo\Downloads\pages_a1", f"polnaya_zanyatost_{p}.txt")
        f = open(path, 'w', encoding = "utf-8")
        f.write(response.text)
        f.close()
        print(f"polnaya_zanyatost_{p}")
        time.sleep(40)
    else:
        print("Не удалось обработать файл")
        time.sleep(40)


for p in range(1, 101):
    url = f"https://www.avito.ru/all/vakansii/chastichnaya_zanyatost-ASgBAgICAUSkgxXk2oUV?cd=1&p={p}"
    response = requests.get(url)
    if response.status_code == 200:
        path = os.path.join(r"C:\Users\dzebo\Downloads\pages_a1", f"chastichnaya_zanyatost_{p}.txt")
        f = open(path, 'w', encoding = "utf-8")
        f.write(response.text)
        f.close()
        print(f"chastichnaya_zanyatost_{p}")
        time.sleep(40)
    else:
        print("Не удалось обработать файл")
        time.sleep(40)


for p in range(1, 101):
    url = f"https://www.avito.ru/all/vakansii/vremennaya-ASgBAgICAUSkgxXw2oUV?cd=1&p={p}"
    response = requests.get(url)
    if response.status_code == 200:
        path = os.path.join(r"C:\Users\dzebo\Downloads\pages_a1", f"vremennaya_{p}.txt")
        f = open(path, 'w', encoding = "utf-8")
        f.write(response.text)
        f.close()
        print(f"vremennaya_{p}")
        time.sleep(40)
    else:
        print("Не удалось обработать файл")
        time.sleep(40)
