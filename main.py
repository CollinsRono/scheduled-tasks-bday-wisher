##################### Normal Starting Project ######################
import os
from datetime import datetime
import pandas
import random
import smtplib

today = datetime.now()
today_tuple = (today.month, today.day)
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    filepath = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open (filepath) as letter_file:
        contents = letter_file.read()
        new_msg = contents.replace("[NAME]", f"{birthday_person["name"]}")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday\n\n {new_msg}")


