# Import some necessary libraries.
from __future__ import division
import socket, requests
from collections import namedtuple
from pprint import pprint as pp
from HTMLParser import HTMLParser
from chatterbotapi import ChatterBotFactory, ChatterBotType
from subprocess import call
from functools import wraps
from timeout import timeout

#define variables
commands={}
 
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

OpInfo = namedtuple('OpInfo', 'prec assoc')
L, R = 'Left Right'.split()
 
ops = {
 '^': OpInfo(prec=4, assoc=R),
 '*': OpInfo(prec=3, assoc=L),
 '/': OpInfo(prec=3, assoc=L),
 '+': OpInfo(prec=2, assoc=L),
 '-': OpInfo(prec=2, assoc=L),
 '(': OpInfo(prec=9, assoc=L),
 ')': OpInfo(prec=0, assoc=L),
 }
 
NUM, LPAREN, RPAREN = 'NUMBER ( )'.split()
 
 
def get_input(inp = None):
    'Inputs an expression and returns list of (TOKENTYPE, tokenvalue)'
 
    if inp is None:
        inp = input('expression: ')
    tokens = inp.strip().split()
    tokenvals = []
    for token in tokens:
        if token in ops:
            tokenvals.append((token, ops[token]))
        #elif token in (LPAREN, RPAREN):
        #    tokenvals.append((token, token))
        else:    
            tokenvals.append((NUM, token))
    return tokenvals

def shunting(tokenvals):
    outq, stack = [], []
    table = ['TOKEN,ACTION,RPN OUTPUT,OP STACK,NOTES'.split(',')]
    for token, val in tokenvals:
        note = action = ''
        if token is NUM:
            action = 'Add number to output'
            outq.append(val)
            table.append( (val, action, ' '.join(outq), ' '.join(s[0] for s in stack), note) )
        elif token in ops:
            t1, (p1, a1) = token, val
            v = t1
            note = 'Pop ops from stack to output' 
            while stack:
                t2, (p2, a2) = stack[-1]
                if (a1 == L and p1 <= p2) or (a1 == R and p1 < p2):
                    if t1 != RPAREN:
                        if t2 != LPAREN:
                            stack.pop()
                            action = '(Pop op)'
                            outq.append(t2)
                        else:    
                            break
                    else:        
                        if t2 != LPAREN:
                            stack.pop()
                            action = '(Pop op)'
                            outq.append(t2)
                        else:    
                            stack.pop()
                            action = '(Pop & discard "(")'
                            table.append( (v, action, ' '.join(outq), ' '.join(s[0] for s in stack), note) )
                            break
                    table.append( (v, action, ' '.join(outq), ' '.join(s[0] for s in stack), note) )
                    v = note = ''
                else:
                    note = ''
                    break
                note = '' 
            note = '' 
            if t1 != RPAREN:
                stack.append((token, val))
                action = 'Push op token to stack'
            else:
                action = 'Discard ")"'
            table.append( (v, action, ' '.join(outq), ' '.join(s[0] for s in stack), note) )
    note = 'Drain stack to output'
    while stack:
        v = ''
        t2, (p2, a2) = stack[-1]
        action = '(Pop op)'
        stack.pop()
        outq.append(t2)
        table.append( (v, action, ' '.join(outq), ' '.join(s[0] for s in stack), note) )
        v = note = ''
    return table

def op_pow(stack):
    b = stack.pop(); a = stack.pop()
    stack.append( a ** b )
def op_mul(stack):
    b = stack.pop(); a = stack.pop()
    stack.append( a * b )
def op_div(stack):
    b = stack.pop(); a = stack.pop()
    stack.append( a / b )
def op_add(stack):
    b = stack.pop(); a = stack.pop()
    stack.append( a + b )
def op_sub(stack):
    b = stack.pop(); a = stack.pop()
    stack.append( a - b )
def op_num(stack, num):
    stack.append( num )
 
ops2 = {
 '^': op_pow,
 '*': op_mul,
 '/': op_div,
 '+': op_add,
 '-': op_sub,
 }
 
def get_input2(inp = None):
    'Inputs an expression and returns list of tokens'
 
    if inp is None:
        inp = input('expression: ')
    tokens = inp.strip().split()
    return tokens

def rpn_calc(tokens):
    stack = []
    table = ['TOKEN,ACTION,STACK'.split(',')]
    for token in tokens:
        if token in ops2:
            action = 'Apply op to top of stack'
            ops2[token](stack)
            table.append( (token, action, ' '.join(str(s) for s in stack)) )
        else:
            action = 'Push num onto top of stack'
            op_num(stack, eval(token))
            table.append( (token, action, ' '.join(str(s) for s in stack)) )
    return table

#Commands for the bot
proxies = {
  "https": "tssproxy.broward.k12.fl.us:8888"
}
commands = {"math":lambda x:rpn_calc(get_input2(shunting(get_input(' '.join(x)))[-1][2]))[-1][2],
            "google":lambda x:strip_tags(HTMLParser().unescape(requests.get('https://ajax.googleapis.com/ajax/services/search/web?v=1.0&rsz=1&userip=24.53.222.246&q='+'%20'.join(x),proxies=proxies).json()["responseData"]['results'][0]['content'].encode('ascii','ignore'))).replace("\n"," ")
            +" Read more: "+strip_tags(HTMLParser().unescape(requests.get('https://ajax.googleapis.com/ajax/services/search/web?v=1.0&rsz=1&userip=24.53.222.246&q='+'%20'.join(x),proxies=proxies).json()["responseData"]['results'][0]['url'].encode('ascii','ignore'))).replace("\n"," "),
            "FTC":lambda x:strip_tags(HTMLParser().unescape(requests.get('https://ajax.googleapis.com/ajax/services/search/web?v=1.0&rsz=1&userip=24.53.222.246&q=ftc%20forum%20'+'%20'.join(x),proxies=proxies).json()["responseData"]['results'][0]['content'].encode('ascii','ignore'))).replace("\n"," ")
            +" Read more: "+strip_tags(HTMLParser().unescape(requests.get('https://ajax.googleapis.com/ajax/services/search/web?v=1.0&rsz=1&userip=24.53.222.246&q=ftc%20forum%20'+'%20'.join(x),proxies=proxies).json()["responseData"]['results'][0]['url'].encode('ascii','ignore'))).replace("\n"," "),
            "youtube":lambda x:youtubeDownload(x),
            "help":lambda x:', '.join([c for c in commands]),
            "whois":lambda x:strip_tags(HTMLParser().unescape(requests.get('https://ajax.googleapis.com/ajax/services/search/web?v=1.0&rsz=1&userip=24.53.222.246&q=ftc%20team%20'+'%20'.join(x),proxies=proxies).json()["responseData"]['results'][0]['content'].encode('ascii','ignore'))).replace("\n"," ")
            +" Read more: "+strip_tags(HTMLParser().unescape(requests.get('https://ajax.googleapis.com/ajax/services/search/web?v=1.0&rsz=1&userip=24.53.222.246&q=ftc%20team%20'+'%20'.join(x),proxies=proxies).json()["responseData"]['results'][0]['url'].encode('ascii','ignore'))).replace("\n"," ")
            +(" The Yellow Alliance: http://theyellowalliance.net/teams/view/"+x[0],"")[not is_number(x[0])],
            "GLRobot":lambda x:strip_tags(bot2session.think(' '.join(x)))
            }
# Some basic variables used to configure the bot
server = "irc.freenode.net" # Server
channel = "#GreasedLightning" # Channel
botnick = "GLRobot" # Your bots nick
factory = ChatterBotFactory() #Setup chatterbot
bot2 = factory.create(ChatterBotType.PANDORABOTS, 'b0dafd24ee35a477')
bot2session = bot2.create_session()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def youtubeDownload(url):
  sendmsg(channel,"Downloading...")
  try:
      result = call('youtube-dl -o "I:\My_Files\Youtube\%(title)s.%(ext)s" '+url[0],shell=False)
      if not result:
          return "Done! 24.51.212.246:2302"
      else:
          return "Failed to download"
  except:
      return "Command Execution Failed"
    
def runCommand(stack):
  try:
    ircsock.send("PRIVMSG "+ channel +" :"+commands[stack.pop(0)](stack)+"\n")
  except:
    print "Command Exception!"
    print stack

def ping(): # This is our first function! It will respond to server Pings.
  ircsock.send("PONG :pingis\n")

def sendmsg(chan , msg): # This is the send message function, it simply sends messages to the channel.
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n")

def joinchan(chan): # This function is used to join channels.
  ircsock.send("JOIN "+ chan +"\n")

def hello(): # This function responds to a user that inputs "Hello Mybot"
  ircsock.send("PRIVMSG "+ channel +" :Hello!\n")

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :This bot is a result of a tutoral covered on http://shellium.org/wiki.\n") # user authentication
ircsock.send("NICK "+ botnick +"\n") # here we actually assign the nick to the bot

joinchan(channel) # Join the channel using the functions we previously defined

while 1: # Be careful with these! it might send you to an infinite loop
  ircmsg = ircsock.recv(2048) # receive data from the server
  ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
  print(ircmsg) # Here we print what's coming from the server

  if ircmsg.find(":Hello "+ botnick) != -1: # If we can find "Hello Mybot" it will call the function hello()
    hello()

  if "#GreasedLightning :" in ircmsg:
    cmd = ircmsg[ircmsg.find("#GreasedLightning :")+19:]
    if cmd.startswith("!"):
      stack = cmd[1:].split(" ")
      print stack
      runCommand(stack)
    
  if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
    ping()
  
