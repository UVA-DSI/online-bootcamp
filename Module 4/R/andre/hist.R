#load tidyverse
library(tidyverse)
#import data
df <- read.csv("andre.csv")
#clean data
df <- filter(df, Year!= 1976)
df <- filter(df, Year < 1994)
#create histogram
ggplot(data = df, aes(df$H)) + geom_histogram()
