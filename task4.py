from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.04.27"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Michael Johnson", "birthday": "1988.04.15"},
    {"name": "Emily Brown", "birthday": "1992.07.03"},
    {"name": "William Taylor", "birthday": "1983.04.21"},
    {"name": "Olivia Martinez", "birthday": "1989.09.28"},
    {"name": "Daniel Garcia", "birthday": "1994.02.08"},
    {"name": "Sophia Nguyen", "birthday": "1991.06.12"},
    {"name": "Matthew Clark", "birthday": "1987.03.30"},
    {"name": "Ava Rodriguez", "birthday": "1986.05.17"},
    {"name": "Ethan Hernandez", "birthday": "1993.08.22"},
    {"name": "Isabella Lewis", "birthday": "1995.10.05"},
    {"name": "James Allen", "birthday": "1997.01.31"},
    {"name": "Charlotte King", "birthday": "1984.12.07"},
    {"name": "Alexander Wilson", "birthday": "1982.02.14"},
    {"name": "Mia Adams", "birthday": "1996.09.10"},
    {"name": "Benjamin Moore", "birthday": "1981.08.25"},
    {"name": "Emily Dilson", "birthday": "1981.04.23"}
]

def get_upcoming_birthdays(users: list) -> list:
    """
        Takes a list of users and their birthdays and returns a list of users and dates, 
        when they should be congratulated on their birthdays for the next seven days.
    """
    weeklong_celebrations = list()
    control_day = datetime.today().date()
    last_checked_day = control_day + timedelta(days=7)
    for user in users:
        year, month, day = user["birthday"].split(".")
        user_birthday = datetime(year=datetime.now().year, month=int(month), day=int(day)).date()

        is_a_birthday_this_week = user_birthday >= control_day and user_birthday < last_checked_day
        if is_a_birthday_this_week:
            is_birthday_falls_on_a_weekend = user_birthday.weekday() == 5 or user_birthday.weekday() == 6
            if is_birthday_falls_on_a_weekend:
                delayed_user_birthday = user_birthday + timedelta(days=7 - user_birthday.weekday())
                weeklong_celebrations.append({"name": user["name"], "birthday": delayed_user_birthday})
            else:
                weeklong_celebrations.append({"name": user["name"], "birthday": user_birthday})        
    return weeklong_celebrations
        

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:\n", upcoming_birthdays)
