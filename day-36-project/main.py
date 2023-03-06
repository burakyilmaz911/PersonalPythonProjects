import requests
import smtplib

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = "5e39dec760f54d7699ac471cd29bb670"
STOCK_API_KEY = "LU4A52G6ZVAF4TWF"

STOCK_API_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&outputsize=compact&datatype=json&symbol=TSLA&apikey=LU4A52G6ZVAF4TWF'

FROM_EMAIL = "burakscode@gmail.com"
TO_EMAIL = "burakscode@yahoo.com"

news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

data_stock = requests.get(STOCK_API_URL)
data_stock_json = data_stock.json()["Time Series (Daily)"]

data_news = requests.get(NEWS_ENDPOINT, params=news_params)
data_news_json = data_news.json()["articles"]
three_articles = data_news_json[:3]
formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
formatted_articles_encoded = [n.encode('utf-8') for n in formatted_articles]
print(formatted_articles_encoded)

data_stock_list = [value for (key, value) in data_stock_json.items()]

yesterdays_close = float(data_stock_list[0]["4. close"])
two_days_ago_close = float(data_stock_list[1]["4. close"])

diff_between_days = abs(yesterdays_close - two_days_ago_close)
avg = (yesterdays_close + two_days_ago_close) / 2
diff_between_days_percentage = (diff_between_days / avg) * 100

diff_between_days_percentage = 6

if diff_between_days_percentage > 5:
    response = smtplib.SMTP("smtp.gmail.com", port=587)
    response.starttls()
    response.login(user=FROM_EMAIL, password="zegzkfrpvrhwgmnv")
    response.sendmail(from_addr=FROM_EMAIL, to_addrs=TO_EMAIL, msg=f"Subject: Alert\n\n{formatted_articles_encoded}")

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

# TODO 2. - Get the day before yesterday's closing stock price

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
