import requests
from bs4 import BeautifulSoup

keyword = "python"
url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}"

r = requests.get(url)
#print(r.text)

soup = BeautifulSoup(r.text, "html.parser")
lis = soup.find_all("li", class_="c_col") #이러면 리스트 형태로 저장됨

for li in lis:
    company = li.find("a", class_="cpname").text
    title = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").text
    print(company)