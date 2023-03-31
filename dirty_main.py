from application.salary import *
from application.db.people import *
import datetime
from pdf_imag import *


now = datetime.datetime.now()


if __name__ == '__main__':
    print(now.strftime('%d-%m-%Y'))
    get_imag()
    calculate_salary()
    get_employees()
