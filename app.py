from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def home():
    if request.method=="POST":
        user_weight_in_kg = request.form.get("weight_input")
        user_height_in_m = request.form.get("height_input")
        if len(user_weight_in_kg)>0 and len(user_height_in_m)>0:
            bmi = str(float(user_weight_in_kg)/(float(user_height_in_m)*float(user_height_in_m)))
            bmi_num = float(bmi)
            bmi_status = ""
            if bmi_num<18.5:
                bmi_status = "Underweight"
            elif bmi_num>=18.5 and bmi_num<25:
                bmi_status = "Normal"
            elif bmi_num>=25 and bmi_num<30:
                bmi_status = "Overweight"
            elif bmi_num>=30:
                bmi_status = "Obese"
            return render_template("index.html",currentBMI=bmi[0:5],statusBMI=bmi_status)
        else:
            return render_template("index.html",currentBMI="Invalid data",statusBMI="")
    else:
        return render_template("index.html")

@app.route('/<dynamicPage>')
def open_dynamicpage(dynamicPage):
    return f"<h1>Error 404<br>Page not found</h1>"

if __name__=="__main__":
    app.run(debug=True)
