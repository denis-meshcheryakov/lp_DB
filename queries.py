from model_2 import Salary

def top_salary(num_rows):
    top_salary = Salary.query.order_by(Salary.salary.desc()).limit(num_rows)
    for s in top_salary:
        print(f'З/п: {s.salary}')

def salary_by_city(city_name):
    top_salary = Salary.query.filter(Salary.city == city_name).order_by(Salary.salary.desc())
    print(city_name)
    for s in top_salary:
        print(f'З/п: {s.salary}')

def top_salary_by_domain(domain, num_rows):
    top_salary = Salary.query.filter(Salary.email.ilike(f'%{domain}')).order_by(Salary.salary.desc()).limit(num_rows)
    print(domain)
    for s in top_salary:
        print(f'З/п: {s.salary}')

if __name__ =="__main__":
    # top_salary(5)
    # salary_by_city('Кимры')
    top_salary_by_domain('@yandex.ru', 5)
