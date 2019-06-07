from datetime import datetime

from config import Source
from config import Config
from fastcampus.dees2.module.models import Bithumb
import requests

# from utils.slack import send_message
import json
import os


class ParserBithumb:
    def __init__(self):
        self.model = Bithumb
        self.url = Source.BITHUMB_URI
        self.currency = ["BTC", "ETH"]

    def get_response(self, params):
        try:
            response = requests.get(self.url, params)
            return response

        except requests.exceptions.ConnectionError as e:
            print (e)
            # send_message("#data-monitoring", "Connection Failed!")
            return "Connection Failed!"

    def parse(self, response, currency):
        result = response.json()["data"]
        price = result["closing_price"]
        volume = result["units_traded"]
        self.model = Bithumb(datetime.utcnow(), price, volume, currency)
        return self.model

    def save( self,response, currency):
        
        result = response.json()["data"]
        date = result["date"]

        # root path
        #fullpath = Config.ROOT_RAW_PATH
        fullpath = os.path.expanduser('~')        
        fullpath += Config.ROOT_RAW_PATH
        # print(fullpath)

        # file path
        filepath = self.model.__tablename__ + "/" + datetime.now().strftime('%Y/%m/%d')
            
        for folder in filepath.split("/"):
            fullpath += "/" + folder
            # print(fullpath)
            # print (os.path.isdir(fullpath))
            if not os.path.isdir(fullpath):
                os.mkdir(fullpath)
                print("make folder")
       
        # file name
        filename = currency + "_" + date + ".json" 

        # full path
        fullpath += "/" + filename

        jstring = json.dumps(response.json(), indent=4)
        
        f = open(fullpath, "w")
        f.write(jstring)
        f.close()