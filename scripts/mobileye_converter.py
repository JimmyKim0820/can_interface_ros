#!/usr/bin/env python
import rospy
import can
import time
import sys
import threading
from can_interface.msg import can_std
from can_interface.msg import Mobileye

'''
function of specific can_ID
Refer to mobileye.xlss

'''

def func_0x669(msg_m):
    data_mobileye.LeftLane_Confidence = msg_m.data[0] & 0x03
    data_mobileye.LeftLane_LDW_Available = (msg_m.data[0] & 0x04)/4
    data_mobileye.LeftLane_Type = (msg_m.data[0] & 0xF0) / 16
    Temp1 = (msg_m.data[2] * 0x10) + (msg_m.data[1] & 0xF0) / 0x10
    if Temp1 & 0x800:
        data_mobileye.LeftLane_Distance = (0xFFF - Temp1 + 0X01) * 0.02
    else:
        data_mobileye.LeftLane_Distance = - Temp1 * 0.02
    data_mobileye.RightLane_Confidence = msg_m.data[5] & 0x03
    data_mobileye.RightLane_LDW_Available = (msg_m.data[5] & 0x04) / 4
    data_mobileye.RightLane_Type = (msg_m.data[5] & 0xF0) / 16
    Temp2 = (msg_m.data[7] * 0x10) + (msg_m.data[6] & 0xF0) / 0x10
    if Temp2 & 0x800:
        data_mobileye.RightLane_Distance = (0x0FFF - Temp2 + 0X01) * 0.02
    else:
        data_mobileye.RightLane_Distance = - Temp2 * 0.02

def func_0x700(msg_m):
    data_mobileye.HW_Valid = msg_m.data[2] & 0x01
    data_mobileye.HW_Measurement = (msg_m.data[2] & 0xFE) / 2 * 0.1
    data_mobileye.Error_ON = 1 - (msg_m.data[3] & 0x01)
    data_mobileye.Error_code = msg_m.data[3] & 0xFE / 2
    data_mobileye.LDW_ON = 1 - msg_m.data[4] & 0x01
    data_mobileye.LDW_Left = (msg_m.data[4] & 0x02) / 2
    data_mobileye.LDW_Right = (msg_m.data[4] & 0x04) / 4
    data_mobileye.Change_LeftLane = (msg_m.data[4] & 0x10) / 16
    data_mobileye.Change_RightLane = (msg_m.data[4] & 0x20) / 32
    data_mobileye.FCW_ON = (msg_m.data[4] & 0x08) / 8
    data_mobileye.Peds_FCW = (msg_m.data[5] & 0x02) / 2
    data_mobileye.Peds_DZ = (msg_m.data[5] & 0x04) / 4
    data_mobileye.TSR_En = (msg_m.data[5] & 0x80) / 128
    data_mobileye.HW_Level = msg_m.data[7] & 0x03

def func_0x720_0x726(msg_m):  # TSR Messange
    i = msg_m.id - 0x720
    data_mobileye.Sign_Type[i] = msg_m.data[0]
    data_mobileye.S_Sign_Type[i] = msg_m.data[1]
    data_mobileye.Sign_X[i] = msg_m.data[2] * 0.5
    Temp1 = msg_m.data[3] & 0x7F
    if Temp1 & 0x40:
        data_mobileye.Sign_Y[i] = (0x7F - Temp1 + 0x01) * 0.5
    else:
        data_mobileye.Sign_Y[i] = -Temp1 * 0.5
    Temp2 = msg_m.data[4] & 0x3F
    if Temp2 & 0x20:
        data_mobileye.Sign_Z[i] = -(0x3F - Temp2 + 0x01) * 0.5
    else:
        data_mobileye.Sign_Z[i] = Temp2 * 0.5
    data_mobileye.Filter_Type[i] = msg_m.data[5]

def func_0x727(msg_m):  # TSR CAN Messange
    data_mobileye.Sign[0] = msg_m.data[0]
    data_mobileye.Sign[1] = msg_m.data[2]
    data_mobileye.Sign[2] = msg_m.data[4]
    data_mobileye.Sign[3] = msg_m.data[6]
    data_mobileye.S_Sign[0] = msg_m.data[1]
    data_mobileye.S_Sign[1] = msg_m.data[3]
    data_mobileye.S_Sign[2] = msg_m.data[5]
    data_mobileye.S_Sign[3] = msg_m.data[7]

def func_0x737(msg_m):
    Temp1 = msg_m.data[1]*0x100 + msg_m.data[0]
    if Temp1 & 0x8000:
        data_mobileye.Lane_Curvature = (~Temp1 + 1) * 3.81 * 1e-6
    else:
        data_mobileye.Lane_Curvature = Temp1 * 3.81 * 1e-6
    Temp2 = (msg_m.data[3] & 0x0F) * 0x100 + msg_m.data[2]
    if Temp2 & 0x800:
        data_mobileye.Lane_Head = (~Temp2 + 1) * 0.0005
    else:
        data_mobileye.Lane_Head = Temp2 * 0.0005
    data_mobileye.CA = (msg_m.data[3] & 0x10) / 16
    data_mobileye.Yaw = (msg_m.data[5] * 0x100 + msg_m.data[4] - 0X7FFF) / 1024
    data_mobileye.Pitch = (msg_m.data[7] * 0x100 + msg_m.data[6] - 0X7FFF) / 1024 / 512

def func_0x760(msg_m): # Car Info
    data_mobileye.Signal_Brake = msg_m.data[0] & 0x01
    data_mobileye.Signal_Left = (msg_m.data[0] & 0x02) / 2
    data_mobileye.Signal_Right = (msg_m.data[0] & 0x04) / 4
    data_mobileye.Wiper = (msg_m.data[0] & 0x08) / 8
    data_mobileye.Beam_Low = (msg_m.data[0] & 0x10) / 16
    data_mobileye.Beam_High = (msg_m.data[0] & 0x20) / 32
    data_mobileye.Speed = msg_m.data[2]

''' callback function to progress data subscribed.
    If there is any ID in func_dictionary,
    appropriate function is going to run '''
def callback(msg_m):
    func = {
        int("669", 16): func_0x669,
        int("700", 16): func_0x700,
        int("727", 16): func_0x727,
        int("737", 16): func_0x737,
        int("760", 16): func_0x760,
        int("720", 16): func_0x720_0x726,
        int("721", 16): func_0x720_0x726,
        int("722", 16): func_0x720_0x726,
        int("723", 16): func_0x720_0x726,
        int("724", 16): func_0x720_0x726,
        int("725", 16): func_0x720_0x726,
        int("726", 16): func_0x720_0x726
    }
    data_mobileye.msg_sub_cnt = msg_m.count
    if msg_m.id in func:
        func[msg_m.id](msg_m)
'''Function for publish. Use threading to match exact frequency'''
def pub():
    while not rospy.is_shutdown():
        data_mobileye.msg_pub_cnt += 1
        pubcan.publish(data_mobileye)
        time.sleep(0.05) #20Hz

#mobileye_status = rospy.get_param("/mobileye_status")
mobileye_status = 1
if mobileye_status == 1:
    data_mobileye = Mobileye()
    rospy.init_node('mobileye_can_converter', anonymous=True)
    sub = rospy.Subscriber('msg_m', can_std, callback)
    pubcan = rospy.Publisher('mobileye_can', Mobileye, queue_size=20)
    my_thread = threading.Thread(target=pub())


