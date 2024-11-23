'''
Необходимо реализовать скрипт, который будет получать с русскоязычной википедии список всех животных
(https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту) и записывать в файл в формате beasts.csv количество
животных на каждую букву алфавита.

Содержимое результирующего файла:
А,642
Б,412
В,....

Примечание:
анализ текста производить не нужно, считается любая запись из категории (в ней может быть не только название, но и,
например, род)
'''


import requests
from bs4 import BeautifulSoup
import csv

url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"


def get_animal_counts(url):
    animal_counts = {}
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        for link in soup.select('.mw-category-group ul li a'):
            animal_name = link.text
            if animal_name:
                first_letter = animal_name[0].upper()
                if 'А' <= first_letter <= 'Я':
                    animal_counts[first_letter] = animal_counts.get(first_letter, 0) + 1

        next_page = soup.find('a', text='Следующая страница')
        url = 'https://ru.wikipedia.org' + next_page['href'] if next_page else None

    return animal_counts


def write_to_csv(animal_counts, filename='beasts.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Буква', 'Счёт'])
        for letter, count in sorted(animal_counts.items()):
            writer.writerow([letter, count])


if __name__ == "__main__":
    animal_counts = get_animal_counts(url)
    write_to_csv(animal_counts)
