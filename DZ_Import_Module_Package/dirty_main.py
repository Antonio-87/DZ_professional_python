import datetime
from application.salary import *
from application.db.people import *

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    now = datetime.date.today()
    print(now)