#!/usr/bin/env python
import os
import json
from pprint import pprint
import urlparse
import templates
import sys
#print("Content-Type: text/html")
#print("Set-Cookie: logged_in=True")
#print #Extra print ends the line to separate the .html headers from the body.
      #This implies that the first thing you print in CGI in the HTTP header.
#print("hello world")

#params = urlparse.parse_qs(os.environ['QUERY_STRING'])
#print(params)
#print(os.environ['QUERY_STRING'])

#print(os.environ['HTTP_USER_AGENT'])
#userAgent = os.environ['HTTP_USER_AGENT']
#if 'Firefox' in userAgent:
#    print("You're using Firefox")
#elif 'Chrome' in userAgent:
#    print("You're using Chrome")
#elif 'curl' in userAgent:
#    print("You're using curl")
content_length = os.environ['CONTENT_LENGTH']
user = "test"
pswrd = "test"
logged_in = False
cookie = os.environ['HTTP_COOKIE']


if("logged_in" in cookie):
      logged_in = True

#print(os.environ) #POST are not placed into environment variables because it can be unreasonably large. It is placed in standard input instead
elif content_length:
      bytes_to_read = int(content_length)
      content = sys.stdin.read(bytes_to_read)
      params = urlparse.parse_qs(content)
      if(params['username'][0] == user and params['password'][0] == pswrd):
            print("Set-Cookie: logged_in") #You are setting the header but not sending it.
            logged_in = True

print("Content-Type: text/html")
print #End the HTTP header

if not logged_in:
      print(r"""
          <h1> Welcome! </h1>
      
          <form method="POST" action="hello.py">
              <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
              <label> <span>Password:</span> <input type="password" name="password"></label>
      
              <button type="submit"> Login! </button>
          </form>
          """)
      #print(cookie)
else:
      print("This is a secret message for " + user)
      #print(cookie)

#print (json.dumps(dict(os.environ))) #Inspecting all environmental variables in Python. All processes can inherit environ variables
                                    #json.dumps() jsonifies the environ variables
#print(json.dumps(dict(os.environ['Home'])))