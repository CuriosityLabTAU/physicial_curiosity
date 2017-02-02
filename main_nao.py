import os
import threading
from naoqi import ALProxy
import time

def intro(subject_id):
    start_working(subject_id)
    time.sleep(60)


def start_working(subject_id):

    subject_id = subject_id

    def worker1():
        os.system('roslaunch my_skeleton_markers markers.launch')
        return

    def worker2():
        os.system('python curious_game/angle_matrix.py')
        return

    def worker3():
        os.system('python curious_game/nao_ros.py')
        return

    def worker4():
        os.system('rosbag record -a -o data/physical_curiosity_open_day_' + subject_id + '.bag')

    def worker5():
        os.system('python curious_game/skeleton_angles.py')

    def worker6():
        os.system('python curious_game/experiment.py '+subject_id)


    t1 = threading.Thread(target=worker1)
    t1.start()
    threading._sleep(0.2)
    t2 = threading.Thread(target=worker2)
    t2.start()
    threading._sleep(0.2)
    t3 = threading.Thread(target=worker3)
    t3.start()
    threading._sleep(0.2)
    t4 = threading.Thread(target=worker4)
    t4.start()
    threading._sleep(0.2)
    t5 = threading.Thread(target=worker5)
    t5.start()
    threading._sleep(0.2)
    t6 = threading.Thread(target=worker6)
    t6.start()



intro("1")
