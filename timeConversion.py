import __main__
# "07:05:45PM"
# add 12 hours to the hour if it's PM, and leave the hour the same if it's AM, except for 12 AM, which becomes 00:00.


def timeConversion(s):
    hour = int(s[:2])  # First two characters are the hour
    minute = s[3:5]    # Characters 3-4 are the minute
    second = s[6:8]    # Characters 6-7 are the second
    period = s[8:]     # Characters 8 onwards are AM/PM

    if period == "PM":
        if hour != 12:
            hour += 12
    elif period == "AM":
        if hour == 12:
            hour = 0

    return f"{hour:02}:{minute}:{second}"


if __name__ == "__main__":
    s = input("Enter time in 12-hour format (e.g., 07:05:45PM): ")
    result = timeConversion(s)
    print("Converted time in 24-hour format:", result)
