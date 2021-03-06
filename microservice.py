import os
import time
from flask import Flask, jsonify


app = Flask(__name__)

#-----------------------------------
#  The following code is invoked when the path portion of the URL matches 
#         /determineTime/42/determineTime/yyyy
#   "yyyy" is passed as the value of the input parameter.
#
@app.route('/watson/<remainderOfUrl>')
def determineTime(remainderOfUrl):
    inp = str(remainderOfUrl)
    return inp
    
port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
