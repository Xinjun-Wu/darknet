
import sys, os
# add the cutomized script 
sys.path.append('/home/darknet/AI-Broadcast/')

from darknet import model
from flask import Flask, request
from flask.views import MethodView
# from PIL import Image
import io

# init the detector model
mymodel = model()
# wrap this script with flask
app = Flask(__name__)

# cutomize view for app
class Prediction(MethodView):
    def post(self):
        if request.method == "POST":
            image = request.get_data()
            img = image
            # mymodel = request.environ['HTTP_FLASK_MODEL']
            r = mymodel.predict(img)
            # print(r)
            return r
        else:
            print("-------abdec-------------")
            return "THE model has not run!"

app.add_url_rule("/detectorservice/", view_func=Prediction.as_view('detector'),
                    methods = ["POST","GET"])

# please in workspace root /home/darknet/ run with below command
# $ gunicorn --threads 8 -b0.0.0.0:12711 detector_service:app