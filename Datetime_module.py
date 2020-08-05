from datetime import datetime, timedelta, date, time
import pytz
def main():

    #printing current date and time
    print(datetime.now())

    #printing today's date
    print(date.today())

    #creating datetime object
    dt=datetime(2020,6,6,16,24,6,26)
    print("Datetime: ", dt)
    print("year: ", dt.year)
    print("Month: ", dt.month)
    print("Day: ", dt.day)
    print("Hour: ", dt.hour)

    #creating date object
    d=date(2020,6,6)
    print("Date: ", d)
    print("Year: ", d.year)
    print("Month: ", d.month)

    #creating time object
    t=time(16,24,6,26)
    print('Time: ', t)
    print('Hour: ', t.hour)

    #timestamp
    timestamp=datetime.fromtimestamp(1326244364)
    print(timestamp)

    #timedelta
    t1 = date(year=2018, month=7, day=12)
    t2 = date(year=2017, month=12, day=23)
    t3 = t1 - t2
    print("t3 =", t3)

    t4 = datetime(year=2018, month=7, day=12, hour=7, minute=9, second=33)
    t5 = datetime(year=2019, month=6, day=10, hour=5, minute=55, second=13)
    t6 = t4 - t5
    print("t6 =", t6)

    print("type of t3 =", type(t3))
    print("type of t6 =", type(t6))

    t1 = timedelta(weeks=2, days=5, hours=1, seconds=33)
    t2 = timedelta(days=4, hours=11, minutes=4, seconds=54)
    t3 = t1 - t2

    print("t3 =", t3)

    #formatting datetime
    now = datetime.now()

    t = now.strftime("%H:%M:%S")
    print("time:", t)

    s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
    print("s1:", s1)

    s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
    print("s2:", s2)

    #time from string
    date_string = "21 June, 2018"
    print("date_string =", date_string)

    date_object = datetime.strptime(date_string, "%d %B, %Y")
    print("date_object =", date_object)

    #timezone in python
    local = datetime.now()
    print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))

    tz_NY = pytz.timezone('America/New_York')
    datetime_NY = datetime.now(tz_NY)
    print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

    tz_London = pytz.timezone('Europe/London')
    datetime_London = datetime.now(tz_London)
    print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))


if __name__ == '__main__':
    main()
