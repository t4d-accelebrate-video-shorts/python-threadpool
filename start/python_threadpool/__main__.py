"""Main Module"""

import multiprocessing as mp
from datetime import datetime

from python_threadpool.rates_api import start_rates_api
from python_threadpool.get_rates import get_rates, get_rates_threadpool


def main() -> None:
    """Main Function"""

    rates_api_process = mp.Process(target=start_rates_api)
    rates_api_process.start()

    start_time = datetime.now()

    num_rates_requested = get_rates()
    # num_rates_requested = get_rates_threadpool()

    print(f"number of rates requested: {num_rates_requested}")
    print(f"execution time: {datetime.now() - start_time} seconds")

    rates_api_process.terminate()


if __name__ == '__main__':
    main()
