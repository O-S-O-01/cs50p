import re

def main():
    s = input("Hours: ")
    result = convert(s)
    print(result)

def convert(s):

    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"

    match = re.search(pattern, s)

    if not match:
        raise ValueError("Invalid format")

    # Extract groups from the regex match
    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    # Convert start and end hours to integers    
    start_hour = int(start_hour)
    end_hour = int(end_hour)

    # Convert start minutes
    if start_minute:
        start_minute = int(start_minute)
    else:
        start_minute = 0

    # Convert end minutes
    if end_minute:
        end_minute = int(end_minute)
    else:
        end_minute = 0

    # Validate start time
    if valid_time(start_hour, start_minute) == False:
        raise ValueError("Invalid start time")

    # Validate end tim
    if valid_time(end_hour, end_minute) == False:
        raise ValueError("Invalid end time")

    # Convert both times to 24-hour format
    start_time = to_24_hour(start_hour, start_minute, start_period)
    end_time = to_24_hour(end_hour, end_minute, end_period)

    return f"{start_time} to {end_time}"


def valid_time(hour, minute):

    if 1 <= hour <= 12 and 0 <= minute <= 59:
        return True
    else:
        return False


def to_24_hour(hour, minute, period):

    # Handle AM times
    if period == "AM":

        if hour == 12:
            hour = 0

    # Handle PM times
    elif period == "PM":

        if hour != 12:
            hour = hour + 12

    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()