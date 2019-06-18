import requests
import time
import sys
from constants import *
from utilities import getLink
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
            
            
        
                



if __name__ == '__main__':
    main()
