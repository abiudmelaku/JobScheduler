from datetime import datetime, timedelta
import time

class Func_IO:
    def check_time_format(self , x):
        try:
            x = x.replace(" ", "")
            am_pm = x[-2:]
            if am_pm.upper() == "AM" or am_pm.upper() == "PM":
                x = str(x[:-2])
                time.strptime(x, '%H:%M')
                return True

        except ValueError:
            return False



    def convert24(self , x):
        x = x.replace(" ", "")
        in_time = datetime.strptime(x, "%I:%M%p")
        out_time = datetime.strftime(in_time, "%H:%M")
        return out_time

    def convert12(self , x):
        convert = datetime.strptime(x, "%H:%M")
        return convert.strftime("%I:%M %p")


    def calculate_duration(self, time, duration):
        time = time.replace(" " , "")
        dh, dm = duration.split(":")
        h, m = time.split(":")
        d = timedelta(hours=int(dh), minutes=int(dm))
        t = timedelta(hours=int(h), minutes=int(m))
        sum = str(t + d)
        test = sum.split(":")
        if(len(test[0]) == 1):
            sum = "0"+sum
        return sum


