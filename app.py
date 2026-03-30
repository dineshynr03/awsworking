from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "version 2: auto deployed - boht thak gaya  Hello from Docker + GitHub Actions!--dinesh 1.0 dev"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
