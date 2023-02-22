#!bin/python3
import calendar as cal

if __name__ == '__main__':
    m, d, y = map(int, input().split())
    print(cal.day_name[cal.weekday(y, m, d)].upper())