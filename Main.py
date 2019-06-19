import requests
import urllib.request
import time
import sys
from bs4 import BeautifulSoup
from bs4.element import Tag
import re

##### error messages #########

ERR_ARG = "Error in arguments argumnets must be  scriptname.py url"
ERR_OUT = "page has no outgoing links"
ERR_LOOP = " we have stucked in a loop"
ERR_INF = " trails out"
ERR_NET = " Network error"
SUCC=" we have reached philosophy"

##### pre Defined links 
PHILO_LINK = "https://en.wikipedia.org/wiki/Philosophy"
BASE_URL = 'https://en.wikipedia.org'

#####
##### number of trials to stop after it the crawling  
##### only in case if the path is too long to terminate the algorithm  ( rarly excuted ) 
TIME_OUT = 50


'''
    To remove tags between () in parant tag

    Args:
        arg (tag): The arg is the input tag 

    return:
        tag elemnt after modification
'''
def removeParen(tag):

    remove =False
    for child in tag.children:
        if (str(child.string).count("(") > str(child.string).count(")")):
            remove =True

        if (str(child.string).count(")") >  str(child.string).count("(")):
            child.replace_with("")
            remove =False


        if remove == True:
            child.replace_with("")


    return tag


'''
    To get the fist outgoing link in wikipedia paragraph
    Args:
        arg (text): body or data of request on specific link

    return:
        string ---> the specificed outgoinglink
'''

def getLink(text):
    ## first get to the content tag of wikipedia
    soup = BeautifulSoup(text, "html.parser")
    soup = soup.find(id="bodyContent").find(
        id="mw-content-text").findChildren('div', {'class': 'mw-parser-output'})[0]

    ## paragarpsh will be in div or p tags
    soup = soup.findChildren(["div", "p"], recursive=False)

    ## filter this paragrapsh to get normal paragraphs

    tags = [tag for tag in soup if (
            tag.get('id') is None and tag.get('class') is None and tag.get('role') is None)]

    ## loop on each paragraph or div and get first  href we get
    for tag in tags:

        tag = removeParen(tag)


        hrefs = tag.findChildren(['a'], href=True, recursive=False)
        for a in hrefs:
            #print (a)
            try:
                ##### to check that the text is italic
                for t in a.children:
                    if t.name == "i":
                        raise Exception()
            except Exception:
                continue
            
            if a.get("class") == "external text":
                continue

            link=a.get("href")
            
            if re.match(r"/wiki/.+", link, flags=0):  # case of the operand @XRn
                if link.find("redlink=1") == -1 :
                    print(link)
                    return BASE_URL+link
                print("RED LINK"+link)
            

    return None


'''
    Main function of the script
    crawling the wikipedia website untill we find the philosophy page or 
    there is a loop or
    or we ended at a page with no outgoing link

    arg:
    command line parameters the link of wikipedai article.


    return:
    doesn't return anything but only print a message indicate the if we get to philosopgy page or not 
    and also print the pages we visit.
    
'''
def main():

    if len(sys.argv) != 2:

        print(ERR_ARG)
        return

    chain = []
    link = sys.argv[1]
    url = link
    count =0
    while (True):
        chain.append(url)
        try:
            response = requests.get(url)
            if response.ok == True:
                count=count+1
                link = getLink(response.text)
                if link == None :
                    print(ERR_OUT)
                    return
                elif link in chain:
                    print (ERR_LOOP)
                    return
                elif count >= TIME_OUT:
                    print(ERR_INF)
                    return 
                elif link == PHILO_LINK:
                    print(SUCC)
                    return 
                url = link
                time.sleep(0.5)
            else:
                print (ERR_NET)
                return 
        except requests.exceptions.ConnectionError:
            print (ERR_NET)
            return
                
            
        
                


if __name__ == '__main__':
    main()
