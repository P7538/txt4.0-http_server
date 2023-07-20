# txt4.0-http_server
Runs as normal python script on the txt 4.0. When started, a http server is creted which can be used to control the txt4.0 with http requests (Can be used to control the txt4.0 from a browser)
GET requests to 'http://192.168.7.2:8000' return the current input data (of both normal and counter inputs).
POST requests are used to configure inputs and outputs, the necessary additional information is send in json format:
{"i" + *index to configure* : 0x0b (for resistance)/ 0x0a(vor Voltage)}: changes the input mode
{"c" + *index to configure* : 0}: Resets counter
{"m" + *index to configure* : *value*} : sets motor to value 
{"o" + *index to configure* : *value*} : sets output to value 
{"s" + *index to configure* : *value*} : sets servo to value 



