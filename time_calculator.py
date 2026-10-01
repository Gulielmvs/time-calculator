def add_time(start, duration, day=None):
    week = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
    ]
    start = start.split()
    format = start[1]
    start_time = start[0].split(':')
    start_hour = int(start_time[0])
    start_minutes = int(start_time[1])
    duration = duration.split(':')
    duration_hours = int(duration[0])
    duration_minutes = int(duration[1])

    # Minutes
    extra_hour = 0
    new_minutes = start_minutes + duration_minutes
    if new_minutes > 59:
        new_minutes = new_minutes - 60
        extra_hour = 1

    # Hours
    new_days = 0
    for i in range(duration_hours + extra_hour):
        start_hour = start_hour + 1
        if start_hour == 12:
            if format == 'AM':
                format = 'PM'
            elif format == 'PM':
                format = 'AM'
                new_days = new_days + 1
        elif start_hour > 12:
            start_hour = 1

    # Days
    if day is not None:
        day = day.capitalize()
        today = week.index(day)
        for i in range(new_days):
            today = today + 1
            if today > 6:
                today = 0
        new_today = week[today]
        result_day = f', {new_today}'
    else:
        result_day = ''

    if new_days > 1:
        day_later = f' ({new_days} days later)'
    elif new_days == 1:
        day_later = ' (next day)'
    else:
        day_later = ''

    # New time
    new_time = f'{start_hour}:{new_minutes:02d} {format}{result_day}{day_later}'
    return new_time
