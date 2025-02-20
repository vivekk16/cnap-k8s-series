from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    color = os.getenv("BG_COLOR", "black")  # Default color is white
    return render_template("index.html", color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)