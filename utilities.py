from bs4 import BeautifulSoup
from bs4.element import Tag

from constants import BASE_URL



def removeParen(tag):

    remove = False
    #print (tag)
    for child in tag.children:

        if (str(child.string).count("(") == 1 and str(child.string).count(")") == 0):
            remove = True

        if (str(child.string).count(")") == 1 and str(child.string).count("(") == 0):
            child.replace_with("")
            remove = False

        if remove == True:
            child.replace_with("")

    return tag


def getLink(text):
    ## first get to the content tag of wikipedia
    soup = BeautifulSoup(text, "html.parser")
    soup = soup.find(id="bodyContent").find(
        id="mw-content-text").findChildren('div', {'class': 'mw-parser-output'})[0]

    ## paragarpsh will be in div or p tags
    soup = soup.findChildren(["div", "p"], recursive=False)

    f = open("debug.txt", "a")

    ## filter this paragrapsh to get normal paragraphs

    tags = [tag for tag in soup if (
            tag.get('id') is None and tag.get('class') is None and tag.get('role') is None)]

    ## loop on each paragraph or div and get first  href we get
    for tag in tags:
        # f.writelines(str(tag.encode("utf8")))
        # f.writelines("\n\n\n")
        # for t in tag.children:
        #     f.writelines(str(t.encode("utf8")))
        #     f.writelines("\n\n\n")
        tag = removeParen(tag)
        # f.writelines("\n\n\n ##################### \n \n \n \n")

        # f.writelines(str(tag.encode("utf8")))
        # f.writelines("\n\n\n")
        # for t in tag.children:
        #     f.writelines(str(t.encode("utf8")))
        #     f.writelines("\n\n\n")

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
            print(a.get("href"))
            return BASE_URL+a.get("href")

    return None
