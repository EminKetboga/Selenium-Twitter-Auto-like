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

arama_yeri.send_keys("#bilişim")
arama_yeri.send_keys('\ue007')

time.sleep(5)

tweetler = set()
elements = browser.find_elements_by_css_selector(".css-901oao.r-18jsvk2.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0")
time.sleep(4)
for element in elements:
    tweetler.add(element.text)

#Alttaki Kodun Anlamı sayfanın sonuna kadar scroll yapıp alttaki sayfa yüklendiğinde tekrar en alta scroll yapması ve scroll özelliği yapılmayıncada döngüden çıkması
lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    elements = browser.find_elements_by_css_selector(".css-901oao.r-18jsvk2.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0")
    time.sleep(2)
    for element in elements:
        tweetler.add(element.text)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True

time.sleep(3)

tweetssayısı = 1




with open("#tweetler.txt","w",encoding= "UTF-8") as file:
    for i in tweetler:

        file.write(str(tweetssayısı) + ".\n" + i + "\n")
        file.write("**************************\n")
        tweetssayısı += 1

time.sleep(2)

browser.close()
