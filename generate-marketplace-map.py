#!/usr/bin/env python3
import os
import json

def main():
    official_obj = {}
    unofficial_obj = {}
    root_dir = "."
    
    for root, dirs, files in os.walk(root_dir):
        # Skip hidden directories like .git
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.endswith(".yydeck.json"):
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, root_dir)
                
                # Check preset levels
                preset_levels = file.endswith(".presetlvl.yydeck.json")
                
                # Human-readable name
                if preset_levels:
                    base_name = file[:-len(".presetlvl.yydeck.json")]
                else:
                    base_name = file[:-len(".yydeck.json")]
                deck_name = base_name.replace("-", " ")
                
                # Load and process the file
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    card_count = len(data.get("cards", []))
                    phrase_count = len(data.get("phrases", []))
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
                    continue
                
                deck_info = {
                    "name": deck_name,
                    "cards": card_count,
                    "phrases": phrase_count,
                    "preset_levels": preset_levels,
                    "location": file
                }
                
                # Categorize
                if rel_path.startswith("official/"):
                    subfolder = os.path.dirname(os.path.relpath(filepath, "official"))
                    official_obj.setdefault(subfolder, []).append(deck_info)
                else:
                    if rel_path.startswith("community/"):
                        subfolder = os.path.dirname(os.path.relpath(filepath, "community"))
                    else:
                        subfolder = os.path.dirname(rel_path)
                    unofficial_obj.setdefault(subfolder, []).append(deck_info)

    # Sort decks in each subfolder
    for subfolder in official_obj:
        official_obj[subfolder].sort(key=lambda x: x["location"])
    for subfolder in unofficial_obj:
        unofficial_obj[subfolder].sort(key=lambda x: x["location"])
        
    # Sort subfolder keys
    sorted_official_obj = {k: official_obj[k] for k in sorted(official_obj.keys())}
    sorted_unofficial_obj = {k: unofficial_obj[k] for k in sorted(unofficial_obj.keys())}
    
    result = {
        "official": [sorted_official_obj] if sorted_official_obj else [],
        "unofficial": [sorted_unofficial_obj] if sorted_unofficial_obj else []
    }
    
    # Write to marketplace-map.json in minified format
    with open("marketplace-map.json", "w", encoding="utf-8") as f:
        json.dump(result, f, separators=(',', ':'))
    print("Successfully generated marketplace-map.json")

if __name__ == "__main__":
    main()
