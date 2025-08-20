from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "BMI CALCULATOR"

@app.route('/<randompage>')
def open_randompage(randompage):
    return "Page not available!"

if __name__=="__main__":

    app.run(debug=True)
