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
    if response.ok:
        print(data)  # Add this line to print data to the console
        return render_template("result.html", 
                                   temperature=data['main']['temp'],
                                   min_temperature=data['main']['temp_min'],
                                   max_temperature=data['main']['temp_max'],
                                   humidity=data['main']['humidity'],
                                   clouds=data['clouds']['all'])
    else:
        print(data)  # Add this line to print data to the console
        return render_template("result.html", error="Error fetching weather data. Please check your input and try again.")


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5001)