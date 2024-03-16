
from bs4 import BeautifulSoup as bs
from datetime import datetime
from pprint import pprint
from tkinter import *
import tkinter.font
import requests
import re

def dt_hour_():
    now = datetime.now()
    h = now.hour
    m = now.minute
    return h

def dt_wf(): #현재온도, 최저, 최고, 강수확률, 미세, 초미세, 날씨상태
    html= requests.get("https://search.naver.com/search.naver?query=날씨")
    soup = bs(html.text, 'html.parser')

    data_local = soup.find('h2',{'class':'blind'})#지역
    data_local = data_local.text
    
    data_td_c = soup.find('div',{'class':'temperature_text'})#현재 온도
    td_c = data_td_c.text
    td_c = td_c[6:]
    
    data_td_low = soup.find('span',{'class':'lowest'})#최저기온
    td_low = data_td_low.text
    td_low = td_low[4:]
    
    
    data_td_high = soup.find('span',{'class':'highest'})#최고기온
    td_high = data_td_high.text
    td_high = td_high[4:]
    
    data_td_r = soup.find('dd',{'class':'desc'}) #강수확률
    td_r = re.findall("\d+",data_td_r.text)
    td_r = td_r[0]
    
    data_td_pm = soup.find('ul',{'class':'today_chart_list'}) #미세먼지, 초미세먼지
    td_pm = data_td_pm.text
    td_pm = list(filter(len,td_pm.split(' ')))
    td_pm10 = td_pm[1]
    td_pm25 = td_pm[3]
    
    data_td_n = soup.find('span',{'class':'weather before_slash'}).text #현제 날씨 텍스트
    data_td_n = re.sub(r"\s+", "", data_td_n, flags=re.UNICODE)

    return td_c, td_low, td_high, td_r, td_pm10, td_pm25, data_td_n, data_local

def srf_(): #시간,온도, 강수확률
    html= requests.get("https://search.naver.com/search.naver?query=날씨")
    soup = bs(html.text, 'html.parser')
    
    data_local = soup.find('h2',{'class':'blind'})#지역
    data_local = data_local.text

    data_ct = soup.find('div',{'class':'graph_inner _hourly_weather'})#날씨
    data_c = data_ct.findAll('span',{'class':"num"})
    data_t = data_ct.findAll('dt')

    data_tt=[]
    data_rc=[]
    data_rt=[]
    ad_rt =[]
    
    data_t = data_ct.findAll('dt') #시간
    data_c = data_ct.findAll('span',{'class':"num"}) #온도
    data_rr = soup.find('div',{'class':'icon_wrap'}) #강수확률
    data_r = data_rr.findAll('em')

    for i in range(4):
        data_rt.append(data_r[i].text)
        data_tt.append(data_t[i].text)
        data_rc.append(data_c[i].text)

    for i in range(6):
        ad = re.findall('\d+', data_r[i].text)
        ad_rt.append(ad[0])


    return data_tt, data_rc, data_rt, ad_rt
    

def wk1_():
    html= requests.get("https://search.naver.com/search.naver?query=날씨")
    soup = bs(html.text, 'html.parser')

    data_wk = soup.findAll('ul',{'class':'week_list'})
    wk = data_wk[0].text
    wk = list(filter(len, wk.split(' ')))
    fin_t = [i for i in range(len(wk)) if '최고' in wk[i]]
    
    wk1 = wk[fin_t[0]+1:fin_t[1]+1]
    wk1_d = wk1[0]
    wk1_rn = [i for i in range(4) if '%' in wk1[i]]
    wk1_r = re.findall('\d+', wk1[wk1_rn[0]])
    wk1_r = wk1_r[0]
    wk1_ln = [i for i in range(len(wk1)) if '최저' in wk1[i]]
    wk1_l = wk1[wk1_ln[0]]
    wk1_l = wk1_l[4:]
    wk1_hn = [i for i in range(len(wk1)) if '최고' in wk1[i]]
    wk1_h = wk1[wk1_hn[0]]
    wk1_h = wk1_h[4:]

    return wk1_d, wk1_r, wk1_l, wk1_h

def wk2_():
    html= requests.get("https://search.naver.com/search.naver?query=날씨")
    soup = bs(html.text, 'html.parser')

    data_wk = soup.findAll('ul',{'class':'week_list'})
    wk = data_wk[0].text
    wk = list(filter(len, wk.split(' ')))
    fin_t = [i for i in range(len(wk)) if '최고' in wk[i]]
    
    wk2 = wk[fin_t[1]+1:fin_t[2]+1]
    wk2_d = wk2[0]
    wk2_rn = [i for i in range(4) if '%' in wk2[i]]
    wk2_r = re.findall('\d+', wk2[wk2_rn[0]])
    wk2_r = wk2_r[0]
    wk2_ln = [i for i in range(len(wk2)) if '최저' in wk2[i]]
    wk2_l = wk2[wk2_ln[0]]
    wk2_l = wk2_l[4:]
    wk2_hn = [i for i in range(len(wk2)) if '최고' in wk2[i]]
    wk2_h = wk2[wk2_hn[0]]
    wk2_h = wk2_h[4:]

    return wk2_d, wk2_r, wk2_l, wk2_h

def wk3_():
    html= requests.get("https://search.naver.com/search.naver?query=날씨")
    soup = bs(html.text, 'html.parser')

    data_wk = soup.findAll('ul',{'class':'week_list'})
    wk = data_wk[0].text
    wk = list(filter(len, wk.split(' ')))
    fin_t = [i for i in range(len(wk)) if '최고' in wk[i]]
    
    wk3 = wk[fin_t[2]+1:fin_t[3]+1]
    wk3_d = wk3[0]
    wk3_rn = [i for i in range(4) if '%' in wk3[i]]
    wk3_r = re.findall('\d+', wk3[wk3_rn[0]])
    wk3_r = wk3_r[0] 
    wk3_ln = [i for i in range(len(wk3)) if '최저' in wk3[i]]
    wk3_l = wk3[wk3_ln[0]]
    wk3_l = wk3_l[4:]
    wk3_hn = [i for i in range(len(wk3)) if '최고' in wk3[i]]
    wk3_h = wk3[wk3_hn[0]]
    wk3_h = wk3_h[4:]

    return wk3_d, wk3_r, wk3_l, wk3_h

def wk4_():
    html= requests.get("https://search.naver.com/search.naver?query=날씨")
    soup = bs(html.text, 'html.parser')

    data_wk = soup.findAll('ul',{'class':'week_list'})
    wk = data_wk[0].text
    wk = list(filter(len, wk.split(' ')))
    fin_t = [i for i in range(len(wk)) if '최고' in wk[i]]
    
    wk4 = wk[fin_t[3]+1:fin_t[4]+1]
    wk4_d = wk4[0]
    wk4_rn = [i for i in range(4) if '%' in wk4[i]]
    wk4_r = re.findall('\d+', wk4[wk4_rn[0]])
    wk4_r = wk4_r[0] 
    wk4_ln = [i for i in range(len(wk4)) if '최저' in wk4[i]]
    wk4_l = wk4[wk4_ln[0]]
    wk4_l = wk4_l[4:]
    wk4_hn = [i for i in range(len(wk4)) if '최고' in wk4[i]]
    wk4_h = wk4[wk4_hn[0]]
    wk4_h = wk4_h[4:]

    return wk4_d, wk4_r, wk4_l, wk4_h

def wk5_():
    html= requests.get("https://search.naver.com/search.naver?query=날씨")
    soup = bs(html.text, 'html.parser')

    data_wk = soup.findAll('ul',{'class':'week_list'})
    wk = data_wk[0].text
    wk = list(filter(len, wk.split(' ')))
    fin_t = [i for i in range(len(wk)) if '최고' in wk[i]]
    
    wk5 = wk[fin_t[4]+1:fin_t[5]+1]
    wk5_d = wk5[0]
    wk5_rn = [i for i in range(4) if '%' in wk5[i]]
    wk5_r = re.findall('\d+', wk5[wk5_rn[0]])
    wk5_r = wk5_r[0] 
    wk5_ln = [i for i in range(len(wk5)) if '최저' in wk5[i]]
    wk5_l = wk5[wk5_ln[0]]
    wk5_l = wk5_l[4:]
    wk5_hn = [i for i in range(len(wk5)) if '최고' in wk5[i]]
    wk5_h = wk5[wk5_hn[0]]
    wk5_h = wk5_h[4:]

    return wk5_d, wk5_r, wk5_l, wk5_h

def wk6_():
    html= requests.get("https://search.naver.com/search.naver?query=날씨")
    soup = bs(html.text, 'html.parser')

    data_wk = soup.findAll('ul',{'class':'week_list'})
    wk = data_wk[0].text
    wk = list(filter(len, wk.split(' ')))
    fin_t = [i for i in range(len(wk)) if '최고' in wk[i]]
    
    wk6 = wk[fin_t[5]+1:fin_t[6]+1]
    wk6_d = wk6[0]
    wk6_rn = [i for i in range(4) if '%' in wk6[i]]
    wk6_r = re.findall('\d+', wk6[wk6_rn[0]])
    wk6_r = wk6_r[0] 
    wk6_ln = [i for i in range(len(wk6)) if '최저' in wk6[i]]
    wk6_l = wk6[wk6_ln[0]]
    wk6_l = wk6_l[4:]
    wk6_hn = [i for i in range(len(wk6)) if '최고' in wk6[i]]
    wk6_h = wk6[wk6_hn[0]]
    wk6_h = wk6_h[4:]

    return wk6_d, wk6_r, wk6_l, wk6_h

def ch_():
    html2= requests.get("https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%BD%94%EB%A1%9C%EB%82%98")
    soup2 = bs(html2.text, 'html.parser')

    data_covid = soup2.find('div',{'class':'wrap_condition'})#다음 코로나 확진자 사망
    data_covid1 = re.findall("\d+",data_covid.text)
    data_covid_local = soup2.find('li',{'class':'location_daejeon'})#대전 확진자
    data_covid_local1 = re.findall("\d+",data_covid_local.text)
    data_covid_local1 = data_covid_local1[0]
    td_ch = data_covid1[0] + data_covid1[1]

    return td_ch, data_covid_local1
    

