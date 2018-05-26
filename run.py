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
    print(request.headers,end="")
    print("---------------------------------------------------------------\n")
    
    #if post, print post contents
    if(request.method == 'POST'):
        for keys in request.args.keys():
            print(key + ":" + request.args[key])

        for keys in request.form.keys():
            print(key + ":" + request.form[key])


    return "xd"

if(__name__ == '__main__'):
    #runs on default port of 5000
    app.run()

