import requests
from datetime import datetime
from bs4 import BeautifulSoup
import json
import time
import logging
import urllib3


#logging.basicConfig(level=logging.INFO)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
shares_dict = {}
symbol_list = []
dt = datetime.now().strftime("%d-%b-%Y")
output_file = "D:\\Downloads\\shares_data\\"+dt+".csv"

def get_market_data():
    cnt = 0
    with open("D:\\Downloads\\shares_data\\NSE_Equity_list.csv") as sym_list:
        symbol = sym_list.readlines()
    get_stock_data(symbol, "no")
    print("List data is: %s" % symbol_list)
    while len(symbol_list) != 0 and cnt <= 2:
        print("Symbol list: %d, count: %d" % (len(symbol_list), cnt))
        get_stock_data(symbol_list, "yes")
        cnt = cnt + 1
    print("List data is: %s" % symbol_list)
    for sym in symbol_list:
        with open(output_file, "a+") as last_data:
            last_data.write(sym+",0,0,0,0,0,0,0,FALSE\n")
        print(sym,",0,0,0,0,0,0,0,FALSE")

def get_stock_data(stock_name, is_list):
    #url = "https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY"
    HEADERS = {'User-Agent': 'Mozilla/5.0'}
    for symbol_line in tuple(stock_name):
        try:
            url = "https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol="+symbol_line.strip()
            page = requests.get(url, headers=HEADERS, verify=False, timeout=10)
            soup = BeautifulSoup(page.content, 'html.parser')
            div_tag = soup.find('div', id='responseDiv')
            trade_data = json.loads(div_tag.string.strip())
            traded_volume = trade_data['data'][0]['totalTradedVolume'].replace(',', '')
            open_price = trade_data['data'][0]['open'].replace("'", '').replace(',', '')
            close_price = trade_data['data'][0]['closePrice'].replace("'", '').replace(',', '')
            high_52 = trade_data['data'][0]['high52'].replace("'", '').replace(',', '')
            low_52 = trade_data['data'][0]['low52'].replace("'", '').replace(',', '')
            price_change = float(close_price) - float(open_price)
            percent_change = price_change/float(open_price) * 100
            price_change_str = str(round(price_change, 2))
            percent_change_str = str(round(percent_change, 2))
            change_type = "FALSE"
            if percent_change > 0:
                change_type = "TRUE"
            #Sample data for traded_volume variable is
            #Div tag type is: {'tradedDate': '25JUN2021', 'data': [{'pricebandupper': '223.55', 'symbol': 'ITC', 'applicableMargin': '14.92', 'bcEndDate': '-', 'totalSellQuantity': '-', 'adhocMargin': '-', 'companyName': 'ITC Limited', 'marketType': 'N', 'exDate': '10-JUN-21', 'bcStartDate': '-', 'css_status_desc': 'Listed', 'dayHigh': '205.60', 'basePrice': '203.25', 'securityVar': '11.42', 'pricebandlower': '182.95', 'sellQuantity5': '-', 'sellQuantity4': '-', 'sellQuantity3': '-', 'cm_adj_high_dt': '09-FEB-21', 'sellQuantity2': '-', 'dayLow': '203.75', 'sellQuantity1': '-', 'quantityTraded': '1,38,77,208', 'pChange': '0.86', 'totalTradedValue': '28,417.75', 'deliveryToTradedQuantity': '56.25', 'totalBuyQuantity': '3,760', 'averagePrice': '204.78', 'indexVar': '-', 'cm_ffm': '1,79,184.74', 'purpose': 'DIVIDEND - RS 5.75 PER SHARE', 'buyPrice2': '-', 'secDate': '25-Jun-2021 00:00:00', 'buyPrice1': '205.05', 'high52': '239.20', 'previousClose': '203.25', 'ndEndDate': '-', 'low52': '163.35', 'buyPrice4': '-', 'buyPrice3': '-', 'recordDate': '11-JUN-21', 'deliveryQuantity': '78,06,217', 'buyPrice5': '-', 'priceBand': 'No Band', 'extremeLossMargin': '3.50', 'cm_adj_low_dt': '30-OCT-20', 'varMargin': '11.42', 'sellPrice1': '-', 'sellPrice2': '-', 'totalTradedVolume': '1,38,77,208', 'sellPrice3': '-', 'sellPrice4': '-', 'sellPrice5': '-', 'change': '1.75', 'surv_indicator': '-', 'ndStartDate': '-', 'buyQuantity4': '-', 'isExDateFlag': False, 'buyQuantity3': '-', 'buyQuantity2': '-', 'buyQuantity1': '3,760', 'series': 'EQ', 'faceValue': '1.00', 'buyQuantity5': '-', 'closePrice': '205.05', 'open': '204.00', 'isinCode': 'INE154A01025', 'lastPrice': '205.00'}], 'optLink': '/marketinfo/sym_map/symbolMapping.jsp?symbol=ITC&instrument=-&date=-&segmentLink=17&symbolCount=2', 'otherSeries': ['EQ'], 'futLink': '/live_market/dynaContent/live_watch/get_quote/GetQuoteFO.jsp?underlying=ITC&instrument=FUTSTK&expiry=01JUL2021&type=-&strike=-', 'lastUpdateTime': '25-JUN-2021 15:57:50'}
            #print("Traded volumes are: %s" % traded_volume)
            with open(output_file, "a+") as opt_fl:
                opt_fl.write(symbol_line.strip()+","+traded_volume+","+open_price+","+close_price+","+price_change_str+","+percent_change_str+","+low_52+","+high_52+","+change_type+"\n")
            print(symbol_line.strip()+","+traded_volume+","+open_price+","+close_price+","+price_change_str+","+percent_change_str+","+low_52+","+high_52+","+change_type)
            #creating dictionary with symbol name
            shares_dict[symbol_line.strip()] = {}
            shares_dict[symbol_line.strip()]['Traded_volume'] = traded_volume
            shares_dict[symbol_line.strip()]['Opening_price'] = float(open_price)
            shares_dict[symbol_line.strip()]['Closing_price'] = float(close_price)
            shares_dict[symbol_line.strip()]['high_52'] = float(high_52)
            shares_dict[symbol_line.strip()]['low_52'] = float(low_52)
            if is_list == "yes":
                symbol_list.pop(symbol_list.index(symbol_line.strip()))

        except requests.exceptions.Timeout as te:
            time.sleep(10)
            if symbol_line.strip() not in symbol_list:
                symbol_list.append(symbol_line.strip())

        except Exception as e:
            time.sleep(10)
            if symbol_line.strip() not in symbol_list:
                symbol_list.append(symbol_line.strip())

def nifty_50_data():
    nifty_50_list = ('ADANIPORTS', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO', 'BAJAJFINSV', 'BAJFINANCE', 'BHARTIARTL', 'BPCL', 'BRITANNIA', 'CIPLA', 'COALINDIA', 'DIVISLAB', 'DRREDDY', 'EICHERMOT', 'GRASIM', 'HCLTECH', 'HDFC', 'HDFCBANK', 'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO', 'HINDUNILVR', 'ICICIBANK', 'INDUSINDBK', 'INFY', 'IOC', 'ITC', 'JSWSTEEL', 'KOTAKBANK', 'LT', 'M&M', 'MARUTI', 'NESTLEIND', 'NTPC', 'ONGC', 'POWERGRID', 'RELIANCE', 'SBILIFE', 'SBIN', 'SHREECEM', 'SUNPHARMA', 'TATACONSUM', 'TATAMOTORS', 'TATASTEEL', 'TCS', 'TECHM', 'TITAN', 'ULTRACEMCO', 'UPL', 'WIPRO')
    with open(output_file, "r+") as all_file_data:
        all_data = all_file_data.readlines()
    for i in all_data:
        stock_name = i.split(",")[0]
        if stock_name in nifty_50_list:
            stock_data = i.split(',')
            stck_nm = stock_data[0]
            volumes = stock_data[1]
            close_price = stock_data[3]
            week_52_high = stock_data[7]
            price_diff = float(week_52_high) - float(close_price)
            print(stck_nm+','+volumes+','+close_price+','+week_52_high+','+str(round(price_diff, 2)))



if __name__ == "__main__":
    get_market_data()
    nifty_50_data()
    #print("Shares dictionary is: %s" % shares_dict)
