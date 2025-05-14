import random
from datetime import datetime

def random_date(max):
    max = random.randint(datetime)
    date = datetime.fromtimestamp(max)

MIN_TIMESTAMP = int(datetime.now().timestamp()) # today
MAX_TIMESTAMP = int(datetime(2050,1,1).timestamp()) # January 1, 2050
print(random_date(MIN_TIMESTAMP, MAX_TIMESTAMP))

# Expected output
# 2029-05-31 05:00:07
# 2036-01-23 16:34:27  
# 2040-09-29 14:15:19

