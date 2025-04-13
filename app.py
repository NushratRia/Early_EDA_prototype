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
    return render_template("merge.html", background_image="background2.jpg")  # Use your next page's image name here

@app.route('/merge2')
def merge2():
    return render_template('merge2.html') 

@app.route('/sort')
def sort():
    return render_template('sort.html') 

@app.route('/sort2')
def sort2():
    return render_template('sort2.html') 

@app.route('/remove')
def remove():
    return render_template('remove.html') 

@app.route('/remove2')
def remove2():
    return render_template('remove2.html') 

@app.route('/missing')
def missing():
    return render_template('missing.html') 

@app.route('/missing2')
def missing2():
    return render_template('missing2.html') 

@app.route('/thanks')
def thanks():
    return render_template('thanks.html') 

if __name__ == "__main__":
    app.run(debug=True)
