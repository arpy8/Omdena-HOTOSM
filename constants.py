import json

PAGE_BANNER = "assets/images/banner.png"
PAGE_FAVICON = "assets/images/favicon.png"
PAGE_BACKGROUND = "assets/images/background.png"

with open("./assets/data.json", "r") as f:
    TASKS_DICT = json.load(f)
    TASKS_DICT = {k: v for k, v in TASKS_DICT.items()}
    
if __name__=="__main__":
    print(TASKS_DICT.keys())