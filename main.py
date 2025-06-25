#!/usr/bin/env python3
import rospy
import time
from geometry_msgs.msg import Twist

class MyPath():
    def __init__(self):
        rospy.init_node('MyPath', anonymous=False)
        rospy.on_shutdown(self.shutdown)
        self.cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        rate=100

        r=rospy.Rate(rate)
        t=rospy.get_time()
        move_cmd=Twist()
        while(rospy.get_time()==0):
        	print("Perimene")
        print("Proti kinisi.................")
        while(rospy.get_time()-t<=2):
        	move_cmd.angular.z=0.69*(rospy.get_time()-t)-0.345*pow(rospy.get_time()-t,2)
        	print("Velocity: ",move_cmd.angular.z)
        	self.cmd_vel.publish(move_cmd)
        	r.sleep()

        move_cmd = Twist()
        self.cmd_vel.publish(move_cmd)
        rospy.sleep(1)
        t=rospy.get_time()

        print("Deyteri kinisi.................")
        while((rospy.get_time()-t)<=190):
        	move_cmd.linear.x=0.004088094*((rospy.get_time()-t))-0.000021516*pow((rospy.get_time()-t),2)
        	print("Velocity: ",move_cmd.linear.x)
        	self.cmd_vel.publish(move_cmd)
        	r.sleep()

        move_cmd = Twist()
        self.cmd_vel.publish(move_cmd)
        rospy.sleep(1)
        t=rospy.get_time()

        print("Triti kinisi.................")
        while(rospy.get_time()-t<=5):
        	move_cmd.angular.z=-0.4872*(rospy.get_time()-t)+0.09744*pow(rospy.get_time()-t,2)
        	print("Velocity: ",move_cmd.angular.z)
        	self.cmd_vel.publish(move_cmd)
        	r.sleep()

        move_cmd = Twist()
        self.cmd_vel.publish(move_cmd)
        rospy.sleep(1)
        t=rospy.get_time()

        print("Tetarti kinisi.................")
        while(rospy.get_time()-t<=166):
        	move_cmd.linear.x=0.004790245*(rospy.get_time()-t)-0.000028857*pow(rospy.get_time()-t,2)
        	print("Velocity: ",move_cmd.linear.x)
        	self.cmd_vel.publish(move_cmd)
        	r.sleep()

        move_cmd = Twist()
        self.cmd_vel.publish(move_cmd)
        rospy.sleep(1)
        t=rospy.get_time()

        print("Pempti kinisi.................")
        while(rospy.get_time()-t<=9):
        	move_cmd.angular.z=0.281888889*(rospy.get_time()-t)-0.031320988*pow(rospy.get_time()-t,2)
        	print("Velocity: ",move_cmd.angular.z)
        	self.cmd_vel.publish(move_cmd)
        	r.sleep()

        move_cmd = Twist()
        self.cmd_vel.publish(move_cmd)
        rospy.sleep(1)

    def shutdown(self):
        rospy.loginfo("Stopping the robot...")
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)
if __name__ == '__main__':
    try:
        MyPath()
    except:
        rospy.loginfo("MyPath node terminated.")
