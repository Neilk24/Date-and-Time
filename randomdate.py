import random
import time

def GetRandomDate(stardate, enddate):
    print('Printing random date between', stardate, 'and', enddate)
    randomGenerator = random.random()
    DateFormat = '%m/%d/%Y'
    startTime = time.mktime(time.strptime(stardate, DateFormat))
    endTime = time.mktime(time.strptime(enddate, DateFormat))
    RandomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(DateFormat, time.localtime(RandomTime))
    return randomDate

print('Random date = ', GetRandomDate("1/1/2020", "12/31/2024"))
