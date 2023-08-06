import json
import requests
import sys
from crypt.crypt import Crypt

class Config():
    #initialize object by passing in config file
    #store info in config file in dict called data
    def __init__(self, config):
        self.config = config
        self.data = {}

    #print dictionary --> convenience function for debugging purposes
    def printdata(self):
        for k,v in self.data.items():
            print(v)

    #read config file and store values in dictionary called data
    #sessionAuthUrl, keyAuthUrl, are endpoints used for authentication respectively
    #podHost and agentHost are used for any of the other REST API requests
    def connect(self):
        with open(self.config, "r") as read_file:
            data = json.load(read_file)
            self.data['sessionAuthUrl'] = data['sessionAuthHost']
            self.data['keyAuthUrl'] = data['keyAuthHost']
            self.data['podHost'] = data['podHost']
            self.data['agentHost'] = data['agentHost']
            self.data['botCertPath'] = data['botCertPath']
            self.data['botCert_cert'] = data['botCertPath'] + 'bot.user11-cert.pem'
            self.data['botCert_key'] = data['botCertPath'] + 'bot.user11-key.pem'
            self.data['botCertName'] = data['botCertName']
            self.data['botCertPassword'] = data['botCertPassword']
            self.data['botEmailAddress'] = data['botEmailAddress']
            self.data['botCertPassword'] = data['botCertPassword']
        #take in .p12 certificate and parse through file to use for authentication
        #data['botCert_cert'] and data['botCert_key'] are passed as certificates upon authentication request
        try:
            crypt = Crypt(self.data['botCertName'], self.data['botCertPassword'])
            self.data['symphony_crt'], self.data['symphony_key'] = crypt.p12parse()


        except Exception as err:
            print("Failed to load config file: %s" % err)
            raise
