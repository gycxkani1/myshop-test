class People():
    def run(self):
        print("run")
    
    def talk(self):
        print("talk")

class DriverMixin(object):
    def driver(self):
        print("driver")

class Children(DriverMixin,People):
    pass

c=Children()
c.run()
c.talk()
c.driver()

