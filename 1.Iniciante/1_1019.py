number = int(input())
minutes = number//60
if minutes>60:
    hours = minutes//60
else: hours = 0
if hours == minutes//60:
    mreal = minutes - (hours*60)
seconds = number%60
if hours != minutes//60:
    print("{}:{}:{}".format(hours,minutes,seconds))
else: print("{}:{}:{}".format(hours,mreal,seconds))