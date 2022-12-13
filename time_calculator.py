from time import time


week_days = [
        "Sunday",
        "Monday",
        "tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
]

def add_time(start, duration, *args):
        [L, N] = start.split(" ")
        [SH, SM] = L.split(":")
        [DH, DM] = duration.split(":")

        days = 0

        total_minutes = int(SM) + int(DM)
        total_hours = int(SH) + int(DH)
        if total_minutes > 60:
                total_minutes -= 60
                total_hours += 1
        if total_minutes < 10:
                total_minutes = f"{total_minutes}".zfill(2)
        if total_hours >= 12:
                p, th = divmod(total_hours, 12)
                total_hours = th if th else total_hours
                if total_hours > 12:
                        total_hours = total_hours - ((p - 1) * 12)
                if p > 0:
                        if N == 'PM':
                                days = ((p - 1) // 2) + 1
                        else:
                                days = p // 2

                if p > 0 and p % 2 != 0:
                        N = 'AM' if N == 'PM' else 'PM'
        new_time = str(total_hours) + ":"
        new_time += str(total_minutes) + f" {N}"

        if args:
                day = args[0].title()
                if days > 0:
                        index = week_days.index(day)

                        index += days % 7
                        if index > 6:
                                index = index - 7
                        day = week_days[index]

                new_time += f", {day}"

        if days == 1:
                new_time += "(next day)".rjust(12)
        elif days > 1:
                new_time += f" ({days} days later) "

        return new_time
