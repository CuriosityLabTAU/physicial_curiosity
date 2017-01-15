# from curious_game.nao_ros import NaoNode

import os
import threading


subject_id = '1'

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


t1 = threading.Thread(target=worker1)
t1.start()
t2 = threading.Thread(target=worker2)
t2.start()
t3 = threading.Thread(target=worker3)
t3.start()
t4 = threading.Thread(target=worker4)
t4.start()
t5 = threading.Thread(target=worker5)
t5.start()

print('here')

