#!/usr/bin/env python3
import json
import os

def main():
    directory = os.fsencode("./official/")
    for file in os.listdir(directory):
        if os.path.isdir("./official/" + os.fsdecode(file)):
            folderName = os.fsdecode(file)
            for ff in os.listdir(os.fsencode("./official/" + os.fsdecode(file))):
                filename = os.fsdecode(ff);
                if filename.endswith(".yydeck.json"):
                    f = open("./official/" + folderName + "/" + filename, "r+")
                    dt = f.read().replace("<", "&lt").replace(">", "&gt")

                    data = json.loads(dt)
                    for i in data["cards"]:
                        i["knowledge"] = 0
                    
                    for i in data["phrases"]:
                        i["knowledge"] = 0
                    
                    f.seek(0)
                    json.dump(data, f)
                    f.truncate()
main()
