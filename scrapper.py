import requests
from bs4 import BeautifulSoup

def search_incruit(keyword):

    url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}"

    import requests
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    lis = soup.find_all("li", class_="c_col") #이러면 리스트 형태로 저장됨

    jobs = []

    for li in lis:
        company = li.find("a", class_="cpname").text
        title = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").text
        location = li.find("div", class_="cl_md").find_all("span")[0].text
        link = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").get("href")
        
        job_data = {
            "site" : "인크루트",
            "company": company,
            "title": title,
            "location": location,
            "link" : link
        }

        jobs.append(job_data)

    return jobs

def search_saramin(keyword):
    url = f"https://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword={keyword}"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    lis = soup.find_all("div", class_="item_recruit")

    jobs = []

    for li in lis:
        company = li.find("div", class_="area_corp").text
        title = li.find("h2", class_="job_tit").text
        location = li.find("div", class_="job_condition").find_all("span")[0].text
        link = li.find("div", class_="area_job").find("h2", class_="job_tit").find("a").get("href")

        job_data = {
            "site" : "사람인",
            "company" : company,
            "title" : title,
            "location" : location,
            "link" : link
        }

        jobs.append(job_data)
    
    return jobs
