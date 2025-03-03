import os
from bs4 import BeautifulSoup
import pandas as pd

def extract_jobs_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")
    job_data = []

    for job in soup.find_all("div", {"data-marker": "item"}):
        # Название вакансии
        title_tag = job.find("p", {"itemprop": "name"})
        title = title_tag.text.strip() if title_tag else None
        if not title:
            title_tag = job.find("a", {"data-marker": "item-title"})
            title = title_tag.text.strip() if title_tag else "Не указано"

        # Ссылка на вакансию
        link_tag = job.find("a", {"itemprop": "url"})
        link = f"https://www.avito.ru{link_tag['href']}" if link_tag else "Нет ссылки"

        # Описание вакансии
        description_meta = job.find("meta", {"itemprop": "description"})
        description = description_meta["content"] if description_meta else "Не указано"

        # Зарплата
        salary_meta = job.find("meta", {"itemprop": "price"})
        salary = salary_meta["content"] if salary_meta else "Не указано"

        # Валюта зарплаты
        currency_meta = job.find("meta", {"itemprop": "priceCurrency"})
        currency = currency_meta["content"] if currency_meta else "Не указано"

        # Условия (график работы, опыт)
        conditions_tag = job.find("p", {"data-marker": "item-specific-params"})
        conditions = conditions_tag.text.strip() if conditions_tag else "Не указано"

        # Местоположение
        location_tag = job.find("div", class_="geo-root-NrkbV")
        location = location_tag.text.strip() if location_tag else "Не указано"

        # Добавляем данные в список
        job_data.append({
            "Название вакансии": title,
            "Ссылка": link,
            "Описание": description,
            "Зарплата": salary,
            "Валюта": currency,
            "Условия": conditions,
            "Местоположение": location
        })

    return job_data

def extract_jobs_from_directory(directory_path):
    all_jobs = []

    # Перебираем файлы в директории
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Проверяем, что это файл (а не папка)
        if os.path.isfile(file_path) and file_path.endswith(".txt"):
            print(f"Обрабатываю файл: {filename}")
            jobs = extract_jobs_from_file(file_path)
            all_jobs.extend(jobs)

    # Создаём общий DataFrame
    df_jobs = pd.DataFrame(all_jobs)
    return df_jobs

# Укажите путь к вашей директории
directory_path = "/workspaces/GP-2/pages_a1"

# Извлекаем данные и сохраняем в DataFrame
df_all_vacancies = extract_jobs_from_directory(directory_path)

# Сохраняем результат в CSV
df_all_vacancies.to_csv("all_vacancies_avito.csv", index=False, encoding="utf-8")
