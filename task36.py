from bokeh.plotting import figure, show
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
    id = int(birthdays_dict[key][:2])
    if id in months_count:
        months_count[id] += 1
    else:
        months_count[id] = 1

months = list(months_count)
count = [months_count[key] for key in months_count]

p = figure(title = 'Months')

p.vbar(months, top = count)

show(p)