from dotenv import load_dotenv
from flask import Flask, render_template, request

from sender import send_email

app = Flask(__name__)
load_dotenv()


@app.route("/", methods=["GET"])
def get_form():
    return render_template("send_email.html")


@app.route("/", methods=["POST"])
def post_form():
    email = request.values.get("email")
    if send_email(email, "Test letter", "test text",
                  ["1.png", "pdfdoc.pdf", "text.txt"]):
        return f"Letter send successfully from to the address {email}"
    return f"An error occurred while sending an email to {email}"


if __name__ == '__main__':
    app.run()
