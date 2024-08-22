from flask import Flask
import sys
from housing.logger import logging 
from housing.exception import HousingException

app = Flask(__name__)

@app.route("/", methods=['GET',"POST"])
def index():
    try:
        raise Exception("We are testng custom exception")
    except Exception as e:
        #housing =   HousingException(e,sys)
        raise HousingException(e,sys) from e
        logging.info(housing.error_message)
        logging.info("We are testing logging module")  #for logging perpose
    return "Starting Machine Learning Project"

if __name__=="__main__":
    app.run(debug=True)
