import schedule
import time
import datetime
def job():
    print("I'm working...")
    print(datetime.datetime.now().strftime("%Y-%n-%d %H:%M:%S"))

schedule.every(5).seconds.do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
# schedule.every().minute.at(":17").do(job)
print(datetime.datetime.now().strftime("%Y-%n-%d %H:%M:%S"))

while True:

    schedule.run_pending()

    time.sleep(1)