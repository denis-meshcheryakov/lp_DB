from datetime import date
import time

from sqlalchemy.orm import joinedload

from models import Employee, Payment

def employees_and_payments():
    employee_list = []
    for paymet in Payment.query.filter(Payment.payment_date > date(2023, 6 ,11)):
        employee_list.append(
            f'{paymet.employee.company.name} - {paymet.employee.name} - {paymet.ammount}'
        )
    return employee_list


def employees_and_payments_joined():
    employee_list = []
    query = Payment.query.options(
        joinedload(Payment.employee).joinedload(Employee.company)
    ).filter(Payment.payment_date > date(2023, 6 ,11))
    for paymet in query:
        employee_list.append(
            f'{paymet.employee.company.name} - {paymet.employee.name} - {paymet.ammount}'
        )
    return employee_list



if __name__ == "__main__":
    # start = time.perf_counter()
    # for _ in range(10):
    #     employees_and_payments()
    # print(f'employees_and_payments: {time.perf_counter() - start}')
    
    start = time.perf_counter()
    for _ in range(10):
        employees_and_payments_joined()
    print(f'employees_and_payments_joined: {time.perf_counter() - start}')
