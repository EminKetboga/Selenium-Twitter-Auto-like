from selenium import webdriver
import giris_bilgileri
import time

browser = webdriver.Firefox()

browser.get("https://twitter.com/")

time.sleep(4)

giris_yap = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div")

giris_yap.click()

time.sleep(3)

username = browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input")

username.send_keys(giris_bilgileri.username)

time.sleep(3)
ileri = browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div")

ileri.click()
time.sleep(4)
password = browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div[1]/input")

password.send_keys(giris_bilgileri.password)
time.sleep(2)

ileri2 = browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div")

ileri2.click()

time.sleep(5)
arama_yeri = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")

arama_yeri.send_keys("#python")
arama_yeri.send_keys('\ue007')
time.sleep(2)
likebutton = browser.find_elements_by_css_selector("[data-testid=like]")
for like in likebutton:
    try:
        like.click()
        time.sleep(0.4)
    except Exception:
        print("bir hata oluştu...")
time.sleep(10)
lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(2)

    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    time.sleep(2)
    likebutton = browser.find_elements_by_css_selector("[data-testid=like]")
    for like in likebutton:
        try:
            like.click()
            time.sleep(1)
        except Exception:
            print("bir hata oluştu")
    if lastCount == lenOfPage:
        match=True

time.sleep(3)

browser.close()