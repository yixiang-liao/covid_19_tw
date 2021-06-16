import requests
import json



def query_case_by_date():
    day = input("查詢日期: (格式 YYYY/MM/DD)")

    # 開放資料連結
    url = 'https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.json'
    # 以 requests 模組發出 HTTP GET 請求
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions as err:
        print(err)

    # 將回傳結果轉換成標準JSON格式
    data = json.loads(response.text)
    # data裡面包含所有案例
    print('OVID-19確診人數:')
    print(day[0:4] + '年' + day[4:6] + '月' + day[6:8] + '日')
    covid_total = 0
    # 縣市的案例dictionary
    covid_city_dictionary = {}
    # 迴圈所有案例
    for case in data:
        # 尋找符合條件的案例
        if case['個案研判日'] == day and case['是否為境外移入'] == '否':
            print(f"性別:{case['性別']}\n縣市:{case['縣市']}\n鄉鎮:{case['鄉鎮']}")
            # city = 縣市
            city = case['縣市']
            # 當天人數+1
            covid_total += 1
            # 縣市dictionary 加1. get那個是取之前的值 沒有的話就從0開始
            covid_city_dictionary[city] = covid_city_dictionary.get(city, 0) + 1

    print(f'確診人數:{covid_total}人')
    print('各地區確診人數:')
    # loop剛剛的縣市案例dictionary sorted(covid_city_dictionary.items(), key=lambda e:e[1], reverse=True)
    for city, number in sorted(covid_city_dictionary.items(), key=lambda e:e[1], reverse=True):
        # 用f string print每個縣市
        print(f'{city}{number}人')

if __name__ == "__main__":
    query_case_by_date()