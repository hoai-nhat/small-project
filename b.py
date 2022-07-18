
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


#dắng nhập
browser = webdriver.Chrome(executable_path="./chromedriver.exe")
browser.get("https://ee88.club/home/#/")

log = browser.find_element_by_class_name("el-button.login.el-button--default").click()
login = browser.find_element_by_class_name("el-input__inner")
login.send_keys("hoainhat")
pas = browser.find_element_by_xpath ("/html/body/div[1]/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/form/div[2]/div/div/input")
sleep(1)
pas.send_keys("Vietnam12345")
sleep(3)
pas.send_keys(Keys.ENTER)
sleep(5)

#p2
p1 = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[1]/div[4]/div/div[1]/button/i").click()
sleep(1)
p2 = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[1]/div[1]/div[2]/div/div/div[3]/div/ul/li/div[1]/span/img").click()
sleep(3)
p3 = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[8]/span[2]").click()
sleep(3)
p4 = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div/span/span/i").click()
sleep(5)
p5 = browser.find_element_by_xpath("/html/body/div[6]/div[1]")
sleep(5)
p8 = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[2]/button[4]/span").click()
sleep(5)
p9 = browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[3]").click
sleep(100)
browser.close()

os.mkdir('photo2')
i =1
for index,img_link in enumerate(links):
    if i<=10:
        img_data = rq.get(img_link).content
        with open('photo/'+str(index+1)+'.jpg','wb+') as f:
            f.write(img_data)
        i+=1
    else:
        f.close()
        break   

