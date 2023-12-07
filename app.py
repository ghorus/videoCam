from streamlit_webrtc import webrtc_streamer
from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

webrtc_streamer(key="key")

@app.route("/")
def home():
    return render_template('home.html')
