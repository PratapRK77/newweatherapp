from flask import Flask , render_template, request
import requests


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")


@app.route("/weatherapp", methods = ['POST','GET'])
def grt_weatherdata():
    url ="https://api.openweathermap.org/data/2.5/weather"
    appid="7abb9086938be30f26f351c85713b98b"
    param  = {
        'q': request.form.get("city"),
        'unit' : request.form.get("unit")
    }
    response= requests.get(url ,params = param)
    data = response.json()
    return f"data : {data}"



if __name__ == "__main__":
    app.run(host="0.0.0.0" , port = 5002)
