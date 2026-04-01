from datetime import datetime, timedelta

def print_working_days(date1, date2):
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    current = d1
    while current < d2: # zatrzymanie przed date2
        if current.weekday() < 5:   # pon–pt
            print(current.strftime("%Y-%m-%d"))
        current += timedelta(days=1) # przejście do kolejnego dnia
print_working_days("2026-04-01", "2026-04-10")