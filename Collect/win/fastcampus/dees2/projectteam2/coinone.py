from datetime import datetime

from config import Source
from config import Config
from fastcampus.dees2.module.models import Coinone
import requests

# from utils.slack import send_message
import json
import os


class ParserCoinone:
    def __init__(self):
        self.model = Coinone
        self.url = Source.COINONE_URI
        self.currency = ["btc", "eth"]

    def get_response(self, params):
        try:
            response = requests.get(self.url, params)
            return response

        except requests.exceptions.ConnectionError as e:
            print (e)
            # send_message("#data-monitoring", "Connection Failed!")
            return "Connection Failed!"

    def parse(self, response, currency):
        result = response.json()
        price = result["last"]
        volume = result["volume"]
        self.model = Coinone(datetime.utcnow(), price, volume, currency)
        return self.model

    def save( self,response, currency):
        result = response.json()
        date = result["timestamp"]

        # root path
        fullpath = Config.ROOT_RAW_PATH
        
        # file path
        filepath = self.model.__tablename__ + "\\" + datetime.now().strftime('%Y\%m\%d')
            
        for folder in filepath.split("\\"):
            fullpath += "\\" + folder 
            if not os.path.isdir(fullpath):
                os.mkdir(fullpath)
       
        # file name
        filename = currency + "_" + date + ".json" 

        # full path
        fullpath += "\\" + filename

        jstring = json.dumps(response.json(), indent=4)
        
        f = open(fullpath, "w")
        f.write(jstring)
        f.close()
