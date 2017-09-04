from selenium import webdriver
import re
import reqfun
import os
rawu='http://www.hdwallpapers.in/nature__landscape-desktop-wallpapers/page/%d'
parurl='http://www.hdwallpapers.in/walls/%s-wide.jpg'
def geturl(rpu,page):
    u=rpu%page
    a=webdriver.Firefox()
    a.get(u)
    b=[str(i.find_element_by_tag_name('a').get_attribute('href')) for i in a.find_elements_by_class_name('wall')]
    #b=[re.findall(r'/thumbs/20\d\d/(.+)-\d1\.jpg',i)[0] for i in b]
    b=[re.findall(r'/www\.hdwallpapers\.in/(.+)-wallpaper',i)[0] for i in b]
    a.quit()
    return b
pa=r'C:\Users\huangjy\Pictures\wallpapers\%s.jpg'
def downpapers(u):
    global pa
    for i in u:
        if '%s.jpg'%i in os.listdir(r'C:\Users\huangjy\Pictures\wallpapers'):
            continue
        ii=i
        i=parurl%i
        print(i)
        i=reqfun.myget(i,timeout=180)
        if i and i.status_code==200:
            with open(pa%ii,'wb') as f:
                f.write(i.content)


def getpapers(rpu,page):
    downpapers(geturl(rpu,page))
for i in range(7,63):
    getpapers(rawu,i)
