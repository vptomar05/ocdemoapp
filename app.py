import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello this page has been build using S2I feature of OpenShift and we are updating it for testing application!"
    return "Hello this page has been build using S2I feature of OpenShift and we are updating it for testing application by master Asif sir!"

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=8080)
