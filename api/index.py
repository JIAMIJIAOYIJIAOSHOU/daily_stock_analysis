from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>AI Stock Analyzer Running</h1>"

# Vercel 会自动识别 app 对象
