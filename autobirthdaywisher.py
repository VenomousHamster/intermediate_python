import smtplib
import datetime as dt
import random
import pandas as pd

my_email = "ghostinthemachine41@gmail.com"
password = "kogbtrjsgdwguzbd"


today = (dt.datetime.now().month, dt.datetime.now().day)
file = pd.read_csv("birthdays.csv")

new_dict = {(data_row["month"],data_row["day"]):data_row for (index, data_row) in file.iterrows()}

if today in new_dict:
    with open(f"././letter_templates/letter_{random.randint(1,3)}.txt") as file:
            letter = file.read()
            new_letter = letter.replace("NAME", new_dict[today]["name"])
            birthday_letter = new_letter

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
         connection.starttls()
         connection.login(user=my_email, password=password)
         connection.sendmail(from_addr=my_email, to_addrs="ghostinthemachine12@outlook.com",
	                      msg=f"Subject:HAPPY BIRTHDAY!\n\n {birthday_letter}")
