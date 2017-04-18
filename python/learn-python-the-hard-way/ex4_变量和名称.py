# -*- coding: utf-8 -*-

#变量名中用下划线连接单词，可以很清楚的看清变量的含义
cars = 100 #名为cars的变量存储1oo
space_in_cars = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven*space_in_cars
average_passengers_per_car = passengers/cars_driven

print "there are ",cars,"cars avaiable"
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
