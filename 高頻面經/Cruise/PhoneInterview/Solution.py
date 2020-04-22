# -*- coding: utf-8 -*-
def calculateBatteryPercentage(input):
    input = input.split('\n')
    totalUsage = 0
    totalSeconds = 0
    prevPercentage = 0
    prevMode = None
    prevTime = None
    for elem in input:
        currTime, precentage, mode = elem.split(" ")
        if prevMode == 'autonomous':
            totalUsage += (float(prevPercentage) - float(precentage))
            totalSeconds += (int(currTime) - int(prevTime))
        prevPercentage = precentage
        prevMode = mode
        prevTime = currTime

    if totalUsage == 0:
        return 0

    return (totalUsage / totalSeconds) * 60
