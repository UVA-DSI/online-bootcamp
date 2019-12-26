#import datetime to record time at the beginning of the program and time to make the program longer
from datetime import datetime
import time

#Get current time at beginning of program
beginning = datetime.now()

#artifically increase program runtime to ensure proper functioning
time.sleep(2.12354)

#get the time at the end of the program
print('Program runtime: ' + str(datetime.now() - beginning))