import csv
import datetime
import os
import warnings
from argparse import ArgumentParser, ArgumentTypeError
from collections import Counter


def formatDateInput(input):
    return datetime.datetime.strptime(input, '%Y-%m-%d').replace(tzinfo=datetime.timezone.utc)


def checkFileInput(input):
    _, ext = os.path.splitext(input)
    if ext.lower() != '.csv':
        raise ArgumentTypeError("File must have CSV extension")
    if not os.path.exists(input):
        raise ArgumentTypeError("File must exist")
    return input


def parseArgs(args):
    parser = ArgumentParser(prog='most_active_cookie',
                            description="Pass a cookie log file and a date to find most active")

    parser.add_argument(
        'filePath',
        type=checkFileInput,
        metavar='',
        help="The cookie log file path"
    )

    parser.add_argument(
        '-d',
        '--date',
        type=formatDateInput,
        metavar='',
        required=True,
        help="desired query date in YYYY-MM-DD format"
    )

    return parser.parse_args(args)


def findCookie(filePath, date):
    activityCounter = Counter()

    with open(filePath, 'r') as file:
        if len(file.readlines()) == 0:
            raise Exception("Empty File")

        file.seek(0)

        if csv.Sniffer().has_header(file.read(2048)) == False:
            raise Exception(
                "Incorrect csv formatting: Needs header in form cookie,timestamp")

        file.seek(0)

        csvReader = csv.DictReader(file)

        for index, record in enumerate(csvReader):
            if not record["cookie"]:
                warnings.warn(
                    f"encountered empty cookie ID at line {index + 2}")
                continue

            if not record["timestamp"]:
                warnings.warn(
                    f"encountered empty timestamp at line {index + 2}")
                continue

            try:
                currentDate = datetime.datetime.fromisoformat(
                    record["timestamp"])
            except ValueError as e:
                raise Exception(
                    "Incorrect CSV formatting: timestamp not in iso format") from e

            dayDiff = (currentDate-date).days
            # since we know the data is sorted before hand, we can create a short circuit if query is later than current date
            if dayDiff < 0:
                break
            elif dayDiff > 0:
                continue

            # I don't think writing the rest of the block of code in a else statement is readable, so no else here
            # here we are assume that currentDate = date

            activityCounter.update({record["cookie"]: 1})

    output = []
    if len(activityCounter.keys()) == 0:
        return output

    _, maxCount = activityCounter.most_common(1)[0]

    for cookie in activityCounter:
        if activityCounter[cookie] == maxCount:
            # I am returning the output as a list for easier testing, I could also capture the system out.
            print(cookie)

            output.append(cookie)

    return output
