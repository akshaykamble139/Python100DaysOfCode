##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import smtplib
import datetime as dt
import random
import pandas


my_email = "testingpython4email@gmail.com"
password = "mzwv ozvf tncr apwf"

now = dt.datetime.now()
day = now.day
month = now.month

letter_name = f"./letter_templates/letter_{random.randint(1,3)}.txt"

data = pandas.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")
for dict in birthdays:
    if day == dict["day"] and month == dict["month"]:
        name = dict["name"]
        to_email = dict["email"]
        with open(letter_name) as file:
            message = file.read().replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email,password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f"Subject:Happy Birthday!\n\n{message}"
            )
            print(f"Email sent to {name}")



