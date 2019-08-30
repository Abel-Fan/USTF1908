from flask import Flask,request,jsonify
import requests
requests.urllib3.disable_warnings()
app = Flask(__name__)

@app.route("/photo",methods=['POST'])
def photo():
    data = dict(request.form)
    res = requests.post("https://118.190.150.35:5000/api/photo",data=data,verify=False)
    rep = res.json()
    return jsonify(rep)

@app.route("/check",methods=['POST'])
def check():
    data = dict(request.form)
    res = requests.post("https://118.190.150.35:5000/api/check",data=data,verify=False)
    rep = res.json()
    return jsonify(rep)

if __name__ == "__main__":
    app.run(debug=True)