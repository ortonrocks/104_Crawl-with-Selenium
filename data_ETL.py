import pandas as pd
import csv


df=pd.read_csv('data50.csv',encoding='UTF-8')
df

job_dict = {}

for i in range(len(df['職務類別'])):
    job_list = df['職務類別'][i].split(',')
    # print(job_list)
for i in range(len(df['職務類別'])):
    job_list = df['職務類別'][i].split(',')
    for i in range(len(job_list)):
        if job_list[i] in job_dict.keys():
            job_dict[job_list[i]] = job_dict[job_list[i]] + 1

        else:
            job_dict[job_list[i]] = 1

with open('job_type.txt', 'w') as f:
    writer = csv.writer(f)
    for k, v in job_dict.items():
        writer.writerow([k, v])

df2=df[['工作名稱','公司','工作內容']]

for i in range(len(df['擅長工具'])):
    df['擅長工具'][i]=df['擅長工具'][i].split(',')
df3=df[['擅長工具']]
df4=df3['擅長工具'].apply(lambda x: pd.Series([1] * len(x), index=x)).fillna(0, downcast='infer')

df_final=pd.concat([df2,df4],axis=1)
df_final.to_csv('skills_required.csv',encoding='utf_8_sig')