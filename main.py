from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
from pdf_imag import get_imag

now = datetime.datetime.now()


if __name__ == '__main__':
    print(now.strftime('%d-%m-%Y'))
    get_imag()
    calculate_salary()
    get_employees()
