import os
import time
from flask import Flask, jsonify


app = Flask(__name__)

#-----------------------------------
#  The following code is invoked when the path portion of the URL matches 
#         /determineTime/42/determineTime/yyyy
#   "yyyy" is passed as the value of the input parameter.
#
@app.route('/determineTime/<remainderOfUrl>')
def determineTime(remainderOfUrl):
    timezone = int(remainderOfUrl)
    #time utc and current
    utime = time.gmtime()
    ctime = time.localtime()
    #find current time off input
    utc_hour = int(time.strftime("%H", utime))
    utc_min = time.strftime("%M", utime)
    c_hour = int(time.strftime("%H", ctime))
    c_min = time.strftime("%M" , ctime)
    c_hour = (utc_hour + timezone)
    #check if am or pm
    if (c_hour < 0):
        c_hour = c_hour + 24
    if (c_hour >= 24):
        c_hour = c_hour - 24  
    localt = str(c_hour)+":"+c_min
    currentTime = str(c_hour)+":"+utc_min
    #check bounded timezones
    if(timezone <= 12 and timezone >= -12):
        if (timezone == -6):
            mess2 = ("The Current Auburn, Alabama Time is: " + str(currentTime))
            return mess2
        mess1 = (str(currentTime))
        return mess1
    else: 
        mess4 = ("Error")
        return mess4 
    
port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
