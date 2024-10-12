from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    header = {"User-Agent": "Mozilla/5.0 (Windows; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/3.4|4399.air.wd|4399.zm5.air"}
    res = requests.get("https://www.4399.com/flash/zmhj2.htm",headers=header)
    soup = BeautifulSoup(res.content,"html.parser")
    for a_tag in soup.find_all('a'):
        img_tag = a_tag.find('img')
        if img_tag and '5.png' in img_tag['src']:
            link = a_tag['href']
            print(link)
    res = requests.get(link,headers=header)
    res.encoding = "gb2312"
    soup = BeautifulSoup(res.content,"html.parser")
    swf_name = soup.find("embed")["src"]
    swf_url = link[:link.rfind("/") + 1] + swf_name
    res = requests.get(swf_url,headers=header)
    print(swf_name)
    with open(swf_name,"wb+") as file:
        file.write(res.content)
    exit()