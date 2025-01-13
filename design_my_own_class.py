# Base class: Device
class Device:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  

    def display_info(self):
        return f"{self.brand} {self.model} with {self.battery_life} hours battery life."

# Derived class: Smartphone
class Smartphone(Device):
    def __init__(self, brand, model, battery_life, camera_quality, os):
        super().__init__(brand, model, battery_life)
        self.camera_quality = camera_quality  
        self.os = os  

    def take_photo(self):
        return f"Taking a photo with {self.camera_quality} MP camera."

    def display_info(self):
        return f"{super().display_info()} Camera: {self.camera_quality} MP, OS: {self.os}."

# Derived class: Tablet
class Tablet(Device):
    def __init__(self, brand, model, battery_life, screen_size, is_4g_supported):
        super().__init__(brand, model, battery_life)
        self.screen_size = screen_size  
        self.is_4g_supported = is_4g_supported  

    def watch_video(self):
        return f"Watching video on {self.screen_size}-inch screen."

    def display_info(self):
        return f"{super().display_info()} Screen Size: {self.screen_size} inches, 4G Support: {self.is_4g_supported}."

# Create instances of the Smartphone and Tablet
phone = Smartphone("Apple", "iPhone 13", 20, 12, "iOS")
tablet = Tablet("Samsung", "Galaxy Tab", 15, 10.5, True)

# Display information and use methods
print(phone.display_info()) 
print(phone.take_photo()) 

print(tablet.display_info())  
print(tablet.watch_video())  
