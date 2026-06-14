#!/usr/bin/env python3
import json
import os

def main():
    directory = os.fsencode(".")
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if (filename.endswith(".yydeck.json")):
            f = open(filename, "r+")
            dt = f.read().replace("<", "&lt").replace(">", "&gt")

            data = json.loads(dt)
            for i in data["cards"]:
                i["knowledge"] = 0
            #endfor
            for i in data["phrases"]:
                i["knowledge"] = 0
            #endfor
            f.seek(0)
            json.dump(data, f)
            f.truncate()

main()
