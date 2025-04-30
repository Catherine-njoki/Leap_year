

class DateCalculator:
    def __init__(self, year, month, day):
        self.original_year = year
        self.month = month
        self.day = day
        self.year = year


        if self.month == 1 or self.month == 2:
            self.month += 12
            self.year -= 1


        self.K = self.year % 100
        self.J = self.year // 100

    def calculate_weekday(self):
        q = self.day
        m = self.month
        K = self.K
        J = self.J


        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + 5 * J) % 7


        weekday_names = [
            "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"
        ]

        return weekday_names[h]


if __name__ == "__main__":

    calculator = DateCalculator(1589, 9, 15)
    weekday = calculator.calculate_weekday()
    print(f"September 15, 1589 was a {weekday}.")
