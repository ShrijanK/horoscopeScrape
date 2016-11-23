import bs4
import requests

def whoreOscope(horoscope):
    if horoscope == "aries":
        res = requests.get("http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=1")
        return res
    elif horoscope == 2:
        res = requests.get("http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=2")
    elif horoscope == 3:
        res = requests.get("http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=3")
    elif horoscope == 4:
        res = requests.get("http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=1")
    elif horoscope == 5:
        res = requests.get("http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=5")
    elif horoscope == 6:
        res = requests.get("http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=6")
    elif horoscope == 7:
        res = requests.get("http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=7")
    elif horoscope == 8:
        res = requests.get("http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=8")
    elif horoscope == 9:
        res = requests.get("http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=9")
    elif horoscope == 10:
        res = requests.get("http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=10")
    elif horoscope == 11:
        res = requests.get("http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=11")
    elif horoscope == 12:
        res = requests.get("http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=12")

    soup = bs4.BeautifulSoup(res.txt, 'html.parser')
    Date = soup.findall("div", {"class":"block-horoscope-date"})
    Horoscope = soup.findAll("div", {"class":"block-horoscope-text f16 120"})
    date_list = []
    horoscope_list = []
    for dates in Date:
        date_list.append(dates.txt)

    for horoscope in Horoscope:
        horoscope_list.append(horoscope.txt)

    print (date_list + horoscope_list)

horoscope = input().lower()

whoreOScope(horoscope)

        
