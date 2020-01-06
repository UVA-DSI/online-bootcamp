library(devtools)
library(tidyverse)
install_github("psychemedia/htmlwidget-hexjson")
library(jsonlite)
library(hexjsonwidget)
summary_data <- read.csv("hocl-ge2015-results-summary.csv")
m<- fromJSON("constituencies.hexjson")

colors <- function(abbrev){
  if (abbrev == "Lab"){
    return("#DC241F")
  } else if(abbrev == "Con"){
    return("#0087DC")
  } else if(abbrev == "SNP"){
    return("#FFFF00")
  } else if (abbrev == "PC"){
    return("#008142")
  } else if (abbrev == "DUP"){
    return("#D46A4C")
  } else if (abbrev == "Green"){
    return("#6AB023")
  } else if (abbrev == "Ind"){
    return("#DDDDDD")
  } else if (abbrev == "LD"){
    return("#FDBB30")
  } else if (abbrev == "SDLP"){
    return("#99FF66")
  } else if (abbrev =="SF"){
    return("#008800")
  } else if (abbrev =="Spk"){
    return("#AAAAAA")
  } else if (abbrev == "UKIP"){
    return("#70147A")
  } else if (abbrev == "UUP"){
    return("#9999FF")
  } else {
    return("#000000")
  }
}

c2 <-lapply(summary_data[,10], colors)
df1<-data.frame(id = as.character(summary_data$ons_id),color = matrix(unlist(c2), nrow=650, byrow=T), stringsAsFactors=FALSE)

hexjsonwidget(m, data = df1, colour = "color", label = NA)
