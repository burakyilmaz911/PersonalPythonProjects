import smtplib
import datetime as dt
import random

my_email = "burakscode@gmail.com"
password = "btvarqlrwabehoxp"

file = open("quotes.txt", "r")
list_quotes = file.readlines()
random_quote = random.choice(list_quotes)
file.close()

date = dt.datetime.now()
day_week = date.weekday()

if day_week == 0:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="burakscode@yahoo.com",
                        msg=f"Subject:Quote of the Day\n\n{random_quote}")
    connection.close()

