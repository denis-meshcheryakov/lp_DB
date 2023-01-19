import time

from db import db_session
from models import Company, Employee


def employees_by_company(company_name):
    company = Company.query.filter(Company.name == company_name).first()
    emmployee_list = []
    if company:
        for employee in Employee.query.filter(Employee.company_id == company.id):
            emmployee_list.append(f'{company.name} - {employee.name}')
    return emmployee_list


def employees_by_company_joined(company_name):
    query = db_session.query(Employee, Company).join(
        Company, Employee.company_id == Company.id
    ).filter(Company.name == company_name)
    emmployee_list = []
    for employee, company in query:
        emmployee_list.append(f'{company.name} - {employee.name}')
    return emmployee_list



if __name__ == "__main__":
    # start = time.perf_counter()
    # for _ in range(100):
    #     employees_by_company('Ростех')
    # print(f'employees_by_company: {time.perf_counter() - start}')
    
    start = time.perf_counter()
    for _ in range(100):
        employees_by_company_joined('Ростех')
    print(f'employees_by_company_joined: {time.perf_counter() - start}')
