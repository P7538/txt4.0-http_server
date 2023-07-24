# txt4.0-http_server
Runs as normal python script on the txt 4.0. When started, a http server is creted which can be used to control the txt4.0 with http requests (Can be used to control the txt4.0 from a browser)<br>
GET requests to 'http://192.168.7.2:8000' return the current input data (of both normal and counter inputs).<br>
POST requests are used to configure inputs and outputs, the necessary additional information is send in json format:<br>
{port : "i" + *index to configure* , val: 0x0b (for resistance)/ 0x0a(vor Voltage)}: changes the input mode<br>
{port: "c" + *index to configure* ,val: 0}: Resets counter<br>
{port: "m" + *index to configure* ,val:*value*} : sets motor to value <br>
{port: "o" + *index to configure* ,val: *value*} : sets output to value <br>
{port: "s" + *index to configure* ,val: *value*} : sets servo to value <br>



