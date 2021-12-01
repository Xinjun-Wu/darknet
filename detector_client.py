import requests

test_img = b"/home/data/yolotestdata/testimage/test8.jpg"

r = requests.post("http://0.0.0.0:12711/detectorservice",data = test_img)

print (test_img, r.text)