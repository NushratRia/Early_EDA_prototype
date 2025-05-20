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

@app.route('/split')
def split():
    return render_template('split.html') 

@app.route('/split2')
def split2():
    return render_template('split2.html')

@app.route('/standard')
def standard():
    return render_template('5_standard.html') 

@app.route('/standard2')
def standard2():
    return render_template('5_standard2.html') 

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

@app.route('/map')
def map():
    return render_template('7_map.html') 

@app.route('/map2')
def map2():
    return render_template('7_map2.html')

@app.route('/open')
def open():
    return render_template('8_open.html')

@app.route('/open2')
def open2():
    return render_template('8_open2.html')

@app.route('/outlier')
def outlier():
    return render_template('9_outlier.html')

@app.route('/outlier2')
def outlier2():
    return render_template('9_outlier2.html')

@app.route('/top')
def top():
    return render_template('10_top.html')

@app.route('/top2')
def top2():
    return render_template('10_top2.html')

@app.route('/pivot')
def pivot():
    return render_template('11_pivot.html')

@app.route('/pivot2')
def pivot2():
    return render_template('11_pivot2.html')

@app.route('/vis')
def vis():
    return render_template('12_vis.html')

@app.route('/vis2')
def vis2():
    return render_template('12_vis2.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html') 

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5001, debug=True)
