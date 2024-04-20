from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
        Return variance between today and date(yyyy-mm-dd)  
    """
    try:
        year, month, day = date.split("-")
        then = datetime(year=int(year), month=int(month), day=int(day))
        now = datetime.now()
        result = now.date() - then.date()
        return result.days
    except ValueError:
        return 0


print("Result of task1:", get_days_from_today('2003-05-07'))