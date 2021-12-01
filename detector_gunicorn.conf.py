import sys
sys.path.append(".")
sys.path.append('/home/darknet/AI-Broadcast/')

from darknet import model

# init the detector model
mymodel = model()

def pre_request(worker, rep):
    req.headers.append(('FLASK_MODEL', mymodel)) 

pre_request = pre_request