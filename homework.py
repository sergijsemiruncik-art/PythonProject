from datetime import datetime

def get_days_from_today(date):
    '''
    calculates the number of days between a specified date and the current date.
    '''

        try:
        #Converting to date from string
            date = datetime.strptime(date, '%Y-%m-%d')
            concurrent_day = datetime.today()
            concurrent_day = concurrent_day.strftime("%d")
        #Calculating the difference in days
            delta_time = date.day - int(concurrent_day)
            return delta_time
        #Processing exceptions
        except ValueError:
            return 'Please enter a correct object'
        except TypeError:
            return 'Please enter a correct object'


#Завдання 2

from random import randint

def get_numbers_ticket(min, max, quantity):
    """"
    Generates a sorted list of unique random numbers.
    """
    #Verifying the correctness of parameters
    if quantity > max - min + 1:
        return []
    #Creating a set to fill it with unique numbers
    numbers = set()
    #Run the while loop until the number of elements in the set reaches the specified parameter
    while len(numbers) < quantity:
        numbers.add(randint(min, max))
    #Converting a set into a list and sorting it
    numbers = list(numbers)
    numbers.sort()
    return numbers


#Завдання 3
import re

def normalize_phone(phone_number):

    """
    Normalises the telephone number to the standard format.
    """

    # Remove all characters except numbers and '+'
    cleaned = re.sub(r"[^\d+]", "", phone_number)

    # If the number starts with “380” without “+”, adding '+'
    if cleaned.startswith("380"):
        cleaned = "+" + cleaned
    # If the number does not start with “+”, add '+38'
    elif not cleaned.startswith("+"):
        cleaned = "+38" + cleaned

    return cleaned


if __name__ == "__main__":
    print(get_days_from_today('2026-12-31'))
    print(get_days_from_today('2026-12-1'))
    print(get_days_from_today(2025 - 12 - 1))
    print(get_days_from_today('jnfhndujsj'))

    print(get_numbers_ticket(1, 1000, 12))

    print(normalize_phone('15017116'))


