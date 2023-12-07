from streamlit_webrtc import webrtc_streamer,RTCConfiguration
from flask import Flask, render_template
import av
import cv2
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


class VideoProcessor:
    def recv(self,frame):
        frm = frame.to_ndarray(format="bgr24")
        return av.VideoFrame.from_ndarray(frm,format='bgr24')
webrtc_streamer(key="key",video_processor_factory=VideoProcessor,rtc_configuration=RTCConfiguration(
    {"iceServers":[{"urls":["stun:stun.l.google.com:19302"]}]}))

@app.route("/")
def home():
    return render_template('home.html')
