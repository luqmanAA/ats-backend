
class Time:

    def __init__( self ):
        
        self.hour = 23 # 0-23
        self.minute = 59 # 0-59
        self.second = 49 # 0-59

    def tick(self):
        if self.second < 59:
            self.second += 1
            return self.second, self.minute, self.hour

        elif self.second == 59 and self.minute < 59:
            self.second = 0
            self.minute += 1
            return self.second, self.minute, self.hour

        elif self.minute == 59 and self.hour < 23:
            self.second = 0
            self.minute = 0
            self.hour += 1
            return self.second, self.minute, self.hour
        self.second, self.minute, self.hour = 0,0,0
        return self.second, self.minute, self.hour

    def get_military_format( self ):

        return("%.2d:%.2d:%.2d" % ( self.hour, self.minute, self.second ))

    def get_standard_format( self ):

        standardTime = ""

        if self.hour == 0 or self.hour == 12:
            standardTime += "12:"
        else:
            standardTime += "%d:" % ( self.hour % 12 )

        standardTime += "%.2d:%.2d" % ( self.minute, self.second )

        if self.hour < 12:
            standardTime += " AM"
        else:
            standardTime += " PM"
        
        return standardTime

time = Time()

time.tick()
print(time.get_standard_format())
print(time.get_military_format())

