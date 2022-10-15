# from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver

def extract_indeed_jobs(keyword):
    browser=webdriver.Chrome()
    browser.get(f"https://www.indeed.com/jobs?q={keyword}+engineering")
    results=[]
    soup=BeautifulSoup(browser.page_source, "html.parser")
    job_list=soup.find('ul', class_="jobsearch-ResultsList")
    jobs=job_list.find_all('li', recursive=False) #only first surface li
    for job in jobs:
        zone=job.find('div', class_="mosaic-zone")
        if zone == None: #it allows only consider none mosaic-zone
            anchor = job.select_one("h2 a")
            link=anchor['href']
            position = anchor['aria-label']
            company = job.find("span", class_="companyName")
            location = job.find('div', class_="companyLocation")
            job_data={
                "company": company.string,
                "position":position,
                "location":location.string,
                "link": f"https://www.indeed.com{link}",
            }
            results.append(job_data)

    for result in results:
        print(result, "///////////\n")
    browser.quit()

   

extract_indeed_jobs('aerospace')


#keyword can be aerospace or mechanical 
#extract from each usa server and kr server
#add click action of each list of jobs
#add action repeat process for all paginations