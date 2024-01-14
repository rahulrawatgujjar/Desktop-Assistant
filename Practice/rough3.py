# import pywhatkit
# import webbrowser as web
import selenium
# # pywhatkit.search("code with harry")
# pywhatkit.playonyt("nissan song")


# def search(topic: str) -> None:
#     """Searches About the Topic on Google"""

#     link = f"https://www.google.com/search?q={topic}"
#     web.open(link)
    
from selenium import webdriver
driver=webdriver.Chrome(r"C:\Users\might\Downloads\chromedriver")
# topic="mathma Gandhi"
# driver.get(f"https://www.google.com/search?q={topic}")
# button=driver.find_element_by_link_text("News")
# button.click()
# a="capital rahul capital rawat gujjar"
# a.replace("rawat","")
# print(a)
# while "capital" in a:
#     ind=int(a.index("capital")+8)
#     last=ind
#     while True:
#         if last==len(a):
#             break
#         elif a[last]==" ":
#             break
#         last+=1
#     r=a[ind:last]
#     a=a.replace(f"capital {r}",f"{r}".capitalize())
# print(a)
# # print(len(a))
# import pywhatkit
# a="kabaddi"
# pywhatkit.info(a,2)
import time
driver.get("https://www.flipkart.com")
time.sleep(2)
key=driver.find_element_by_id("Search for products, brands, and more")
key.send_keys("poco x2")