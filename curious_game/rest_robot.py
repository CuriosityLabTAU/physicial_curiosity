from naoqi import ALProxy

robotIP = '192.168.0.104'
port = 9559
motionProxy = ALProxy("ALMotion", robotIP, port)
motionProxy.rest()