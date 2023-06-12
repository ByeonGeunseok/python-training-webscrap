from datetime import datetime


def save_to_file(file_name, jobs):
    time_str = datetime.now().strftime('%Y%m%d_%H%M%S')

    # Create a file
    file = open(f"{file_name}_{time_str}.csv", "w")

    # Write Headers
    file.write("Position,Company,Kind,Location,URL\n")

    # Write Contents
    for job in jobs:
        file.write(
            f"{job['position']},{job['company']},{job['kind']},{job['region']},{job['link']}\n")

    # Done
    file.close()
