import requests
import datetime
import configParser
def get_past_days():
    from datetime import datetime, timedelta
    now = datetime.now()
    past_30_days = []
    for i in range(30):
        past_date = now - timedelta(days=i)
        formatted_date = past_date.strftime("%Y%m%d")
        past_30_days.append(formatted_date)
    return past_30_days

if __name__ == '__main__':
    server_pre = "https://sda.4399.com/4399swf/upload_swf/ftp22/csya/20170622/1/assets/data/cg1_"
    header = {"User-Agent": "Mozilla/5.0 (Windows; U; zh-CN) AppleWebKit/533.19.4 (KHTML, like Gecko) AdobeAIR/3.4|4399.air.wd|4399.zm5.air"}
    has_get = False
    file_name = ""
    for i in get_past_days():
        if has_get:
            break
        for j in range(5,0,-1):
            if has_get:
                break
            url = server_pre + str(i) + "_" + str(j) + ".swf"
            print(url)
            data = requests.get(url,headers=header)
            if data.status_code == 404:
                continue
            file_name = "./cg1_" + str(i) + "_" + str(j) + ".swf"
            print("found",file_name)
            with open(file_name,"wb+") as f:
                f.write(data.content)
                f.close()
                has_get = True
    configParser.parseConfigFile(file_name)

