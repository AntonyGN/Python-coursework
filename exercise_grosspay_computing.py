#Program that prompts the user for hours and rate per hour to compute gross pay

hours = input ("Enter Hours:")
rate = input ("Enter Rate:")

hours = int(hours)
rate =  float(rate)       

Pay = (hours*rate)

print(Pay)