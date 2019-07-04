import requests
import json

class block:
    def __init__(self, address):
        self.url = "http://eliotctl.fr:6876/nxt"
        querystring = {"requestType":"getAccount","account":address}
        response = requests.request("GET", self.url, params=querystring)
        try:
            self.acc = json.loads(response.text)
            test = self.acc["publicKey"]
        except:
            self.acc = None

    def get_data(self, data):
        if self.acc is None:
            return [False, "invalid account", 401]
        return [True, {"account": self.acc["accountRS"], "data": self.acc[data]}, 200]

    def upload(self, data):
        if self.acc is None:
            return [False, "invalid account", 401]
        querystring = {"requestType":"uploadTaggedData","data":json.dumps(data),"name":"Upload Model " + self.acc["accountRS"] ,"description":""","tags":"","channel":"","secretPhrase":"disappear%20joke%20opinion%20blush%20rare%20wonderful%20curse%20drag%20deadly%20swell%20manage%20minute","feeNQT":"100000000","deadline":"60"}
        response = requests.request("POST", self.url, params=querystring)
        querystring = {"requestType":"sendMoney","secretPhrase":"disappear%20joke%20opinion%20blush%20rare%20wonderful%20curse%20drag%20deadly%20swell%20manage%20minute","recipient": self.acc["accountRS"],"amountNQT":"200000000","feeNQT":"100000000","deadline":"60"}
        response = requests.request("POST", self.url, params=querystring)
        return [True, {"account": self.acc["accountRS"], "payback": 200000000}, 200]
