from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__, static_folder="Static", template_folder="templates")
app.secret_key = "global-ai-students-demo"


@app.route("/")
def home():
    return render_template("index.html")


@app.post("/contact")
def contact():
    # Demo endpoint for the contact form.
    flash("Thank you! Your message has been received.", "success")
    return redirect(url_for("home") + "#contact")


@app.post("/newsletter")
def newsletter():
    # Demo endpoint for newsletter subscription.
    flash("You have been subscribed successfully.", "success")
    return redirect(url_for("home") + "#footer")


if __name__ == "__main__":
    app.run(debug=True)
