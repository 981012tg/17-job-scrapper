import requests 
from bs4 import BeautifulSoup


def search_incruit(keyword, page=1):

    jobs = []

    for i in range(page):
        page = 30 * i
        url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno={page}"
        r = requests.get(url) 
        soup = BeautifulSoup(r.text, "html.parser")
        lis = soup.find_all("li", class_="c_col")


        for li in lis:
            company = li.find("a", class_="cpname").text
            title = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").text
            location = li.find("div", class_="cl_md").find_all("span")[0].text
            link = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").get("href")
            
            job_data = {
                "site" : "인크루트",
                "company": company, 
                "title" : title, 
                "location": location, 
                "link" : link
            }

            jobs.append(job_data)

    return jobs

def search_saramin(keyword, page=1):
    jobs = []

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/150.0.0.0 Safari/537.36"
        )
    }

    for i in range(page):
        page = i + 1
        url = f"https://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=recently&searchword={keyword}&recruitPage={page}"
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        lis = soup.find_all("div", class_= "item_recruit")

        for li in lis:
            company = li.find("div", class_="area_corp").find("strong", class_="corp_name").find("a").text
            title = li.find("h2", class_="job_tit").find("a").get("title")
            job_condition = li.find("div", class_="job_condition")
            location_tag = job_condition.find("a") if job_condition else None
            location = location_tag.text.strip() if location_tag else "지역 정보 없음"
            link = li.find("h2", class_="job_tit").find("a").get("href")

            if link.startswith("/"):
                link = "https://www.saramin.co.kr" + link

            job_data = {
                "site" : "사람인",
                "company" : company,
                "title" : title,
                "location" : location,
                "link" : link
            }

            jobs.append(job_data)
        
    return jobs

if __name__ == "__main__": 
    incruit_result = search_incruit(keyword, 2)
    saramin_result = search_saramin(keyword, 2)

    result = incruit_result + saramin_result
    print(result)
    print(len(result))
