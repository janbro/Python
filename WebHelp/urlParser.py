strHTML = input()
while(strHTML.find("http")!=-1):
    print strHTML[strHTML.lower().find("http"):strHTML.lower().find(".jpg")+4]
    strHTML=strHTML[strHTML.lower().find(".jpg")+4:]
    strHTML=strHTML[strHTML.lower().find(".jpg")+4:]
