#Write a program that prints out a time it takes to run.

#Step 1: Record the time at the start of the program.
#Step 2: Print the current time minus the time at the start of the program.


start_time <- Sys.time()
print(format(Sys.time(),"%I:%M:%S %p"))

Sys.sleep(5)

elapsed_time <- Sys.time() - start_time
print(format(Sys.time(),"%I:%M:%S %p"))
print(elapsed_time)