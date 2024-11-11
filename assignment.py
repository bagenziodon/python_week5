class Superhero:
    def __init__(self, name, superpower, health):
        """Constructor to initialize the superhero's attributes"""
        self.name = name
        self.superpower = superpower
        self.health = health

    def display_info(self):
        """Display the superhero's information"""
        print(f"Superhero: {self.name}")
        print(f"Superpower: {self.superpower}")
        print(f"Health: {self.health}")

    def attack(self):
        """Generic attack method"""
        print(f"{self.name} is attacking with their {self.superpower}!")

    def defend(self):
        """Generic defend method"""
        print(f"{self.name} is defending themselves!")

class SuperSpeedHero(Superhero):
    def __init__(self, name, superpower, health, speed):
        super().__init__(name, superpower, health)
        self.speed = speed  # Additional attribute for speed

    def attack(self):
        """Override the attack method for super speed"""
        print(f"{self.name} is attacking at {self.speed} km/h with {self.superpower}!")

    def run(self):
        """Run at super speed"""
        print(f"{self.name} is running at {self.speed} km/h!")

class FlyingHero(Superhero):
    def __init__(self, name, superpower, health, wingspan):
        super().__init__(name, superpower, health)
        self.wingspan = wingspan  # Additional attribute for wingspan

    def attack(self):
        """Override the attack method for flying"""
        print(f"{self.name} is attacking while flying with their {self.superpower}!")

    def fly(self):
        """Fly with wings"""
        print(f"{self.name} is flying with a wingspan of {self.wingspan} meters!")

class FireHero(Superhero):
    def __init__(self, name, superpower, health, fire_intensity):
        super().__init__(name, superpower, health)
        self.fire_intensity = fire_intensity  # Additional attribute for fire intensity

    def attack(self):
        """Override the attack method for fire-based attacks"""
        print(f"{self.name} is attacking with intense fire at {self.fire_intensity} temperature!")

    def breathe_fire(self):
        """Breathe fire"""
        print(f"{self.name} is breathing fire with {self.fire_intensity} intensity!")
# Creating objects of different superhero classes
flash = SuperSpeedHero("Flash", "Super Speed", 100, 300)  # Speed in km/h
superman = FlyingHero("Superman", "Flight", 150, 10)  # Wingspan in meters
inferno = FireHero("Inferno", "Fire Control", 120, 500)  # Fire intensity in degrees

# Display superhero info and demonstrate polymorphism in attack()
flash.display_info()
flash.attack()  # Flash attacks with speed
flash.run()  # Flash runs at super speed

print()  # Just for separating outputs

superman.display_info()
superman.attack()  # Superman attacks while flying
superman.fly()  # Superman flies

print()  # Just for separating outputs

inferno.display_info()
inferno.attack()  # Inferno attacks with fire
inferno.breathe_fire()  # Inferno breathes fire
