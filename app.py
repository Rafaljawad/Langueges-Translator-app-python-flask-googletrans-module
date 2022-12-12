from flask import Flask, render_template,request

import requests
import json

app=Flask(__name__)

def translat(word,source,destination):
    from googletrans import Translator
    translater=Translator()
    output=translater.translate(word,src=source,dest=destination)
    print("********************************",output)
    return output.text
@app.route("/")
def home():
    to_="--SELECT--"
    from_="--SELECT--"
    return render_template("index.html",to_=to_,from_=from_)
@app.route('/translate',methods=['POST','GET'])
def translate_word():
    word=request.form['text']
    to_=request.form['translate-to']
    from_=request.form['translate-from']
    # res=translat(word,from_,to_)
    #try for if true and all the form sections has been selected so implement them
    try:
        res=translat(word,from_,to_)
    #exception for if we leave the select or textarea empty, will get an error 
    except Exception as e:
            return render_template("error.html",data=e)
    return render_template('index.html',res=res,word=word,from_=from_,to_=to_)


if(__name__)=="__main__":
    app.run(debug=True)
