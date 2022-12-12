from flask import Flask, render_template,request

import requests
import json

app=Flask(__name__)

#restful API function and by passing these parameters so in route will get these parameters through request.form
#once we get them from request.form will pass them throug  querystring dict
#then will get json syntax of 3 values , will take just the amount and round it 2 decimal places
# def get_currency(from_,to_,amt):
#     url = "https://currency-converter13.p.rapidapi.com/convert"
#     querystring = {"from":from_,"to":to_,"amount":amt}
#     headers = {
#     'x-rapidapi-key': "bbc4e72c95msh764d7107571c9ccp132292jsne000b3620c23",
#     'x-rapidapi-host': "currency-converter13.p.rapidapi.com"
#     }
#     response = requests.request("GET", url, headers=headers, params=querystring).json()
#     print("***********************",response)
#     final_result=round(response["amount"],2)
#     return final_result




# def translat(word,lang):
#     from googletrans import Translator
#     translater=Translator()
#     output=translater.translate(word,dest=lang)
#     print(output)
#     return output.text
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
