import csv
from datetime import date, timedelta, datetime


def get_all_data_from_report(list_reports):
    list_all_date = []
    for line in list_reports:
        if line["Report Date"] not in list_all_date:
            list_all_date.append(line["Report Date"])

    return list_all_date


def get_list_finance_mouth():
    current_mounth = int(datetime.now().strftime("%m"))
    current_mounth = 9
    if current_mounth == 7:
        start_day = date(2019, 6, 30)
        end_day = date(2019, 7, 27)
    if current_mounth == 8:
        start_day = date(2019, 7, 28)
        end_day = date(2019, 8, 24)
    if current_mounth == 9:
        start_day = date(2019, 8, 25)
        end_day = date(2019, 9, 28)
    if current_mounth == 10:
        start_day = date(2019, 9, 29)
        end_day = date(2019, 10, 26)
    if current_mounth == 11:
        start_day = date(2019, 10, 27)
        end_day = date(2019, 11, 23)
    if current_mounth == 12:
        start_day = date(2019, 11, 24)
        end_day = date(2019, 12, 28)
    if current_mounth == 1:
        start_day = date(2019, 12, 29)
        end_day = date(2020, 1, 25)
    number_days = end_day - start_day
    list_finance_mouth = []
    for one_day in range(number_days.days + 1):
        day = start_day + timedelta(days=one_day)
        list_finance_mouth.append(day.strftime("%-m/%-d/%Y"))

    return list_finance_mouth


def validate_date(list_all_date_from_report):
    list_finance_mouth = get_list_finance_mouth()

    list_date_without_reports = []

    for one_day_finance_mouth in list_finance_mouth:
        if f'{one_day_finance_mouth} 12:00:00 AM' not in list_all_date_from_report:
            list_date_without_reports.append(one_day_finance_mouth)

    return list_date_without_reports


def get_list_reports(csv_file):
    list_all_reports = []
    with open(csv_file) as file_obj:
        reader = csv.DictReader(file_obj, delimiter=',')
        for line in reader:
            list_all_reports.append(line)

    return list_all_reports


def validate_cost_in_reports(list_all_reports):
    current_date = Net_Sale_USD = Net_Sale_LC = COGS_USD = COGS_LC = Count_of_Customer_Order_Number = 0
    for line in list_all_reports:
        if current_date == line["Report Date"]:
            Net_Sale_USD += line["Net Sales USD"]
            Net_Sale_LC += line["Net Sales LC"]
            COGS_USD += line["COGS USD"]
            COGS_LC += line["COGS LC"]
            Count_of_Customer_Order_Number += line["Count of Customer Order Number"]
        else:
            if Net_Sale_USD == 0 and Net_Sale_LC == 0 and COGS_USD == 0 and COGS_LC == 0 and Count_of_Customer_Order_Number == 0:
                print(line)

            current_date = line["Report Date"]
            Net_Sale_USD = Net_Sale_LC = COGS_USD = COGS_LC = Count_of_Customer_Order_Number = 0

            Net_Sale_USD += line["Net Sales USD"]
            Net_Sale_LC += line["Net Sales LC"]
            COGS_USD += line["COGS USD"]
            COGS_LC += line["COGS LC"]
            Count_of_Customer_Order_Number += line["Count of Customer Order Number"]
    print('New line')


if __name__ == "__main__":
    csv_file = 'Revenue_Details_FM_CA_2019FM09.csv'
    list_all_reports = get_list_reports(csv_file)
    list_all_data = get_all_data_from_report(list_all_reports)
    validate_date(list_all_data)
    validate_cost_in_reports(list_all_reports)
