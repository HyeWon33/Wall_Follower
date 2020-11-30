#!/usr/bin/env python

import math
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class SelfDrive:
    def __init__(self, publisher):
        self.publisher = publisher
    
    def lds_callback(self, scan):
        turtle_vel = Twist()
        Scan_Value = average(scan.ranges[225:315])
        Scan_Value_Top = average(scan.ranges[270:315])
        Scan_Value_Bottom = average(scan.ranges[225:270])
        Scan_Value_f = average(scan.ranges[5:-5])
       # print(Scan_Value_f)
        print(Scan_Value)
        
        #if Scan_Value_f != 1.25:
         #   if Scan_Value_f <= 1.25:
           #     print('ww')
          #      turtle_vel.linear.x = 0
            #    turtle_vel.angular.z = (math.pi / 4)
            #print('ffff')
            #turtle_vel.linear.x = 0.15


        if Scan_Value >= 0.15 and Scan_Value <= 0.2:
            turtle_vel.linear.x = 0.15
            print("go")
            if scan.ranges[0] >= 0.12:
                turtel_vel.linear.x = 0

        elif Scan_Value > 0.2:
           # turtle_vel.angular.z = -(math.pi / 2.5)
           # turtle_vel.linear.x = 0.14 
           # print("Right go")
            
            if(Scan_Value_Top > Scan_Value_Bottom):
                turtle_vel.angular.z = -(math.pi / 2)
                turtle_vel.linear.x = 0.14 
                print("R R") 

                
            else: 
                turtle_vel.angular.z = (math.pi / 9) 
                turtle_vel.linear.x = 0.08
                print("R L")
        elif Scan_Value < 1.5:
            turtle_vel.angular.z = math.pi / 6 
            turtle_vel.linear.x = 0.12
            print("Left go")

            if(Scan_Value_Top > Scan_Value_Bottom):
                print("Scan_Top,Bot : ",Scan_Value_Top, Scan_Value_Bottom)
                turtle_vel.angular.z = -(math.pi / 6)
                turtle_vel.linear.x = 0.14 
                print("L R")
            else:
                print("Scan_Top,Bot : ",Scan_Value_Top, Scan_Value_Bottom)
                turtle_vel.angular.z = -(math.pi / 6)
                turtle_vel.linear.x = 0.14 
                print("L B R")

        self.publisher.publish(turtle_vel)

def average(list):
    return (sum(list) / len(list))


def main():
    rospy.init_node('self_drive')
    publisher = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    driver = SelfDrive(publisher)
    subscriber = rospy.Subscriber('scan', LaserScan,
                                  lambda scan: driver.lds_callback(scan))
    rospy.spin()

if __name__ == "__main__":
    main()

