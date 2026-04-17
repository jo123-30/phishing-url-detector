from flask import Flask, render_template, request
import os

app = Flask(__name__)

def check_url(url):
    score = 0

    if "@" in url:
        score += 25
    if len(url) > 75:
        score += 25
    if "https" not in url:
        score += 25
    if any(word in url for word in ["login", "verify", "bank"]):
        score += 25

    if score >= 75:
        return "Phishing", score
    elif score >= 50:
        return "Suspicious", score
    else:
        return "Safe", score


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    score = 0

    if request.method == "POST":
        url = request.form["url"]
        result, score = check_url(url)

    return render_template("index.html", result=result, score=score)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
