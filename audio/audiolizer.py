
'''
Reading serial data, manipulating it and writing to a serial port

'''

import serial
import time
import os, sys


base_freq = 440 # A sys.argv[3]
avg_val = 1
# read_port = sys.argv[1]
# write_port = sys.argv[2]
#
#
# def serial_data_read(port, baudrate):
#     ser = serial.Serial(port, baudrate)
#
#     while True:
#         yield ser.readline()
#
#     ser.close()
#
#
#
# def serial_data_write(port, baudrate, data):
#
#     ser = serial.Serial(port, baudrate)
#
#     while 1:
#         ser.write(data)
#
#     ser.close()


def send_to_pd(msg, port):
    os.system("echo '" + msg + "' | pdsend %d" % port)
    print "message sent"


def main(val):
    # New value
    new_val = base_freq + 2 ** abs(avg_val - val)

    # write it out - change serial port
    # serial_data_write('/dev/ttyACM0', 9600, new_val)
    msg = '1 ' + str(new_val) + ';'
    send_to_pd(msg, 3000)


if __name__== "__main__":
    main(50)
