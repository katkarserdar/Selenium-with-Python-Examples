from selenium import webdriver

import time

import logininfo

browser = webdriver.Firefox()

browser.get("https://www.instagram.com/")

time.sleep(2)
#name özelliği ile giriş yapıyoruz.
username = browser.find_element_by_name("username")

password = browser.find_element_by_name("password")

username.send_keys(logininfo.username)
password.send_keys(logininfo.password)

time.sleep(2)

loginButton = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]")

loginButton.click()

time.sleep(5)

mainMenu = browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[1]/a/div/div/img")

mainMenu.click()

time.sleep(6)

profileLogin1 = browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span")

profileLogin1.click()

time.sleep(1)

profileLogin2 = browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div")

profileLogin2.click()

time.sleep(1)

followersButton = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")

followersButton.click()

time.sleep(1)

jscommand = """
followers = document.querySelector(".isgrP");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage=followers.scrollHeight;
return lenOfPage;

"""
lenOfPage = browser.execute_script(jscommand)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True
time.sleep(1)

followersList = []

followers = browser.find_element_by_css_selector(".FPmhX .notranslate  ._0imsa ")


for follower in followers:
    followersList.append(follower.text)
    
with open("followers.txt","w",encoding = "UTF-8") as file:
    for follower in followersList:
        file.write(follower + "\n")
        



time.sleep(10)
browser.close()















