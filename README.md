# 104_Crawl-with-Selenium

*使用者需要先下載CHROME版本對應的 Webdriver

DOWNLOAD LINK-(https://chromedriver.chromium.org/downloads)

主要有以下幾種功能：

1.爬蟲UI界面（可將結果輸出到界面）

2.使用者可自行選擇爬取關鍵字、爬取職缺數量(將完整資料儲存至data50.csv)

3.針對輸出職缺進行職務類別統計（輸出至job_type.txt）

4.將"擅長工具"欄進行dummy_variables分類（並和工作名稱、公司、工作內容一同輸出至skills_required.csv）

以下進行細部說明：

1.爬蟲UI界面（用戶輸入職缺關鍵字、職缺個數並點擊 “開始爬蟲” ）

![alt text](https://github.com/ortonrocks/104_Crawl-with-Selenium/blob/main/%E7%88%AC%E8%9F%B2UI%E7%95%8C%E9%9D%A2.png)


2.點擊“顯示結果”：爬蟲結果以table顯示於界面中（同時儲存資料至data50.csv）

（以關鍵字：AI工程師，個數：50為例）

*因為爬取了所有內容共21欄，以兩頁呈現，具體圖片在壓縮檔中

![alt text](https://github.com/ortonrocks/104_Crawl-with-Selenium/blob/main/%E7%88%AC%E8%9F%B2%E7%B5%90%E6%9E%9C%E5%9C%96%E4%B8%80.png)

![alt text](https://github.com/ortonrocks/104_Crawl-with-Selenium/blob/main/%E7%88%AC%E8%9F%B2%E7%B5%90%E6%9E%9C%E5%9C%96%E4%BA%8C.png)

3.統計職務類別

將所爬取資料的職務類別進行統計並儲存在job_type.txt中


![alt text](https://github.com/ortonrocks/104_Crawl-with-Selenium/blob/main/%E5%B0%8D%E8%81%B7%E7%BC%BA%E9%A1%9E%E5%9E%8B%E9%80%B2%E8%A1%8C%E7%B5%B1%E8%A8%88.png)


4.將“擅長工具”進行dummy_variables的分類並結合“工作名稱、公司、工作內容”欄位儲存在”skills_required.csv中


![alt text](https://github.com/ortonrocks/104_Crawl-with-Selenium/blob/main/%E6%A0%B9%E6%93%9A%E4%B8%8D%E5%90%8C%E6%8A%80%E8%83%BD%E8%A6%81%E6%B1%82%E9%80%B2%E8%A1%8C%E5%88%86%E9%A1%9E.png)




