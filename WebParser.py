strHTML = input()
urls = ""
while(strHTML.find("http")!=-1):
    urls+= strHTML[strHTML.lower().find("http"):strHTML.lower().find(".jpg")+4]
    strHTML=strHTML[strHTML.lower().find(".jpg")+4:]
    strHTML=strHTML[strHTML.lower().find(".jpg")+4:]
    
str1 = """
<div class="img">
  <a href="websiteurl2" target="_blank">
  <img class="centered" alt="image-1" src="websiteurl1" />
<a class="expand" href="websiteurl2"></a>
  </a>
</div>"""

count = 0

while(urls.find("http")!=-1):
    count+=1
    newStr = str1.replace("websiteurl1",urls[urls.find("http"):urls.lower().find(".jpg")+4].replace("s1600","s320"))
    newStr = newStr.replace("websiteurl2",urls[urls.find("http"):urls.lower().find(".jpg")+4].replace("s320","s1600"))
    print newStr.replace("image-1","image-"+str(count))
    urls = urls[urls.lower().find(".jpg")+4:]
