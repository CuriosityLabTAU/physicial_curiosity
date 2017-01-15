import rospy
from std_msgs.msg import String
from skeleton_markers.msg import Skeleton
import numpy as np


class SkeletonAngles():
    def __init__(self):
        self.pub = rospy.Publisher ('skeleton_angles', String)
        self.names = ['head', 'neck', 'torso', 'left_shoulder', 'left_elbow', 'left_hand',
                      'right_shoulder', 'right_elbow', 'right_hand',
                      'left_hip', 'left_knee', 'left_foot', 'right_hip', 'right_knee', 'right_foot']
        self.positions = {}
        for name in self.names:
            self.positions[name] = {'x': None, 'y': None, 'z': None}

        self.skeleton_angles = np.zeros([8])

    def start(self):
        #init a listener to kinect and
        rospy.init_node('skeleton_angle')
        rospy.Subscriber("skeleton", Skeleton, self.callback)
        rospy.spin()

    def callback(self, data):
        positions = data.position
        for name in self.names:
            self.positions[name]['x'] = positions[self.names.index(name)].x
            self.positions[name]['y'] = positions[self.names.index(name)].y
            self.positions[name]['z'] = positions[self.names.index(name)].z

        print(self.positions)

        # Omer + Matan
        # takes left_shoulder, left_elbow, left_hand --> 4 angles
        self.skeleton_angles[0:4] = np.zeros([4])

        # takes right_shoulder, right_elbow, right_hand --> 4 angles
        self.skeleton_angles[4:8] = np.zeros([4])

        pub_str = ''
        for s in self.skeleton_angles:
            pub_str += str(s) + ','
        self.pub.publish(pub_str[:-1])

skeleton_angles = SkeletonAngles()
skeleton_angles.start()