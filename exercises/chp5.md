# chp5.
3. 다음 조건으로 클래스와 그 클래스를 사용하는 프로그램을 만드시오.
   class SayDays:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = daㅛ
        self.is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        self.month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap:
            self.month_days[1] = 29

    def days(self):
        total_days = sum(self.month_days[:self.month - 1]) + self.day
        return total_days

    def days_left(self):
        year_total = 366 if self.is_leap else 365
        return year_total - self.days()

    def weekday(self):
        y = self.year
        m = self.month
        d = self.day
        
        if m < 3:
            m += 12
            y -= 1
            
        k = y % 100
        j = y // 100
        
        # h = (q + [13(m+1)/5] + K + [K/4] + [J/4] - 2J) mod 7
        h = (d + ((13 * (m + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)) % 7
        return h

    def weekday_name(self):
        names = ["토요일", "일요일", "월요일", "화요일", "수요일", "목요일", "금요일"]
        return names[self.weekday()]

while True:
    try:
        user_input = input("날짜를 입력해줘 (예: 2024 10 25, 종료하려면 'q' 입력): ")
        if user_input.lower() == 'q':
            break
            
        y, m, d = map(int, user_input.split())
        sd = SayDays(y, m, d)
        
        print(f"1. 1월 1일 기준: {sd.days()}일째")
        print(f"2. 12월 31일 기준 남은 일수: {sd.days_left()}일")
        print(f"3. 요일 숫자 (0:토): {sd.weekday()}")
        print(f"4. 요일 이름: {sd.weekday_name()}")
        print("-" * 30)
        
    except ValueError:
        print("잘못된 입력방식")
