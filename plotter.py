### Shelly Dimmer 2 Plotter 
### Temperature / Brightness over Time
### SpawnTerror 2021

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation


from urllib.request import urlopen
from datetime import datetime
import json
import time

# Create figure for plotting / variables
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
ys2 = []

# Shelly IP / update interval
update_interval = 10000
url = "http://192.168.1.230/status"

# Gui info
fig.text(0.5, 0.92, "Shelly Dimmer 2 Plotter", ha="center", va="bottom", size="medium",color="black")
fig.text(0.40, 0.89, "Temperature", ha="center", va="bottom", size="medium",color="red")
fig.text(0.5, 0.89, " & ", ha="center", va="bottom", size="medium")
fig.text(0.60,0.89,"Brightness", ha="center", va="bottom", size="medium",color="blue")
fig.text(0.13,0.15,'URL: ' + url + '.' , ha="left", va="bottom", size="medium",color="black")
fig.text(0.13,0.12,'Start time: ' + dt.datetime.now().strftime('%H:%M:%S') + '.' , ha="left", va="bottom", size="medium",color="black")
fig.text(0.13,0.09,'Update interval: ' + str(update_interval)[0:2] + 's.' , ha="left", va="bottom", size="medium",color="black")


# Animate function
def animate(i, xs, ys):

    # Read temperature (Celsius) from TMP102
    response = urlopen(url)
    data = json.loads(response.read())  
    tempe_values = data['tmp']
    temperature = tempe_values['tC']
    light_values = data['lights']
    light_read = light_values[0]
    brightness = light_read['brightness']
    plt.pause(0.001)
   
    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%M:%S'))
    ys.append(temperature)
    ys2.append(brightness)
    
    # Draw x and y lists
    ax.plot(xs, ys, color='red')
    ax.plot(xs, ys2, color='blue')

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.ylabel('Temperature (C)')

# Set up plot to call animate() function periodically
runtime = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=update_interval)
plt.show()

