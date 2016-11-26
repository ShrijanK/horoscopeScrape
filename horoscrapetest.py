import bs4
import requests

def whoreOscope():
    res = requests.get("http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=" + horoscope_number)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    h1 = soup.find("div",{"class":"container"}).find("div",{"class":"main-container"})
    print (h1)
    """h2 = h1.find("div",{"class":"main-container"})
    h3 = h2.find("div",{"class":"row"})
    h4 = h3.find("div",{"class":"page-2col-col1"})
    h5 = h4.find("div",{"class":"col1-1col-col1"})
    h6 = h5.find("div",{"class":"block-horoscope-container"})
    h7 = h6.find("div",{"class":"block-horoscope-right-container"})
    h8 = h7.find("div",{"class":"block-horoscope-text f16"})
    horoscope_list = []
    for horoscope in h8:
        horoscope_list.append(horoscope.txt)

    print (horoscope_list)"""
  

print ("1. for Aries")
print ("2. for Taurus")




horoscope_number = str(input())
whoreOscope()
