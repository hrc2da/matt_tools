#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState


class republishJointState:
	def __init__(self):
		rospy.init_node("joint_state_republisher",anonymous=True)
		self.republisher = rospy.Publisher("joint_states", JointState, queue_size=10)
		rospy.Subscriber("j2s7s300_driver/out/joint_state", JointState, self.republish)
		rospy.spin()
	def republish(self,data):
		self.republisher.publish(data)

if __name__ == '__main__':
	try:
		rp = republishJointState()
	except rospy.ROSInterruptException:
		pass
