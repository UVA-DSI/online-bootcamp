from datetime import datetime
import time
first_time = datetime.now()
#Add sleep time to get a result that isn't 0:00:00
time.sleep(5)
final_time = datetime.now()
print("This program takes " + str(final_time - first_time) + " to run")
