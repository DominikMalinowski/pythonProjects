from car import Car

class Battery():
    """Prosta próba modelowania akumulatora samochodu elektrycznego"""
    def __init__(self, battery_size = 75):
        """Inicjalizacja atrybutów akumulatora"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Wyświetlenie informacji o wielkości akumulatora"""
        print(f'Ten samochód ma akumulator o pojeności {self.battery_size} kWh')

    def get_range(self):
        """Wyświetla informacje o zasięgu samochodu na podstawie pojemności akumulatora"""
        if self.battery_size == 75:
            range = 260 
        elif self.battery_size == 100:
            range = 315
        print(f'Zasięg tego samochodu wynosi około {range}  km po pełnym naładowaniu akumulatora')

    def upgrade_battery(self):
        if self.battery_size != 100: 
            self.battery_size = 100

class ElectricCar(Car):
    """Przedstawai cechy charakterystyczne samochodu elektrycznego"""
    def __init__(self, make, model, year):
        """Inicjalizacja atrybutów klasy nadrzędnej. 
        Nastepnie inicjalizacja atrybutów charakterystycznych dla 
        samochodu elektrycznego."""
        super().__init__(make,model,year)
        self.battery = Battery()