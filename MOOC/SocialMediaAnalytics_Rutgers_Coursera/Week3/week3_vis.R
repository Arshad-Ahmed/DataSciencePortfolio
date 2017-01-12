#load libraries
library(ggplot2)
library(plyr)
library(hexbin)

#load datasets
business <- read.csv(file.choose())
users <- read.csv(file.choose())

#check data has read properly
head(users)
names(users)

#get column names

names(business)
head(business)

#visualise data

#look at star distribution in users
ggplot(users) + geom_histogram(aes(x=average_stars))

#look at fans distribution
ggplot(users) + geom_histogram(aes(x=fans))

#any relation between fans and average stars
ggplot(users) + geom_hex(aes(x=fans,y=average_stars))

#business review counts with star rating
ggplot(business) + geom_hex(aes(x=review_count, y=stars))


