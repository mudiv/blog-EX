# blog | ruks | muntazit

import requests 

EXText = requests.get("https://github.com/mudiv/").text
# هنا يشترط ان يكون محتوى المرجع من الوموقع بتنسبق json 
EXJson = requests.get("https://github.com/mudiv/").json()

EXContent = requests.get("https://github.com/mudiv/").content

EXStatus_code = requests.get("https://github.com/mudiv/").status_code

EXNext = requests.get("https://github.com/mudiv/").next

