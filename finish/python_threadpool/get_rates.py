""" get rates modules """

from concurrent.futures import ThreadPoolExecutor
from datetime import date
import json
import requests
from python_threadpool.utils import business_days


def get_rates() -> list[str]:
    """ get rates """

    start_date = date(2021, 1, 1)
    end_date = date(2021, 3, 31)
    rates: list[str] = []

    for business_day in business_days(start_date, end_date):
        rates_url = "".join(["http://localhost:5000/api/",
                             business_day.strftime("%Y-%m-%d"),
                             "?base=USD&symbols=EUR"])

        response = requests.request("GET", rates_url)
        daily_rate = json.loads(response.text)

        rates.append(": ".join([daily_rate["date"],
                                str(daily_rate["rates"]["EUR"])]))

    return rates


def get_rate_task(business_day: date) -> str:
    """ get rate task """

    rates_url = "".join(["http://localhost:5000/api/",
                        business_day.strftime("%Y-%m-%d"),
                        "?base=USD&symbols=EUR"])

    response = requests.request("GET", rates_url)
    daily_rate = json.loads(response.text)

    return ": ".join([daily_rate["date"],
                      str(daily_rate["rates"]["EUR"])])


def get_rates_threadpool() -> list[str]:
    """ get rates threadpool """

    start_date = date(2021, 1, 1)
    end_date = date(2021, 3, 31)

    with ThreadPoolExecutor() as executor:

        return list(executor.map(
            get_rate_task,
            [business_day for business_day in business_days(
                start_date, end_date)]))
