def main():
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October',
              'November', 'December']

    while True:
        try:
            date = input('Date: ').strip()

            if '/' in date:
                month, day, year = date.split('/')
                month = int(month)
                day = int(day)
                year = int(year)

            else:
                month_str, rest = date.split(" ", 1)
                day_str, year = rest.split(",")

                if month_str not in months:
                    raise ValueError

                month = months.index(month_str) + 1
                day = int(day_str.strip())
                year = int(year.strip())

            if month < 1 or month > 12:
                raise ValueError

            if day < 1 or day > 31:
                raise ValueError

            print(f'{year}-{month:02}-{day:02}')
            break

        except (ValueError, IndexError):
            continue


if __name__ == '__main__':
    main()