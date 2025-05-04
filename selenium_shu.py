from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def get_grades(account, password):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)

    driver.get("https://infosys.shu.edu.tw/")
    driver.find_element(By.ID, "username").send_keys(account)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(3)

    # 導向成績頁面（請根據實際成績頁網址更新）
    driver.get("https://infosys.shu.edu.tw/grades")
    time.sleep(2)

    grade_text = driver.find_element(By.ID, "gradeTable").text
    driver.quit()
    return grade_text
