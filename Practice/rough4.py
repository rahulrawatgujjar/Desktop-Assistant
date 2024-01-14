# import mouse
# import pyautogui as pg
# from pywhatkit.core import core, exceptions, log 
# # mouse.DOWN
# pg.click(core.WIDTH/2,core.HEIGHT/2)
# # pg.press("enter")
# # pg.press("")



# # importing the module
# from englisttohindi.englisttohindi import EngtoHindi
 
# # message to be translated
# message = "Yes, I am geeks"
 
# # creating a EngtoHindi() object
# res = EngtoHindi(message)
 
# # displaying the translation
# print(res.convert)

from bs4 import BeautifulSoup
import requests

res=requests.get("https://www.google.com/search?q=translate to hindi")
soup=BeautifulSoup(res.text,"html.parser")
print(soup)













































