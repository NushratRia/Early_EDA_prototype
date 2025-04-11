from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")

@app.route("/")
def landing():
    return render_template("index.html")
# @app.route("/")
# def index():
#     return render_template("index.html", background_image="background.jpg")

@app.route("/task")
def page2():
    return render_template("sort.html", background_image="background2.jpg")  # Use your next page's image name here

if __name__ == "__main__":
    app.run(debug=True)
