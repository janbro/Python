from subprocess import call
urlfile = "youtubeurl.txt"
def readfile():
    line = ''
    for x in open(urlfile, 'r').readlines():
        line += x
        return line
url = readfile()
call('youtube-dl -o "C:\Users\Alejandro\Documents\GitHub\Python\IRC Bot\youtube\%(title)s.%(ext)s" '+url,shell=False)
