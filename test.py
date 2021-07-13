import pytz
from datetime import datetime

if __name__ == '__main__':
    print(pytz.timezone('Asia/Tashkent'))
    print(datetime.now().date())
    print(datetime.now(tz=pytz.utc).date())
    print(datetime.now(tz=pytz.utc).date() < datetime.now().date())
