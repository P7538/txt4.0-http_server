from fischertechnik.controller.Motor import Motor
##from lib.controller import *
import fischertechnik.factories as txt_factory
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver 
HOST = "192.168.7.2"  # txt 4.0 
##HOST  = "127.0.0.1"
PORT = 8000  # Port to listen on (non-privileged ports are > 1023)
inputs = [0x0b, 0x0b, 0x0b, 0x0b,0x0b, 0x0b,0x0b, 0x0b]
input = []
counter  = []
output = []
servo = []
class NewHTTP(BaseHTTPRequestHandler):
    def do_GET(self): 
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*"),
        self.end_headers()
        ##TXT_M_I1_color_sensor.get_voltage()
        ##result = { "i1":str(TXT_M_I1_mini_switch.get_resistance())}
        result = dict()
        for i in range(8): 
            if(inputs[i]==0x0b):
                result.update({ "i"+str(i+1) : str(input[i].get_resistance())})
            else: 
                result.update({ "i"+str(i+1) : str(input[i].get_voltage())})
        for n in range(4): 
            result.update({ "c"+str(n+1) : str(counter[n].get_count())})
        self.wfile.write(bytes(json.dumps(result), "utf-8"))

    def do_POST(self):
        content_len = int(self.headers.get("Content-Length"))
        post_body = self.rfile.read(content_len)
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*"),
        self.end_headers()
        if(str(post_body)[2] == "i"):
            self.wfile.write(self.changein(post_body))
        elif(str(post_body)[2] == "c"):
            counter[int(str(post_body)[3])-1].reset()
            self.wfile.write(bytes("ok", "utf-8"))
        elif(str(post_body)[2] == "o"): 
            self.wfile.write(self.setout(post_body))
        elif(str(post_body)[2] == "m"):
            self.wfile.write(self.setmotor(post_body))
        elif(str(post_body)[2] == "s"):
            self.wfile.write(self.setservo(post_body))
        else:
            self.wfile.write(bytes("undefined", "utf-8"))

    def changein(self, post_body): 
        try:
            val = str(post_body).split('=', 1)[1][:-1]
            if(val == "0x0a"):
                input[int(str(post_body)[3])-1] = txt_factory.input_factory.create_color_sensor(TXT_M, int(str(post_body)[3]))
                inputs[int(str(post_body)[3])-1] = 0x0a
                return bytes("ok", "utf-8")
            elif(val == "0x0b"): 
                input[int(str(post_body)[3])-1] = txt_factory.input_factory.create_photo_resistor(TXT_M, int(str(post_body)[3]))
                inputs[int(str(post_body)[3])-1] = 0x0b       
                return bytes("ok", "utf-8")
            else: 
                return bytes("mode not defined", "utf-8")
        except Exception as e:
            return bytes("error:"+str(e), "utf-8")

    def setout(self, post_body):
        try:
            val = int(str(post_body).split('=', 1)[1][:-1])
            output[int(str(post_body)[3])-1].set_brightness(val)
            return bytes("ok", "utf-8")
        except Exception as e:
            return bytes("error:"+str(e), "utf-8")

    def setmotor(self, post_body): 
        try:
            val = int(str(post_body).split('=', 1)[1][:-1])
            if(val>0):
                output[int(str(post_body)[3])].set_brightness(0)
                output[int(str(post_body)[3])-1].set_brightness(val)
            else: 
                output[int(str(post_body)[3])].set_brightness(val*(-1))
                output[int(str(post_body)[3])-1].set_brightness(0) 
            return bytes("ok", "utf-8")   
        except Exception as e:
            return bytes("error:"+str(e), "utf-8")
        
    def setservo(self, post_body):
        try:
            val = int(str(post_body).split('=', 1)[1][:-1])
            servo[int(str(post_body)[3])-1].set_position(val)
            return bytes("ok", "utf-8")           
        except Exception as e:
            return bytes("error:"+str(e), "utf-8")

server = HTTPServer((HOST, PORT ), NewHTTP) ##server is started 
txt_factory.init()
txt_factory.init_input_factory()
txt_factory.init_motor_factory()
txt_factory.init_counter_factory()
txt_factory.init_usb_factory()
txt_factory.init_camera_factory()
txt_factory.init_output_factory()
txt_factory.init_servomotor_factory()


TXT_M = txt_factory.controller_factory.create_graphical_controller()
TXT_M_I1_mini_switch = txt_factory.input_factory.create_photo_resistor(TXT_M, 1)
input.append(TXT_M_I1_mini_switch)
TXT_M_I2_mini_switch = txt_factory.input_factory.create_photo_resistor(TXT_M, 2)
input.append(TXT_M_I2_mini_switch)
##TXT_M_I2_photo_transistor = txt_factory.input_factory.create_photo_transistor(TXT_M, 2)
##TXT_M_I3_ultrasonic_distance_meter = txt_factory.input_factory.create_ultrasonic_distance_meter(TXT_M, 3)
TXT_M_I3_mini_switch = txt_factory.input_factory.create_photo_resistor(TXT_M, 3)
input.append(TXT_M_I3_mini_switch)
TXT_M_I4_mini_switch = txt_factory.input_factory.create_photo_resistor(TXT_M, 4)
input.append(TXT_M_I4_mini_switch)
TXT_M_I5_mini_switch = txt_factory.input_factory.create_photo_resistor(TXT_M, 5)
input.append(TXT_M_I5_mini_switch)
TXT_M_I6_mini_switch = txt_factory.input_factory.create_photo_resistor(TXT_M, 6)
input.append(TXT_M_I6_mini_switch)
TXT_M_I7_mini_switch = txt_factory.input_factory.create_photo_resistor(TXT_M, 7)
input.append(TXT_M_I7_mini_switch)
TXT_M_I8_mini_switch = txt_factory.input_factory.create_photo_resistor(TXT_M, 8)
input.append(TXT_M_I8_mini_switch)
TXT_M_C1_mini_switch = txt_factory.counter_factory.create_mini_switch_counter(TXT_M, 1)
counter.append(TXT_M_C1_mini_switch)
TXT_M_C2_mini_switch = txt_factory.counter_factory.create_mini_switch_counter(TXT_M, 2)
counter.append(TXT_M_C2_mini_switch)
TXT_M_C3_mini_switch = txt_factory.counter_factory.create_mini_switch_counter(TXT_M, 3)
counter.append(TXT_M_C3_mini_switch)
TXT_M_C4_mini_switch = txt_factory.counter_factory.create_mini_switch_counter(TXT_M, 4)
counter.append(TXT_M_C4_mini_switch)
for x in range (8): 
    output.append(txt_factory.output_factory.create_led(TXT_M,x+1))
for x in range(3):
    servo.append(txt_factory.servomotor_factory.create_servomotor(TXT_M,x+1))

txt_factory.initialized()

server.serve_forever() ##runs infinitely
