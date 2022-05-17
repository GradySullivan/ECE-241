sec = int(input("Input Number of Seconds ")) #input number of seconds

def convert(sec): #function to convert seconds
    min,hour,day = 0,0,0

    if sec >= 60: #converts seconds into minutes if there are at least 60 seconds
        min=sec//60
        sec=sec%60 #calculates leftover seconds

    if min >= 60: #converts minutes into hours if there are at least 60 minutes
        hour=min//60
        min=min%60 #calculates leftover minutes

    if hour >= 24: #converts hours into days if there are at least 24 hours
        day=hour//24
        hour=hour%24 #calculates leftover hours

    if day == 0: #omits days from answer if there are 0 days
        if hour == 0: #omits hours from answer if there are 0 hours
            if min == 0: #omits minutes from answer if there are 0 minutes
                print("%s seconds(s)" % (sec)) #print statement without days, hours, and minutes
            else:
                print("%s minutes(s), %s seconds(s)" % (min, sec)) #print statement without days and hours
        else:
            print("%s hour(s), %s minute(s), %s second(s)" % (hour, min, sec)) #print statement without days
    else:
        print("%s day(s), %s hour(s), %s minute(s), %s second(s)" % (day, hour, min, sec)) #print statement when the answer is at least one day

convert(sec) #start function
