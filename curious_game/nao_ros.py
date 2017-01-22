import rospy
from std_msgs.msg import String
from naoqi import ALProxy
import sys
import almath
import time


class NaoNode():
    def __init__(self):
        self.robotIP = '192.168.0.100'
        self.port = 9559

        try:
            self.motionProxy = ALProxy("ALMotion", self.robotIP, self.port)
            self.audioProxy = ALProxy("ALAudioPlayer", self.robotIP, self.port)
            self.postureProxy = ALProxy("ALRobotPosture", self.robotIP, self.port)
        except Exception,e:
            print "Could not create proxy to ALMotion"
            print "Error was: ",e
            sys.exit(1)

        # Get the Robot Configuration
        self.robotConfig = self.motionProxy.getRobotConfig()
        self.motionProxy.setStiffnesses("Body", 1.0)
        self.postureProxy.goToPosture("StandInit", 0.5)
        # self.motionProxy.rest()


    def start(self):
        #init a listener to kinect and
        rospy.init_node('nao_listener')
        rospy.Subscriber('nao_commands', String, self.callback)
        rospy.spin()

    def callback(self, data):
        # data = 'name1, name2;target1, target2;pMaxSpeedFraction'
        data_str = data.data
        info = data_str.split(';')
        pNames = info[0].split(',')
        pTargetAngles = [float(x) for x in info[1].split(',')]
        print pTargetAngles
        # pTargetAngles = [ x * almath.TO_RAD for x in pTargetAngles]             # Convert to radians

        pMaxSpeedFraction = float(info[2])

        print(pNames, pTargetAngles, pMaxSpeedFraction)
        while time.gmtime()[5]%2 == 0:
            self.motionProxy.angleInterpolationWithSpeed(pNames, pTargetAngles, pMaxSpeedFraction)


nao = NaoNode()
nao.start()