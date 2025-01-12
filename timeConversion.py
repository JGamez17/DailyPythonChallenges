import __main__
# "07:05:45PM"
# add 12 hours to the hour if it's PM, and leave the hour the same if it's AM, except for 12 AM, which becomes 00:00.


def timeConversion(s):
    hour = int(s[:2])  # First two characters are the hour
    minute = s[3:5]    # Characters 3-4 are the minute
    second = s[6:8]    # Characters 6-7 are the second
    period = s[8:]

    if period == "AM":
        if hour == 12:
            hour += 12
    elif period == "AM":
        hour = 0

    return f"{hour:00}:{minute}:{second}"


if __name__ == __main__:
    s = input()
    result = timeConversion(s)
    print(result)
