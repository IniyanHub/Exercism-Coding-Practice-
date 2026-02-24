"""Module for currency exchange calculations."""

def exchange_money(budget, exchange_rate):
    """Calculate the value of the exchanged currency.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - amount of domestic currency equal to one unit of foreign currency.
    :return: float - exchanged currency value.
    """
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """Calculate the amount of money left from the budget.

    :param budget: float - amount of money before exchange.
    :param exchanging_value: float - amount of money that is taken from the budget.
    :return: float - amount left.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """Calculate the total value of bills.

    :param denomination: int - value of a single bill.
    :param number_of_bills: int - total number of bills.
    :return: int - total value of the bills.
    """
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """Calculate the number of currency bills you can receive.

    :param amount: float - starting amount.
    :param denomination: int - value of a single bill.
    :return: int - number of whole bills.
    """
    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    """Calculate the leftover amount that cannot be exchanged.

    :param amount: float - starting amount.
    :param denomination: int - value of a single bill.
    :return: float - leftover amount.
    """
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculate the maximum value of new currency after fees and denomination restriction.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - amount of domestic currency equal to one unit of foreign currency.
    :param spread: int - percentage taken as an exchange fee.
    :param denomination: int - value of a single bill of the new currency.
    :return: int - maximum value of the new currency.
    """
    # Calculate the effective exchange rate with the spread
    # Spread is a percentage, e.g., 10 means 10%
    adjusted_exchange_rate = exchange_rate * (1 + (spread / 100))

    # Calculate the maximum amount of foreign currency obtainable
    max_foreign = budget / adjusted_exchange_rate

    # Calculate how many whole bills fit into this amount
    number_of_bills = int(max_foreign // denomination)

    # Return the total value of these bills
    return number_of_bills * denomination