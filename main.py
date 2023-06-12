# TODO: Error Handling
# TODO: More Website

from extractors.wwr import extract_wwr_jobs
from file import save_to_file

keyword = input("What do you want to search for? -> ")

wwr = extract_wwr_jobs(keyword)

jobs = wwr  # + wwr + wwr

save_to_file(keyword, jobs)
