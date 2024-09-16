import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # Check out the docs:
    #   - https://docs.python.org/3/library/datetime.html#datetime.datetime.fromisoformat
    #   - https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime
    #   - https://strftime.org/     <- handy cheatsheet for representing datetime string formats

    return datetime.fromisoformat(iso_string).strftime("%A %d %B %Y")


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_celcius = 5*(float(temp_in_farenheit)-32)/9
    
    # Check out the docs:
    #   - https://docs.python.org/3/library/functions.html#round

    return round(temp_in_celcius, 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # We use a list comprehension to convert any non-floats from the input to floats.
    # There's a short discussion of this in the README, but here are the docs:
    #   - https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    #   - handy examples here: https://www.youtube.com/watch?v=AhSvKGTh28Q 

    data_points = [float(datapoint) for datapoint in weather_data]

    # now we can calculate the average
    return sum(data_points)/len(weather_data)

# -----------------------------------------------------------------------------
# It's possible to solve these next three in fewer lines with clever hacks.
# If you did it that way, that's fine too.
# I think the way I use here is quite readable, though, which is desirable.
# -----------------------------------------------------------------------------

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    # It's good practice to make sure that the file gets closed after we are done.
    # Otherwise another function might not be able to access it later.
    
    # The "with" statement in Python lets you define a variable to 
    # represent objects that need cleaning up when you're done. 
    # Here's a good writeup: https://realpython.com/python-with-statement/
    
    with open(csv_file, 'r') as file:
        my_reader = csv.reader(file, delimiter=',')
        
        # We want to throw the header away, so we pop it off with "next()"
        # https://docs.python.org/3/library/functions.html#next

        # This works because my_reader is an "iterator"
        # (a special type of object that returns a list of values one-by-one)
        #   - https://docs.python.org/3/glossary.html#term-iterator

        header = next(my_reader)

        # A list comprehension with a boolean condition!
        data_to_return = [
            [row[0], int(row[1]), int(row[2])] for row in my_reader if row
        ]

        return data_to_return

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """

    # If we got no data, there is no minimum value or position to return
    # In that case we return an empty tuple

    if not weather_data:
        return ()

    # Now we need to create variables to store our results, but we have to make
    # sure that they will be immediately replaced by the first item in the list,
    # no matter how high it is!

    # Since 0 is the lowest index, every index will come after "-1"!
    min_index = -1

    # It turns out we can create a float with a value of "infinity"
    # This is handy, because every number is smaller than infinity!
    min_value = float('infinity')

    # We use enumerate to get the index and value of each item in the list
    #   - https://docs.python.org/3/library/functions.html#enumerate
    for index, value in enumerate(weather_data):
        value = float(value)
        
        # If the value is smaller than our current min, we replace it!
        if value <= min_value:
            min_index = index
            min_value = value

    # Finally, we can return the results.
    return round(min_value, 1), min_index


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """

    # The logic for this function is exactly the same as find_min, except...
    #   - we use "negative infinity" as our starting max_value
    #   - we use greater-than-or-equal-to (">=") instead of less-than-or-equal-to ("<=")

    if not weather_data:
        return ()
    
    max_index = -1
    max_value = -float('infinity')

    for index, value in enumerate(weather_data):
        value = float(value)
        if value >= max_value:
            max_index = index
            max_value = value

    return round(max_value, 1), max_index


# -----------------------------------------------------------------------------
# It's possible to solve these next two a few different ways.
#   - You could use "+" to concatenate strings 
#   - You could use multi-line f-strings with triple quotes 
#
# I've chosen to add each line of the output to a list, and then use join()
# to concatenate the lists together. This is a common idiom in Python, and
# it keeps things easy to read. It's also very efficient for the computer.
# (not that that matters in a program this simple!)
# -----------------------------------------------------------------------------

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    
    # Three list comprehensions to convert our days and temps
    # See how we grab the first element of each row for the dates,
    # the second element of each row for the lows,
    # and the third element of each row for the highs?
    dates = [convert_date(day[0]) for day in weather_data]
    lows = [convert_f_to_c(day[1]) for day in weather_data]
    highs = [convert_f_to_c(day[2]) for day in weather_data]

    # Using the functions we built earlier!
    lowest, lowest_index = find_min(lows)
    highest, highest_index = find_max(highs)

    # We can get the lowest and highest days using the indices we just found
    lowest_day = dates[lowest_index]
    highest_day = dates[highest_index]

    # Using the functions we built earlier!
    # (Need to round to 1 decimal place!)
    mean_low = round(calculate_mean(lows), 1)
    mean_high = round(calculate_mean(highs), 1)


    # A list to store our results
    result_list = [
        f"{len(weather_data)} Day Overview",
        f"  The lowest temperature will be {format_temperature(lowest)}, and will occur on {lowest_day}.",
        f"  The highest temperature will be {format_temperature(highest)}, and will occur on {highest_day}.",
        f"  The average low this week is {format_temperature(mean_low)}.",
        f"  The average high this week is {format_temperature(mean_high)}.",
        "" # The test files end with an empty line!
    ]

    # Here we use the string.join() method to concatenate the items in the list.
    # Each concatenated line is separated by a newline character.
    #   - https://docs.python.org/3/library/stdtypes.html#str.join
    #   - https://www.freecodecamp.org/news/print-newline-in-python/

    return "\n".join(result_list)

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # We use the same list-building process as above
    result_list = []

    for day in weather_data:
        # Using the extend method to add multiple items to the list at once.
        #   - https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
        result_list.extend([
            f"---- {convert_date(day[0])} ----",
            f"  Minimum Temperature: {format_temperature(convert_f_to_c(day[1]))}",
            f"  Maximum Temperature: {format_temperature(convert_f_to_c(day[2]))}",
            ""
        ])

    # The test files end with TWO empty lines!
    result_list.append("")

    return "\n".join(result_list)
    
    
    

