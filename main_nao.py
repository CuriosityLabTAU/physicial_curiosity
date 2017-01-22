import os
import threading
from naoqi import ALProxy
import time

def intro(subject_id):
    robotIP = '192.168.0.100'
    port = 9559
    tts = ALProxy("ALTextToSpeech", robotIP, port)
    tts.say("Hello, let me wake up")
    time.sleep(15)
    tts.say("lest start")
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



intro("1")