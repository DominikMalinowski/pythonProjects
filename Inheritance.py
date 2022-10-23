
# parent class
class Device():
   def __init__(self, dev_name):
       self.name = dev_name

   def turn_on(self):
       print(f"Device {self.name} turned on")

   def turn_off(self):
       print(f"Device {self.name} turned off")

   def ring(self):
       print(f"Device {self.name} ringing")

# sub class (?)
class SmartDevice(Device):
    def update(self):
        print(f"Device {self.name} is being updated")

    def exchange_data(self):
        print(f"Device {self.name} exchanging data")

# child class
class MobilePhone(SmartDevice):
    def game_mode(self):
       print(f"Device {self.name} set to game mode")


class SmartWatch(SmartDevice):
    def measure_heart_rate(self):
       print(f"Device {self.name} measuring_heart_rate")

    #superchage classes
    def exchange_data(self):
       super().exchange_data()
       print(f"Device {self.name} checking connection with mobile phone")

# initialising and using devices
x_phone = MobilePhone("xPhone")
x_watch = SmartWatch("xWatch")

x_phone.turn_on()
x_phone.game_mode()
x_phone.exchange_data()
x_phone.ring()
x_phone.update()
x_phone.turn_off()

x_watch.turn_on()
x_watch.update()
x_watch.measure_heart_rate()
x_watch.ring()
x_watch.exchange_data()
x_watch.turn_off()