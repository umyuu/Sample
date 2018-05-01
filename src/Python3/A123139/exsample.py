# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import time
#
import schedule


def job():
    nowDate = datetime.now()
    print(nowDate)


def entry():
    schedule.every(1).minutes.do(job)
    #schedule.every(15).minutes.do(job)
    return schedule.CancelJob


def main():
    run_date = datetime.now() + timedelta(minutes=1)
    schedule.every().day.at(run_date.strftime("%H:%M")).do(entry)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
