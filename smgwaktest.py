import time
import random
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()

#무료체험신청 회사명
companyname = '테스트' + str(random.randrange(1,30))
#무료체험신청 대표자명
ceoName = '테스트' + str(random.randrange(1,20))
#무료체험신청 담당자명
testname = '테스트' + str(random.randrange(1,20))
#무료체험신청 이메일
testemail = 'test123@a.com'
#무료체험신청 휴대폰번호
phone = "01000000001"
#무료체험신청 담당업무
testwork = '인사'

#일루미나리안 접속
URL = 'https://illuminarean.com/'
driver.get(URL)
time.sleep(2)

#인재풀 등록 팝업 닫기
driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div/div/button[2]').click()

#WORK 선택
driver.find_element(By.XPATH,'//*[@id="__next"]/div/header/div/div/div/div/nav/ul/li[2]/a/span').click()

#goodworks
driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[2]/div/div[3]/div/a').click()
#새탭으로이동
driver.switch_to.window(driver.window_handles[-1])
#무료체험신청선택
freee = driver.find_element(By.XPATH,"//*[text()='무료 체험 신청']")
driver.execute_script("arguments[0].scrollIntoView();",freee)
freee.click()

#무료체험신청회사명입력
companynameinput = driver.find_element(By.ID,'companyName')
companynameinput.click()
companynameinput.send_keys(companyname)
#대표자명입력
ceonameinput = driver.find_element(By.ID,'ceoName')
ceonameinput.click()
ceonameinput.send_keys(ceoName)

#사업자유형선택
driver.find_element(By.CSS_SELECTOR,'#businessType > div').click()
option = driver.find_element(By.XPATH,"//*[text()='개인']")
driver.execute_script("arguments[0].scrollIntoView();", option)
option.click()

#직원수선택
driver.find_element(By.CSS_SELECTOR,'#scale > div').click()
option2 = driver.find_element(By.XPATH,"//*[text()='501-999명']")
driver.execute_script("arguments[0].scrollIntoView();", option2)
option2.click()

#담당자명
name = driver.find_element(By.ID,'name')
name.click()
name.send_keys(testname)

#이메일
email = driver.find_element(By.ID,'email')
email.click()
email.send_keys(testemail)

#휴대폰
phonenumber = driver.find_element(By.ID,'mobile')
phonenumber.click()
phonenumber.send_keys(phone)

#담당업무
driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div/div/div/div/div[2]/dl[8]/dd/div/div[2]/button/p/div').click()
workinput = driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div/div/div/div/div[2]/dl[8]/dd/div/div[2]/button/p/div/input')
workinput.click()
va1 = driver.find_element(By.XPATH,"//*[text()='회계']")
driver.execute_script("arguments[0].scrollIntoView();", va1)
va1.click()
workinput.send_keys(testwork)
va2 = driver.find_element(By.XPATH,"//*[text()='인사']")
driver.execute_script("arguments[0].scrollIntoView();", va2)
va2.click()
driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div/div/div/div/div[2]/dl[8]/dd/div/div[2]/div/div[2]/button[2]').click()

#닫기
driver.find_element(By.XPATH,'/html/body/div[6]/button/span').click()
driver.find_element(By.XPATH,'/html/body/div[8]/div/div/div/div/div/div/button[2]').click()
time.sleep(5)
