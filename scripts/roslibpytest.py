from __future__ import print_function
import roslibpy
import time
ros = roslibpy.Ros(host="localhost",port=9090)
topic = roslibpy.Topic(ros,"/test","std_msgs/String")

def callback():
	topic.advertise()
	print("publishing data")
	while True:
		topic.publish(roslibpy.Message({"data":"hithere"}))
		#time.sleep(1)

ros.on_ready(callback)

ros.run_forever()
