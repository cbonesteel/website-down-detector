import requests
import time
import matplotlib
import sys
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

history = []
time_history = []

def __main__():
    if len(sys.argv) < 3:
        print("[Error] No Arguments Provided\n Usage: python3 detector.py [url] [update time]")
        return
    plt.ion()
    first = True

    while(True):
        if len(history) == 1440:
            history.pop(0)
            time_history.pop(0)

        try:
            requests.get(str(sys.argv[1]), verify=False)
            history.append(1)
        except ValueError:
            print("[Error] Invalid URL\n Usage: python3 detector.py [url] [update time]")
            return
        except Exception as e:
            history.append(0)

        time_history.append(datetime.now().strftime("%H:%M:%S"))

        if first:
            figure = plt.figure()
            ax = figure.add_subplot(111)
            ax.set(ylim=(0,1), yticks=np.arange(0,1.5))
            ax.autoscale(enable=True, axis='x')
            line1, = ax.plot(time_history, history)
            plt.title("Gitlab Status", fontsize=20)
            plt.xlabel("Time")
            plt.ylabel("Status")
            first = False

        line1.set_xdata(time_history)
        line1.set_ydata(history)

        plt.xticks(time_history)
        
        figure.canvas.draw_idle()
        figure.canvas.flush_events()
        try:
            time.sleep(int(sys.argv[2]))
        except ValueError:
            print("[Error] Invalid Update Time\n Usage: python3 detector.py [url] [update time]")
            return

if __name__=="__main__":
    __main__()