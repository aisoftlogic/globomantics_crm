#!/usr/bin/env python

class Database:
    def __init__(self, path):
        # self.data = {"ACCT100": {"paid": 60, "due": 100},"ACCT200": {"paid": 70, "due": 60}, "ACCT300": {"paid": 0, "due": 0}}
        
        with open(path, "r") as handle:
            
            # import json
            # self.data = json.load(handle)

            # import yaml
            # self.data = yaml.safe_load(handle)

            import xmltodict
            self.data = xmltodict.parse(handle.read())["root"]


    def balance(self, acct_id):
        acct = self.data.get(acct_id)
        if acct:
            return int(acct["due"]) - int(acct["paid"])
        return None