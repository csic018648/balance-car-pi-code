import sys
#from pynput import keyboard
import RPi.GPIO as GPIO
import smbus
import time
from time import sleep
from DFRobot_RaspberryPi_DC_Motor import DFRobot_DC_Motor_IIC as Board
import json

GPIO.setmode(GPIO.BCM)

PIDButton = 23
offsetBTADD = 24
offsetBTDEE = 25

GPIO.setup(PIDButton,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(offsetBTADD,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(offsetBTDEE,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

class Gyro(object):

    def __init__(self, addr):
        self.addr = addr
        self.i2c = smbus.SMBus(1)
        
    def get_acc(self):
        try:
            self.raw_acc_x = self.i2c.read_i2c_block_data(self.addr, 0x34, 2)
            self.raw_acc_y = self.i2c.read_i2c_block_data(self.addr, 0x35, 2)
            self.raw_acc_z = self.i2c.read_i2c_block_data(self.addr, 0x36, 2)
        except IOError:
            print("ReadError: gyro_acc")
            return (0, 0, 0)
        else:
            self.k_acc = 16 

            self.acc_x = (self.raw_acc_x[1] << 8 | self.raw_acc_x[0]) / 32768 * self.k_acc
            self.acc_y = (self.raw_acc_y[1] << 8 | self.raw_acc_y[0]) / 32768 * self.k_acc
            self.acc_z = (self.raw_acc_z[1] << 8 | self.raw_acc_z[0]) / 32768 * self.k_acc

            if self.acc_x >= self.k_acc:
                self.acc_x -= 2 * self.k_acc 
        
            if self.acc_y >= self.k_acc:
               self.acc_y -= 2 * self.k_acc
                
            if self.acc_z >= self.k_acc:
                self.acc_z -= 2 * self.k_acc
            return (self.acc_y)
            #return (self.acc_x, self.acc_y, self.acc_z)
                    
    def get_gyro(self):
        try:
            self.raw_gyro_x = self.i2c.read_i2c_block_data(self.addr, 0x37, 2)
            self.raw_gyro_y = self.i2c.read_i2c_block_data(self.addr, 0x38, 2)
            self.raw_gyro_z = self.i2c.read_i2c_block_data(self.addr, 0x39, 2)
        except IOError:
            print("ReadError: gyro_gyro")
            return (0, 0, 0)
        else:
            self.k_gyro = 2000

            self.gyro_x = (self.raw_gyro_x[1] << 8 | self.raw_gyro_x[0]) / 32768 * self.k_gyro
            self.gyro_y = (self.raw_gyro_y[1] << 8 | self.raw_gyro_y[0]) / 32768 * self.k_gyro
            self.gyro_z = (self.raw_gyro_z[1] << 8 | self.raw_gyro_z[0]) / 32768 * self.k_gyro

            if self.gyro_x >= self.k_gyro:
                self.gyro_x -= 2 * self.k_gyro
        
            if self.gyro_y >= self.k_gyro:
               self.gyro_y -= 2 * self.k_gyro
                
            if self.gyro_z >= self.k_gyro:
                self.gyro_z -= 2 * self.k_gyro
            
            return (self.gyro_y)
            #return (self.gyro_x, self.gyro_y, self.gyro_z)
        
    def get_angle(self):
        try:
            self.raw_angle_x = self.i2c.read_i2c_block_data(self.addr, 0x3d, 2)
            self.raw_angle_y = self.i2c.read_i2c_block_data(self.addr, 0x3e, 2)
            self.raw_angle_z = self.i2c.read_i2c_block_data(self.addr, 0x3f, 2)
        except IOError:
            print("ReadError: gyro_angle")
            return (0, 0, 0)
        else:
            self.k_angle = 180

            self.angle_x = (self.raw_angle_x[1] << 8 | self.raw_angle_x[0]) / 32768 * self.k_angle
            self.angle_y = (self.raw_angle_y[1] << 8 | self.raw_angle_y[0]) / 32768 * self.k_angle
            self.angle_z = (self.raw_angle_z[1] << 8 | self.raw_angle_z[0]) / 32768 * self.k_angle

            if self.angle_x >= self.k_angle:
                self.angle_x -= 2 * self.k_angle
        
            if self.angle_y >= self.k_angle:
                self.angle_y -= 2 * self.k_angle
                
            if self.angle_z >= self.k_angle:
                self.angle_z -= 2 * self.k_angle

            return (self.angle_y)
            #return (self.angle_x, self.angle_y, self.angle_z)
        
def main():
    head_gyro = Gyro(0x50)
    board = Board(1, 0x10)
    board.set_encoder_enable(board.ALL)                 # Set selected DC motor encoder enable
    board.set_encoder_reduction_ratio(board.ALL, 30)    # Set selected DC motor encoder reduction ratio, test motor reduction ratio is 43.8
    board.set_moter_pwm_frequency(1000)   # Set DC motor pwm frequency to 1000HZ
    address = board.detecte()
    print("Board list conform:")
    print(address)
    while board.begin() != board.STA_OK:    # Board begin and check board status
         print_board_status()
         print("board begin faild")
         time.sleep(2)
    print("board begin success")
    
    offseterror = 0.0
    
    kp = 0
    ki = 0
    kd = 0

    Lmin = 0    #M1
    Rmin = 0    #M2
    LminR = 0    #M1
    RminR = 0    #M2
    
    lastError = 0.000000000000
    lastError_1 = 0.000000000000
    lastError_2 = 0.000000000000
    integral = 0.0
    flag = 0
    
    try:
        while(True):
            button_state = GPIO.input(PIDButton)  #offsetBTDEE
            button_stateADD = GPIO.input(offsetBTADD)
            button_stateDEE = GPIO.input(offsetBTDEE)
            if button_state==1:
                sleep(0.5)
                if flag==0:
                     flag=1
                else:
                     flag=0
                
            if flag==0:
                integral = 0.0
                board.motor_stop(board.ALL)
                continue
               
            angle = float(repr(head_gyro.get_angle()))+offseterror
            gyro = float(repr(head_gyro.get_gyro()))
            

            if angle > 80 or angle < -80:
                integral = 0.0
                flag = 0
                board.motor_stop(board.ALL)
                continue
            
            error = angle
            proportional = kp * error
            integral += ki * error
            derivative = kd * (error - lastError_1)
            PID = int((proportional + integral + derivative))  # 
            if PID > 50:
               PID = 50
            if PID < -50:
               PID = -50
            
            print("Angle:" + repr(head_gyro.get_angle()) + " gyro:" +  repr(head_gyro.get_gyro())+ " offset angle:" + str(PID) + "offseterror:" + str(offseterror) + "\n")
            
            if PID > 0:
              board.motor_movement([board.M1], board.CCW, Rmin + abs(PID))    # DC motor 1 movement, orientation clockwise
              board.motor_movement([board.M2], board.CW, Lmin + abs(PID))   # DC motor 2 movement, orientation count-clockwise
            else:
              board.motor_movement([board.M1], board.CW, RminR + abs(PID))    # DC motor 1 movement, orientation clockwise
              board.motor_movement([board.M2], board.CCW, LminR + abs(PID))   # DC motor 2 movement, orientation count-clockwise
            
            lastError_2 = lastError_1
            lastError_1 = error
    except KeyboardInterrupt:
         board.motor_stop(board.ALL)
main()
