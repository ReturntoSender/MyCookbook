import constants as c
from helpers import *

# Triggering the entire project
# Do this by python run.py


def run():
    primes = calculate_primes(start=c.START, finish=c.FINISH)
    print(primes)


if __name__ == "__main__":
    run()
