# TODO: Error Handling
# TODO: More Website

import datetime
from extractors.wwr import extract_wwr_jobs

keyword = input("What do you want to search for? -> ")

wwr = extract_wwr_jobs(keyword)

jobs = wwr  # + wwr + wwr

time_str = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

# Create a file
file = open(f"{keyword}_{time_str}.csv", "w")

# Write Headers
file.write("Position,Company,Kind,Location,URL\n")

# Write Contents
for job in jobs:
    file.write(
        f"{job['position']},{job['company']},{job['kind']},{job['region']},{job['link']}\n")

# Done
file.close()
