from requests import get
from bs4 import BeautifulSoup


def extract_wwr_jobs(keyword):
    # USE CAREFULLY !
    # ONLY FOR PRACTICE !
    base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
    response = get(f"{base_url}{keyword}")

    # When the response is normal
    if response.status_code == 200:
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all('section', class_="jobs")

        # Get '.jobs > li' and then delete 'View All'
        for job_section in jobs:
            job_posts = job_section.find_all('li')
            job_posts.pop(-1)

            # Get all anchor tag
            for post in job_posts:
                anchors = post.find_all('a')
                anchor = anchors[1]

                # Get link in anchor
                link = anchor['href']

                # Get company, kind, region class HTML element
                company, kind, region = anchor.find_all(
                    'span', class_="company")

                # Get title class HTML element
                title = anchor.find('span', class_="title")

                # Create Dictionary
                job_data = {
                    'link': f"https://weworkremotely.com{link}",
                    'company': company.string.replace(",", " "),
                    'kind': kind.string.replace(",", " "),
                    'region': region.string.replace(",", " "),
                    'position': title.string.replace(",", " ")
                }

                # Save the results
                results.append(job_data)
        return results
