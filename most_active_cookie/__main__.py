import sys

from .most_active_cookie import findCookie, parseArgs


def main():
    args = parseArgs(sys.argv[1:])
    findCookie(args.filePath, args.date)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
