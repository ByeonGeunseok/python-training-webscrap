from requests import get

# USE CAREFULLY !
base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term = "python"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("no response.")
else:
  print(response.text)

