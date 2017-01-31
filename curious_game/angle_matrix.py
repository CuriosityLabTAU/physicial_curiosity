import rospy
from std_msgs.msg import String
import numpy as np
import random


class AngleMatrix:

    def __init__(self):

        self.matrices = []
        self.matrices.append(np.eye(8))
        self.matrices.append(np.eye(8))
        self.matrices.append(np.eye(8))

        self.matrix = random.choice(self.matrices)
        print(self.matrix, type(self.matrix))
        self.skeleton_angles = np.zeros([8])
        self.robot_angles = np.zeros([8])

        self.pub = rospy.Publisher ('nao_commands', String)
        self.log = rospy.Publisher ('experiment_log', String)

        self.exp_running = False

    def start(self):
        #init a listener to kinect angles
        rospy.init_node('angle_matrix')
        rospy.Subscriber("skeleton_angles", String, self.callback)
        rospy.spin()

    def callback(self, data):
        if not self.exp_running:
            self.exp_running = True
            self.log.publish(str(self.matrix))

        self.skeleton_angles = np.array([float(x) for x in data.data.split(',')])

        self.calculate_robot_angles()

        self.transmit_robot_angles()

    def calculate_robot_angles(self):
        self.robot_angles = np.dot(self.matrix, self.skeleton_angles)
        # safety!
        # Matan: take angles from website. don't allow more than max-2 degrees.
        self.robot_angles[0] = np.maximum(self.robot_angles[0],-2.0850)
        self.robot_angles[0] = np.minimum(self.robot_angles[0], 2.0850)

        self.robot_angles[1] = np.maximum(self.robot_angles[1],-0.3140)
        self.robot_angles[1] = np.minimum(self.robot_angles[1], 1.3260)

        self.robot_angles[2] = np.maximum(self.robot_angles[2],-2.0850)
        self.robot_angles[2] = np.minimum(self.robot_angles[2], 2.0850)

        self.robot_angles[3] = np.maximum(self.robot_angles[3],-1.5440)
        self.robot_angles[3] = np.minimum(self.robot_angles[3],-0.0340)

        self.robot_angles[4] = np.maximum(self.robot_angles[4],-2.0850)
        self.robot_angles[4] = np.minimum(self.robot_angles[4], 2.0850)

        self.robot_angles[5] = np.maximum(self.robot_angles[5],-1.3260)
        self.robot_angles[5] = np.minimum(self.robot_angles[5], 0.3140)

        self.robot_angles[6] = np.maximum(self.robot_angles[6],-2.0850)
        self.robot_angles[6] = np.minimum(self.robot_angles[6], 2.0850)

        self.robot_angles[7] = np.maximum(self.robot_angles[7],0.0340)
        self.robot_angles[7] = np.minimum(self.robot_angles[7],1.5440)

    def transmit_robot_angles(self):
        pNames = ['LShoulderPitch', 'LShoulderRoll', 'LElbowYaw', 'LElbowRoll',
                  'RShoulderPitch', 'RShoulderRoll', 'RElbowYaw', 'RElbowRoll']

        robot_str = ''
        for name in pNames:
            robot_str += name + ','
        robot_str = robot_str[:-1] + ';'

        for ang in self.robot_angles:
            robot_str += str(ang) + ','
        robot_str = robot_str[:-1] + ';'
        robot_str += '0.2'
        self.pub.publish(robot_str)
        print('*************** angle_matrix ************ published: ', robot_str)


angle_matrix = AngleMatrix()
angle_matrix.start()