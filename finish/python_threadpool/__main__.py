"""Main Module"""

from datetime import datetime

from python_threadpool.rates_api_server import rates_api_server
from python_threadpool.get_rates import get_rates, get_rates_threadpool


def main() -> None:
    """Main Function"""

    with rates_api_server():

        print("processing rate requests")

        start_time = datetime.now()

        # rates = get_rates()
        rates = get_rates_threadpool()

        print("Rates")
        print("\n".join(rates))

        print(f"\nnumber of rates requested: {len(rates)}")
        print(f"execution time: {datetime.now() - start_time} seconds")


if __name__ == '__main__':
    main()
