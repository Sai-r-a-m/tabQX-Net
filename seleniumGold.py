from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import pandas as pd
import time
from dateutil.relativedelta import relativedelta

driver = webdriver.Chrome()

try:
    driver.get("https://finance.yahoo.com/quote/GC%3DF/history/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAEj4EneKneKLy5IJ5A5XLpSw26AlX72KgiihvvvhTSgXZeYjZ8kqQYwA_rwAM9WwHMKAUp7UYP-WHFxlbzUXbK7j-FyZh-LwN4ye8DzFfz3D3wtJeQ8pK0u3YSYrRzLT_cZnW-0fpxDimtrrwLKO8SIlwJzeLshfggdu42yyuN4h&period1=1577631848&period2=1735484489")
    wait = WebDriverWait(driver, 10)    
    
    calendar_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Dec 29, 2019 - Dec 29, 2024']")))
    calendar_button.click()
    time.sleep(1)
    print("Hellooooo")
    date_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='5Y']")))
    date_input.click()
    time.sleep(5)
    print("Hellooooo")

    rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody//tr")))
    data = []
    print("helllllo")
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = [cell.text for cell in cells]
        print(row_data)

    columns = ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]
    df = pd.DataFrame(data, columns=columns)

    df.to_csv("crude_oil_data.csv", index=False)
    print("Data saved to 'gold.csv'.")
    print(df.head())

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()