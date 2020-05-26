import datetime
sunrise = datetime.time(7,30,0) #Lights sould come on at 07:00
period = [16,0,0]
sunset = datetime.time(sunrise.hour + period[0], sunrise.minute + period[1], sunrise.second + period[2]) #Lights sould turn off after the period.
state = 0
while (True):  
    time = datetime.datetime.now().time()
    if state == 0:  #Lights are in state 'off'
        if time > sunrise and time < sunset:   #Lights should be on
            state = 1    #Change state to 'on'
            # relay_open(channel)
            print("Changing state to on")
        else:
            continue    #Lights should remain off

    elif state == 1:    #Lights are in state 'on'
        if time < sunrise or time >= sunset:   #Lights should be off
            state = 0    #Change state to 'off'
            # relay_closed(channel)
            print("Changing state to off")
        else:
            continue #Lights should remain on