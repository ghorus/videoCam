# import eventlet
# import eventlet.wsgi
# eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
import cv2
from flask import Flask, render_template,Response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

@app.route("/")
def home():
    return render_template('home.html')

f = ""
def generate_frames():
    camera=cv2.VideoCapture(-1)
    while True:
        #read camera frame
        success,frame=camera.read()
        f = frame
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpeg',frame)
            frame = buffer.tobytes()
        yield(b'--frame\r\n' 
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route("/video")
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run(debug=True)

@app.route("/capture")
def capture():
    cv2.imwrite('webcam.jpeg',f)