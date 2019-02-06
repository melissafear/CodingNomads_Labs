'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

kmRun = 10 * 1.6
totalSecsInHr= 60 * 60
secs_run= 30 * 60 + 30

percentOfHourRun = secs_run / totalSecsInHr

speed = kmRun/percentOfHourRun

print("Average speed in km/p/h is "+ str(speed))