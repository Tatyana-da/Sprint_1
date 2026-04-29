time_string = '1h 45m,360s,25m,30m 120s,2h 60s'

time_string_new = time_string.replace(' ', '')
time_values = time_string_new.split(',')

total_minutes = 0 

for value in time_values:
    minutes = 0 
    if 'h' in value:
        value = value.replace('h', '*60+')

    if 'm' in value:
        value = value.replace('m', '+')

    if 's' in value:
        value = value.replace('s', '//60+')

    value = value.rstrip('+')
    minutes = eval(value)
    total_minutes += minutes

print(total_minutes)