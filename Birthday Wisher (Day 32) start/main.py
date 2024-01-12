import smtplib
import datetime as dt
import random

quotes_list = []
with open("quotes.txt") as file:
    quotes_list += file.readlines()


now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 4:
    message = random.choice(quotes_list)

    my_email = "testingpython4email@gmail.com"
    password = "mzwv ozvf tncr apwf"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="testingpython4email@yahoo.com",
            msg=f"Subject:Hello\n\n{message}"
        )


# now = dt.datetime.now()
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1999,month=12, day=2)
# print(date_of_birth)

