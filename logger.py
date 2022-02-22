import requests, time, sys
from datetime import date, datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    if len(sys.argv) < 3:
        print("[Error] No Arguments Provided\n Usage: python3 detector.py [url] [update_time]")
        return

    with open("output.log", 'a') as file:
    
        while(True):
            file.write(datetime.now().strftime("%m/%d/%Y %H:%M:%S "))

            try:
                requests.get(str(sys.argv[1]), verify=False)
                file.write("1\n")
            except ValueError:
                print("[Error] Invalid URL\n Usage: python3 detector.py [url] [update_time]")
                return
            except Exception as e:
                file.write("0\n")

            file.flush()

            try:
                time.sleep(int(sys.argv[2]))
            except ValueError:
                print("[Error] Invalid Update Time\n Usage: python3 detector.py [url] [update_time]")
                return

if __name__=="__main__":
    main()