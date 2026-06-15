#!/usr/bin/env python3
import json
import os

def sanitize_dir(base_path):
    directory = os.fsencode(base_path)
    if not os.path.exists(directory):
        return
    for file in os.listdir(directory):
        dir_path = os.path.join(base_path, os.fsdecode(file))
        if os.path.isdir(dir_path):
            folderName = os.fsdecode(file)
            sub_dir = os.path.join(base_path, folderName)
            for ff in os.listdir(os.fsencode(sub_dir)):
                filename = os.fsdecode(ff)
                if filename.endswith(".yydeck.json"):
                    filepath = os.path.join(sub_dir, filename)
                    f = open(filepath, "r+")
                    dt = f.read().replace("<", "&lt").replace(">", "&gt")

                    data = json.loads(dt)
                    if not filename.endswith(".presetlvl.yydeck.json"):
                        for i in data.get("cards", []):
                            i["knowledge"] = 0
                        #endfor
                        for i in data.get("phrases", []):
                            i["knowledge"] = 0
                        #endfor
                    #endif
                    f.seek(0)
                    json.dump(data, f)
                    f.truncate()
                    f.close()

def main():
    sanitize_dir("./official/")
    sanitize_dir("./community/")

if __name__ == "__main__":
    main()
