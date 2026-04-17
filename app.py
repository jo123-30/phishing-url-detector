from flask import Flask, render_template, request

app = Flask(__name__)

def check_url(url):
    score = 0

    if "@" in url:
        score += 1
    if len(url) > 75:
        score += 1
    if "https" not in url:
        score += 1
    if any(word in url for word in ["login", "verify", "bank"]):
        score += 1

    if score >= 3:
        return "Phishing"
    elif score == 2:
        return "Suspicious"
    else:
        return "Safe"


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        url = request.form["url"]
        result = check_url(url)
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
