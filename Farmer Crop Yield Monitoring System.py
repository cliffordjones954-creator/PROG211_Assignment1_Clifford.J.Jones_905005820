class Farmer:
    System = "Farmer Crop Yield Monitoring System"

    def __init__(self, farmer_id, name, location, farm_size):
        self.farmer_id = farmer_id
        self.name = name
        self.location = location
        self.farm_size = farm_size

    def display_farmer(self):
        print(f"Farmer ID: {self.farmer_id}")
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Farm Size: {self.farm_size} acres")

    def update_farmer(self, name, location, farm_size):
        self.name = name
        self.location = location
        self.farm_size = farm_size

    @classmethod
    def display_system(cls):
        print(f"**********{cls.System}**********")

# CROP CLASS
class Crop:
    def __init__(self, crop_name, season, yield_amount, farmer):
        self.crop_name = crop_name
        self.season = season
        self.yield_amount = yield_amount
        self.farmer = farmer

    def display_crop(self):
        print(f"Crop: {self.crop_name}")
        print(f"Season: {self.season}")
        print(f"Yield: {self.yield_amount} kg")
        print(f"Farmer: {self.farmer.name}")

    def update_yield(self, new_yield):
        self.yield_amount = new_yield

# CREATE FARMER OBJECTS
farmer1 = Farmer(1, "Jane Bahh", "Makeni", 5)
farmer1.display_system()
farmer2 = Farmer(2, "Esther Mansaray", "Bo", 8)

# CREATE CROP OBJECT
crop1 = Crop("Rice", "Wet Season", 1200, farmer1)

# DISPLAY FARMER INFORMATION
print(f"***** FARMER INFORMATION *****")
farmer1.display_farmer()

# DISPLAY CROP INFORMATION
print(f"***** CROP INFORMATION *****")
crop1.display_crop()

# LIST OF FARMERS
farmers = []
farmers.append(farmer1)
farmers.append(farmer2)

print(f"***** LIST OF FARMERS *****")
for farmer in farmers:
    farmer.display_farmer()
    print()

# UPDATE FARMER INFORMATION
print(f"***** UPDATED FARMER *****")
farmer1.update_farmer("Jane Bahh", "Freetown", 7)
farmer1.display_farmer()

# UPDATE CROP YIELD
print(f"***** UPDATED CROP YIELD *****")
crop1.update_yield(1500)
crop1.display_crop()