import re
import sys

import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.json())



