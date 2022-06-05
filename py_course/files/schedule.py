import shelve

# monday_schedule = ['English language', 'System programing', 'Python']
# tuesday_schedule = ['Reading', 'English language', 'System programing', 'Python']
# wednesday_schedule = ['English language', 'System programing', 'Python', 'HTML']
# thursday_schedule = ['English language', 'System programing', 'Python', 'CSS']
# friday_schedule = ['English language', 'System programing', 'Python', 'JavaScript']
# saturday_schedule = ['Reading', 'English language', 'PowerShell', 'Python']

with shelve.open('schedules') as schedules:
    # schedules['monday_schedule'] = monday_schedule
    # schedules['tuesday_schedule'] = tuesday_schedule
    # schedules['wednesday_schedule'] = wednesday_schedule
    # schedules['thursday_schedule'] = thursday_schedule
    # schedules['friday_schedule'] = friday_schedule
    # schedules['saturday_schedule'] = saturday_schedule

    schedules['thursday_schedule'].append('Anime watching')

    for key in schedules:
        print(key, schedules[key])

    