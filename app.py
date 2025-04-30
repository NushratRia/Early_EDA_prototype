from flask import Flask, render_template, jsonify
from fingertip_test import FingertipTracker
import logging

# Configure logging to write to app.log
logging.basicConfig(filename='app.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s: %(message)s')

# Optional: short reference to the logger
logger = logging.getLogger()

app = Flask(__name__)
tracker = FingertipTracker()
tracker.start() 

# @app.route("/")
# def index():
#     return render_template("index.html")

@app.route("/")
def landing():
    return render_template("index.html")


@app.route("/fingertips")
def get_fingertips():
    return {"fingertips": tracker.fingertips}

@app.route("/task")
def page2():
    return render_template("merge.html")

@app.route('/merge2')
def merge2():
    return render_template('merge2.html') 

@app.route('/sort')
def sort():
    return render_template('sort.html') 

@app.route('/sort2')
def sort2():
    return render_template('sort2.html') 

@app.route('/ssort')
def ssort():
    return render_template('ssort.html')
 
@app.route('/ssort2')
def ssort2():
    return render_template('ssort2.html') 

@app.route('/remove')
def remove():
    return render_template('remove.html') 

@app.route('/remove2')
def remove2():
    return render_template('remove2.html') 

@app.route('/rremove')
def rremove():
    return render_template('rremove.html') 

@app.route('/rremove2')
def rremove2():
    return render_template('rremove2.html') 

@app.route('/missing')
def missing():
    return render_template('missing.html') 

@app.route('/missing2')
def missing2():
    return render_template('missing2.html') 

@app.route('/mmissing')
def mmissing():
    return render_template('mmissing.html') 

@app.route('/mmissing2')
def mmissing2():
    return render_template('mmissing2.html') 

@app.route('/thanks')
def thanks():
    return render_template('thanks.html') 

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5001, debug=True)
