sec = int(input("Input Number of Seconds: ")) #input number of seconds

def convert(sec): #function to convert seconds
    min,hour,day = 0,0,0
    sec_name, min_name, hour_name, day_name = "","","",""

    if sec >= 60: #converts seconds into minutes if there are at least 60 seconds
        min = sec // 60
        sec = sec % 60 #calculates leftover seconds

    if sec > 1: #decides whether second should be singular/plural
        sec_name = " seconds"
    elif sec == 1:
        sec_name = " second"
    else:
        sec_name = ""

    if min >= 60: #converts minutes into hours if there are at least 60 minutes
        hour =min // 60
        min = min % 60 #calculates leftover minutes

    if min > 1 and sec == 0: #decides whether minute should be singular/plural
        min_name = " minutes"
    elif min > 1 and sec != 0:
        min_name = " minutes,"
    elif min == 1 and sec == 0:
        min_name = " minute"
    elif min == 1 and sec != 0:
        min_name = " minute,"
    else:
        min_name = ""

    if hour >= 24: #converts hours into days if there are at least 24 hours
        day = hour//24
        hour=hour % 24 #calculates leftover hours

    if hour > 1 and (min != 0 or sec != 0): #decides whether hour should be singular/plural
        hour_name = " hours,"
    elif hour > 1 and min == 0:
        hour_name = " hours"
    elif hour == 1 and (min != 0 or sec != 0):
        hour_name = " hour,"
    elif hour == 1 and min == 0:
        hour_name = " hour"
    else:
        hour_name = ""

    if day > 1 and (hour != 0 or min != 0 or sec != 0): #decides whether day should be singular/plural
        day_name = " days,"
    elif day > 1 and hour == 0 :
        day_name = " days"
    elif day == 1 and (hour != 0 or min != 0 or sec != 0):
        day_name = " day,"
    elif day == 1 and hour == 0:
        day_name = " day"
    else:
        day_name = ""

    #following if statements add space in front of each number
    if sec > 0:
        sec = " "+str(sec)
    if min > 0:
        min = " "+str(min)
    if hour > 0:
        hour = " "+str(hour)

    #following if statements turns values of zero to a blank string
    if sec == 0:
        sec = ""
    if min == 0:
        min = ""
    if hour == 0:
        hour = ""
    if day == 0:
        day = ""

    if day == 0: #omits days from answer if there are 0 days
        if hour == 0: #omits hours from answer if there are 0 hours
            if min == 0: #omits minutes from answer if there are 0 minutes
                print("%s%s" % (sec,sec_name)) #print statement without days, hours, and minutes
            else:
                print("%s%s%s%s" % (min, min_name, sec, sec_name)) #print statement without days and hours
        else:
            print("%s%s%s%s%s%s" % (hour, hour_name, min, min_name, sec, sec_name)) #print statement without days
    else:
        print("%s%s%s%s%s%s%s%s" % (day, day_name, hour, hour_name, min, min_name, sec, sec_name)) #print statement when the answer is at least one day

convert(sec) #start function