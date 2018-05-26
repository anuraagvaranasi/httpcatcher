#!/usr/bin/python3
#simple flask app to catch requests 
#and print out information about it

from flask import Flask, request


app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
@app.route('/<url>',methods=['GET','POST'])
def home(url=""):
    #ignore favicon.ico
    if(url == "favicon.ico"):
        return "fuckoff"

    print("\n---------------------------------------------------------------")
    print("URL: " + url)
    print("Request method: " + request.method)
    print("")
    print(request.headers,end="")
    
    if(len(request.cookies) > 0):
        print("Cookies:")
    for key in request.cookies.keys():
        print("    " + key + ":" + request.args[key])
    
    if(len(request.args) > 0):
        print("Arguments:")
    for key in request.args.keys():
        print("    " + key + ":" + request.args[key])
   
   
   #if post, print post contents
    if(request.method == 'POST'):

        if(len(request.form) > 0):
            print("Form Contents:")
        for key in request.form.keys():
            print("    " + key + ":" + request.form[key])

    print("---------------------------------------------------------------\n")

    return "xd"

if(__name__ == '__main__'):
    #runs on default port of 5000
    app.run()

