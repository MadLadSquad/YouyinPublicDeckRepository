#!/usr/bin/env python3
import json
import os

def main():
    directory = os.fsencode("./community/")
    for file in os.listdir(directory):
        if os.path.isdir("./community/" + os.fsdecode(file)):
            folderName = os.fsdecode(file)
            for ff in os.listdir(os.fsencode("./community/" + os.fsdecode(file))):
                filename = os.fsdecode(ff);
                if filename.endswith(".yydeck.json"):
                    f = open("./community/" + folderName + "/" + filename, "r+")
                    dt = f.read().replace("<", "&lt").replace(">", "&gt")

                    data = json.loads(dt)
                    if not filename.endswith(".presetlvl.yydeck.json"):
                        for i in data:
                            i["knowledge"] = 0
                    #endfor
                    f.seek(0)
                    json.dump(data, f)
                #endif
            #endfor
        #endif
    #endfor
#endfunc


main()
