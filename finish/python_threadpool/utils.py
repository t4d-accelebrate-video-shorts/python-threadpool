""" utils module """

from datetime import timedelta, date
from collections.abc import Generator
import holidays


def business_days(start_date: date, end_date: date) -> Generator[
        date, None, None]:
    """ generate business days for a date range inclusive """

    us_holidays = holidays.UnitedStates()

    for num in range((end_date - start_date).days + 1):
        the_date = start_date + timedelta(days=num)
        if (the_date.weekday() < 5) and (the_date not in us_holidays):
            yield the_date
