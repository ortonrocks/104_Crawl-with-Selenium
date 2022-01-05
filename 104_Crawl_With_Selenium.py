#記得install
#!pip install pandastable
import requests
from  bs4 import BeautifulSoup
import json
from selenium.webdriver import Chrome
import pandas as pd
import time
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.common.by import By
from collections import defaultdict
import tkinter as tk
from tkinter import *
from pandastable import Table
import math


# 將HTML資料清洗後存入字典中
# 將HTML資料清洗後存入字典中
# 將HTML資料清洗後存入字典中
def getHTMLcontent_and_saveDict(soup, data_dict):
    ##html清洗
    data = json.loads(soup.find('script', type='application/ld+json').string)
    data[1]['description'] = data[1]['description'].replace('&lt;', '')
    data[1]['description'] = data[1]['description'].replace('br&gt;', '')
    data[1]['description'] = data[1]['description'].replace('h3&gt;', '')
    data[1]['description']

    # html位置標記
    # print(data[1]["description"])

    worktype_label = data[1]['description'].split('- 職務類別：')
    salary_label = worktype_label[1].split('- 工作待遇：')
    jobtype_label = salary_label[1].split('- 工作性質：')
    location_label = jobtype_label[1].split('- 上班地點：')
    try:
        responsibility_label = location_label[1].split('- 管理責任：')
    except IndexError:
        responsibility_label = location_label
    try:
        working_abroad_label = responsibility_label[1].split('- 出差外派：')

    except IndexError:
        working_abroad_label = responsibility_label
    work_time_label = working_abroad_label[1].split('- 上班時段：')
    vacation_label = work_time_label[1].split('- 休假制度：')
    work_date_label = vacation_label[1].split('- 可上班日：')
    try:
        require_num_label = work_date_label[1].split('- 需求人數：')
    except IndexError:
        require_num_label = work_date_label
    experience_label = require_num_label[1].split('- 工作經歷：')
    require_degree_label = experience_label[1].split('- 學歷要求：')
    require_major_label = require_degree_label[1].split('- 科系要求：')
    language_skill_label = require_major_label[1].split('- 語文條件：')
    skills_label = language_skill_label[1].split('- 擅長工具：')
    working_skills_label = skills_label[1].split('- 工作技能：')
    try:
        other_requirements = working_skills_label[1].split('- 其他：')
    except IndexError:
        other_requirements = working_skills_label

    # 參數賦值

    job_name = data[0]['name']
    company_name = data[0]['publisher']['name']
    work_content = worktype_label[0]
    work_type = salary_label[0]
    salary = jobtype_label[0]
    job_type = location_label[0]
    location = responsibility_label[0]
    responsbility = working_abroad_label[0]
    working_abroad = work_time_label[0]
    work_time = vacation_label[0]
    vacation = work_date_label[0]
    work_date = require_num_label[0]
    experience = require_degree_label[0]
    require_num = experience_label[0]
    require_degree = require_num_label[0]
    require_major = language_skill_label[0]
    language_skill = skills_label[0]
    skills = working_skills_label[0]
    working_skills = other_requirements[0]
    try:
        other_requirements = other_requirements[1]
    except IndexError:
        other_requirements = '無'

    content_list = [job_name, company_name, work_content,
                    work_type, salary, job_type, location, responsbility, working_abroad, work_time,
                    vacation, work_date, require_num, experience, require_degree,
                    require_major, language_skill, skills, working_skills, other_requirements]

    i = 0
    # 將查詢值賦值字典
    for key in data_dict:
        data_dict[key].append(content_list[i])
        i = i + 1
    return


# 轉成Dataframe並存入DATA.CSV

def saveDicttoCSV(data_dict):
    df = pd.DataFrame(data=data_dict)
    # display(df)=>可展示df
    df.to_csv('data.csv', index=False, mode='w', encoding='utf-8-sig')
    return df


# 在tkinter 上展現Dataframe
def show_results():
    f = Frame()
    f.pack(fill=BOTH, expand=1)
    df = saveDicttoCSV(data_dict)
    pt = Table(f, dataframe=df, showtoolbar=True, showstatusbar=True)
    pt.show()
    return


def mainfunction():

    inputkeyword=str(keyword_entry.get())
    inputsearchnum=int(amount_entry.get())
    url='https://www.104.com.tw/jobs/search/?ro=0&keyword='+str(inputkeyword)+'&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=1&asc=0&page=1&mode=s&jobsource=tab_cs_to_job&langFlag=0'
    driver=Chrome('./chromedriver.exe')
    driver.get(url)
    time.sleep(5)
    for i in range(1,inputsearchnum+1):
        try:
            python_button = driver.find_elements_by_xpath('/html/body/main/div[3]/div/div[2]/div[4]/article['+str(i)+']/div[1]/h2/a')[0]
        except IndexError :
            python_button = driver.find_elements_by_xpath('/html/body/main/div[3]/div/div[3]/div[4]/article['+str(i)+']/div[1]/h2/a')[0]

        python_button.click()
        p=driver.window_handles[0]
        c=driver.window_handles[1]
        driver.switch_to.window(c)
        #html = driver.execute_script("return document.getElementsByTagName('html')[0].outerHTML")
        html=driver.page_source

        soup=BeautifulSoup(html,'html.parser')
        getHTMLcontent_and_saveDict(soup,data_dict)
        time.sleep(5)
        driver.close()
        driver.switch_to.window(p)
        time.sleep(1)
        driver.execute_script('var s = document.documentElement.scrollTop='+str(200*i))

        time.sleep(1)
    #saveDicttoCSV(data_dict)



data_dict={
            '工作名稱':[],
            '公司':[],
            '工作內容':[],
            '職務類別':[],
            '工作待遇':[],
            '工作性質':[],
            '上班地點':[],
            '管理責任':[],
            '出差外派':[],
            '上班時段':[],
            '休假制度':[],
            '可上班日':[],
            '需求人數':[],
            '學歷要求':[],
            '科系要求':[],
            '語文條件':[],
            '擅長工具':[],
            '工作技能':[],
            '其他條件':[]
        }


window = tk.Tk()
window.title('CFI101-104 homework')
window.geometry('400x300')
window.configure(background='white')


header_label = tk.Label(window, text='CFI101-18 104 關鍵字爬蟲')
header_label.pack()

keyword_frame = tk.Frame(window)
keyword_frame.pack(side=tk.TOP)
keyword_label = tk.Label(keyword_frame, text='請輸入職缺關鍵字：')
keyword_label.pack(side=tk.LEFT)
keyword_entry = tk.Entry(keyword_frame)
keyword_entry.pack(side=tk.LEFT)

amount_frame = tk.Frame(window)
amount_frame.pack(side=tk.TOP)
amount_label = tk.Label(amount_frame, text='請輸入爬取個數')
amount_label.pack(side=tk.LEFT)
amount_entry = tk.Entry(amount_frame)
amount_entry.pack(side=tk.LEFT)

result_label = tk.Label(window)
result_label.pack()



calculate_btn = tk.Button(window, text='開始爬蟲', command=mainfunction)
calculate_btn.pack()

button = Button(window, text="顯示結果", command=show_results)
button.pack()

window.mainloop()