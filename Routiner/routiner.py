from threading import Thread
import schedule
import time

class Routiner(Thread):
     
    def __init__(self, hours, function, *args, first_launch=False, check_time_hours=None):
        Thread.__init__(self)
        self.__hours = hours
        self.__function = function
        self.__first_launch = first_launch
        self.__args = args
        
        if check_time_hours == None:
            self.__check_time_hours = hours
        else:
            self.__check_time_hours = check_time_hours

    def run(self):

        if self.__first_launch:
            self.__function(*self.__args)


        schedule.every(self.__hours).hours.do(self.__function, *self.__args)

        while True:
            schedule.run_pending()
            time.sleep(3600*self.__check_time_hours)