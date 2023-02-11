#!/usr/bin/env python3
import json
import os

def main():
    directory = os.fsencode(".")
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if (filename.endswith(".yydeck.json")):
            f = open(filename, "r+")
            data = json.load(f)
            for i in data:
                i["knowledge"] = 0
            #endfor
            f.seek(0)
            json.dump(data, f)
        #endif
    #endfor
#endfunc


main()
