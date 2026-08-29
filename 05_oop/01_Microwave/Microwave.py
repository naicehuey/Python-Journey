class Microwave:
    def __init__(self, brand, power_rating):
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False

    def turn_on(self):
        if self.turned_on:
            print(f"Microwave ({self.brand}) is already turned on.")
        else:
            self.turned_on = True
            print(f"Microwave ({self.brand}) is now turned on.")

    def turn_off(self):
        if self.turned_on:
            self.turned_on = False
            print(f"Microwave ({self.brand}) is now turned off.")
        else:
            print(f"Microwave ({self.brand}) is already turned off.")

    def run(self, seconds: int):
        if self.turned_on:
            print(f"Running ({self.brand}) for {seconds} seconds.")
        else:
            print(f"You need to turn on your Microwave.")

    def __str__(self):
        return f"{self.brand} (Rating: {self.power_rating})"

    def status(self):
      state = "ON" if self.turned_on else "OFF"
      print(f"{self.brand} is currently {state}")

# -------------------------
# Creating objects
# -------------------------
    
smeg: Microwave = Microwave('smeg', 'B')
bosch: Microwave = Microwave('bosch', 'A')

# -------------------------
# Testing
# -------------------------
print(smeg)

print(bosch)

smeg.turn_on()

smeg.turn_on()

bosch.turn_on()

smeg.run(50)

smeg.turn_off()

bosch.status()

smeg.status()