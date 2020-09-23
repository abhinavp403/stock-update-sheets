# https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
import finance
import manufacturing
import healthcare
import consumergoods
import datetime
from datetime import datetime
import calendar
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import finnhub

def main():
    # Setup client
    finnhub_client = finnhub.Client(api_key="btcplnn48v6svpql9uo0")

    # Create a client to interact with the Google Drive API
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/Abhinav/PycharmProjects/stock_api/credentials.json', scope)
    client = gspread.authorize(creds)

    # Current date time in local system
    d = str(datetime.date(datetime.now())).split("-")
    date = d[2] + " " + d[1] + " " + d[0]

    # day of the week
    born = datetime.strptime(date, '%d %m %Y').weekday()
    day = calendar.day_name[born]

    if day == "Monday":
        categories(3, 1, client, finnhub_client)
    if day == "Tuesday":
        categories(10, 1, client, finnhub_client)
    if day == "Wednesday":
        categories(17, 1, client, finnhub_client)
    if day == "Thursday":
        categories(3, 7, client, finnhub_client)
    if day == "Friday":
        categories(10, 7, client, finnhub_client)


def categories(row, column, client, finnhub_client):
    finance.updatedaily(row, column, client, finnhub_client)
    manufacturing.updatedaily(row, column, client, finnhub_client)
    consumergoods.updatedaily(row, column, client, finnhub_client)
    healthcare.updatedaily(row, column, client, finnhub_client)


main()
