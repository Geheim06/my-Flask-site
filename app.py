from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=("GET", "POST"))
def home():
    message= ""
    if request.method == "POST":
        name = request.form["name"]
        message = f"Иди на хуй!, {name}!"

    return render_template("index.html", message=message)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=("GET", "POST"))
def contact():
    message= ""
    if request.method == "POST":
        name = request.form["name"]
        message = f"ПОШЕЛ НА ХУЙ!, {name}!"
    return render_template("contact.html", message=message)
if __name__ == "__main__":
 app.run(host="0.0.0.0", port=5000) (debug=True)
