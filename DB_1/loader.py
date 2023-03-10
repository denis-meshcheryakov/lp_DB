import csv
import time

from db_2.db import db_session
from model_2 import Salary

def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['name', 'city_name', 'street_address',
                  'large_company', 'job', 'phone_number',
                  'free_email', 'date_of_birth', 'salary']
        reader = csv.DictReader(f, fields, delimiter=';')
        for row in reader:
            save_salary_data(row)


def save_salary_data(row):
    salary = Salary(name=row['name'], city=row['city_name'],
                    address=row['street_address'],
                    company=row['large_company'], job=row['job'],
                    phone_number=row['phone_number'],
                    email=row['free_email'],
                    date_of_birth=row['date_of_birth'],
                    salary=row['salary'])
    db_session.add(salary)
    db_session.commit()


def read_csv2(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['name', 'city', 'address',
                  'company', 'job', 'phone_number',
                  'email', 'date_of_birth', 'salary']
        reader = csv.DictReader(f, fields, delimiter=';')
        salary_data = []
        for row in reader:
            salary_data.append(row)
        save_salary_data2(salary_data)


def save_salary_data2(data):
    db_session.bulk_insert_mappings(Salary, data)
    db_session.commit()

if __name__ == "__main__":
    # start = time.time()
    # read_csv('salary.csv')
    # print(f'Загрузка1 заняла {time.time() - start} сек.')

    start = time.time()
    read_csv2('salary.csv')
    print(f'Загрузка2 заняла {time.time() - start} сек.')
