import requests
import json
import matplotlib.pyplot as plt

def everyday_case():
    covid_everyday_dictionary = {}
    # 開放資料連結
    url = 'https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.json'
    # 以 requests 模組發出 HTTP GET 請求
    # res = requests.get(url)
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions as err:
        print(err)
    everyday=[]
    total_case=[]
    # 將回傳結果轉換成標準JSON格式
    data = json.loads(response.text)
    for case in data:
    #      cday = datetime.strptime(case['個案研判日'], '%Y%m%d')

         covid_everyday_dictionary[case['個案研判日']] = covid_everyday_dictionary.get(case['個案研判日'], 0) + 1

    for day,total in covid_everyday_dictionary.items():
        # 用f string print每個縣市
        everyday.append(day)
        total_case.append(total)

    xpt = everyday
    ypt = total_case
    plt.plot(xpt, ypt)  # 畫線
    plt.title("Covid-19", fontsize=24)  # 圖表標題
    plt.xlabel("day", fontsize=16)  # x軸標題
    plt.ylabel("total", fontsize=20)  # y軸標題
    plt.show()  # 顯示繪製的圖形


if __name__ == "__main__":
    everyday_case()