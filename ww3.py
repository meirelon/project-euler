from datetime import datetime, timedelta
import re

start = datetime.strptime("1900-01-01", "%Y-%m-%d")
end = datetime.strptime("2200-01-01", "%Y-%m-%d")
date_generated = [start + timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    date_split = date.strftime("%Y-%m-%d").split("-")
    year_split = re.findall('.{1,2}', date_split.pop(0))
    nums = sum([int(y) for y in year_split] + [int(d) for d in date_split])
    if nums == 68:
        print(date)