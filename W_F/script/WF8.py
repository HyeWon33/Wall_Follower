#!/home/won/.pyenv/versions/rospy3/bin/python

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
        print(Scan_Value)

        def stop(self, scan):
            if scan.ranges[0] < 0.3 and scan.ranges[0] > 0.1:
                print(scan.ranges[0], "stop")
                turtle_vel.linear.x = 0
                turtle_vel.angular.z = math.pi / 2

        if Scan_Value

        if Scan_Value >= 0.18 and Scan_Value <= 0.22:
            turtle_vel.linear.x = 0.15
            print("go")
            stop(self,scan)
            self.publisher.publish(turtle_vel)

        elif Scan_Value > 0.22:
            if (Scan_Value_Top > Scan_Value_Bottom):
                turtle_vel.angular.z = -(math.pi / 2)
                turtle_vel.linear.x = 0.14
                print("R R")
                stop(self, scan)
                self.publisher.publish(turtle_vel)
            elif (Scan_Value_Top == Scan_Value_Bottom):
                turtle_vel.linear.x = 0.15
                self.publisher.publish(turtle_vel)
                stop(self, scan)
                print("R G")
            else:
                turtle_vel.angular.z = (math.pi / 9)
                self.publisher.publish(turtle_vel)
                turtle_vel.linear.x = 0.08
                print("R L")
                stop(self, scan)
                self.publisher.publish(turtle_vel)

            # elif Scan_Value < 1.8:
        else:
            if (Scan_Value_Top > Scan_Value_Bottom):
                turtle_vel.angular.z = -(math.pi / 9)
                turtle_vel.linear.x = 0.08
                print("L R")
                stop(self, scan)
                self.publisher.publish(turtle_vel)
            elif (Scan_Value_Top == Scan_Value_Bottom):
                turtle_vel.linear.x = 0.15
                print("L G")
                stop(self, scan)
                self.publisher.publish(turtle_vel)
            else:
                turtle_vel.angular.z = (math.pi / 2)
                turtle_vel.linear.x = 0.14
                print("L L")
                stop(self, scan)
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


turtle_vel = Twist()
Scan_Value = average(scan.ranges[225:315])
Scan_Value_Top = average(scan.ranges[270:315])
Scan_Value_Bottom = average(scan.ranges[225:270])
print(Scan_Value)


if Scan_Value >= 0.18 and Scan_Value <= 0.22:
    turtle_vel.linear.x = 0.15
    print("go")
    self.stop(self, scan)
    self.publisher.publish(turtle_vel)

elif Scan_Value > 0.22:
    if (Scan_Value_Top > Scan_Value_Bottom):
        turtle_vel.angular.z = -(math.pi / 2)
        turtle_vel.linear.x = 0.14
        print("R R")
        turtle_vel = self.stop(self, scan)
        self.publisher.publish(turtle_vel)
    elif (Scan_Value_Top == Scan_Value_Bottom):
        turtle_vel.linear.x = 0.15
        self.publisher.publish(turtle_vel)
        stop(self, scan)
        print("R G")
    else:
        turtle_vel.angular.z = (math.pi / 9)
        self.publisher.publish(turtle_vel)
        turtle_vel.linear.x = 0.08
        print("R L")
        stop(self, scan)
        self.publisher.publish(turtle_vel)

    # elif Scan_Value < 1.8:
else:
    if (Scan_Value_Top > Scan_Value_Bottom):
        turtle_vel.angular.z = -(math.pi / 9)
        turtle_vel.linear.x = 0.08
        print("L R")
        stop(self, scan)
        self.publisher.publish(turtle_vel)
    elif (Scan_Value_Top == Scan_Value_Bottom):
        turtle_vel.linear.x = 0.15
        print("L G")
        stop(self, scan)
        self.publisher.publish(turtle_vel)
    else:
        turtle_vel.angular.z = (math.pi / 2)
        turtle_vel.linear.x = 0.14
        print("L L")
        stop(self, scan)
        self.publisher.publish(turtle_vel)
