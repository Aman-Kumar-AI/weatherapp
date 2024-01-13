import requests
from flask import Flask, request, render_template

app=Flask(__name__)
@app.route("/")
def weather_app():
    return render_template("index.html")
@app.route("/weatherapp",methods=["GET","POST"])
def weather_at():
    url= "https://api.openweathermap.org/data/2.5/weather"
    params={'q':request.form.get("city"),
        'appid':request.form.get('appid'),
        'units':request.form.get('units')}
    response=requests.get(url,params=params)
    data=response.json()
    return f"data: {data}"


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5001)