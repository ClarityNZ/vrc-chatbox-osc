# Sending messages via OSC
 The VRChat chatbox listens on the OSC address `/chatbox/input` and accepts 2 parameters  
`s`: The message you want to send in string format  
`b`: A boolean representing whether to send the message automatically or not, if null or false the message will be typed out for the user but will not be sent without confirmation, otherwise the message will be sent automatically, useful for automated messages such as a clock.  
Attached is an example script which will send the message "Hello World!"  
# Requirements  
[python-osc](https://github.com/attwad/python-osc/) 

