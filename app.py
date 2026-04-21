import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hello cloud"

if __name__ == "__main__":
    # Render साठी Port आणि Host सेट करणे गरजेचे आहे
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)