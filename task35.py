import calendar
import json

def get_data(file: str) -> dict:
    with open(file, 'r') as f:
        return dict(json.load(f))


birthdays_dict = get_data('task34_birthdays.json')

months_id = {}
for i in range(1, 13):
    months_id[i] = calendar.month_name[i]

months_count = {}

for key in birthdays_dict:
    id = birthdays_dict[key][:2]
    month_name = months_id[int(id)]
    if month_name in months_count:
        months_count[month_name] += 1
    else:
        months_count[month_name] = 1

print(months_count)