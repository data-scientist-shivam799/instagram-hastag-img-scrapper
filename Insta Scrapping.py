import wget
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os

driver=webdriver.Chrome(executable_path='E:\RPA\chromedriver.exe')
driver.get('https://www.instagram.com/')
driver.maximize_window()

userName=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='username']")))
passWord=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']")))
userName.clear()
passWord.clear()
userName.send_keys('sage_of_s1x_paths')
passWord.send_keys('Shivam799')
logIn=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))).click()
notNow=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()
notNow2=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()
# driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()

searchBox = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))
searchBox.clear()
keyWord='jisoo'
search='https://www.instagram.com/explore/tags/'+str(keyWord)
driver.get(search)
driver.execute_script("window.scrollTo(0,4000);")
images=driver.find_elements_by_tag_name("img")
images=[image.get_attribute('src') for image in images]
print(images)
path=os.getcwd()
path=os.path.join(path,keyWord[0:]+"s")
os.mkdir(path)
counter=0
for i in images:
    save_as=os.path.join(path,keyWord[1:]+str(counter)+'.jpg')
    wget.download(i, save_as)
    counter+=1
driver.close()