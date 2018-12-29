import time
import sched

import pomodoro_event
import rpi_gpio_helper

from threading import Timer

class PomodoroTimer:
    def __init__(self):
        return 
    
    def init(self):
        self.t = Timer(5, self.time_expire_handler, ())
        return
    
    def time_expire_handler(self):
        print("timer is expired")
    
    def start_timer(self):
        print("config timer1")
        print("config timer4");
        self.t.start()

    def cancel_timer(self):
        self.t.cancel()
        
    def stop(self):
        return
    
    def restart(self):
        return



def main():

    pomodoro_timer = PomodoroTimer()
    pomodoro_timer.init()

    pomodoro_timer.start_timer()

    time.sleep(10)
    pomodoro_timer.cancel_timer()
    while (True):
        time.sleep(50)
    

if __name__ == "__main__":
    main()
