#Get beginning time
beg_time <- Sys.time()

#find difference between beginning and now
time_dif <- difftime(Sys.time(), beg_time)

#print difference
print(time_dif)