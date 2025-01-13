Smartphone and Tablet Classes in Python
Overview
This Python program demonstrates object-oriented programming (OOP) concepts by modeling two classes: Smartphone and Tablet. The program showcases inheritance, polymorphism, and encapsulation in action.

The base class Device contains common attributes for electronic devices, and the derived classes Smartphone and Tablet extend the functionality of the Device class, each adding unique attributes and methods.

Features
Device Class: A base class that holds common attributes like brand, model, and battery_life.
Smartphone Class: Inherits from Device and adds attributes for camera_quality and os. It also includes a method to simulate taking a photo.
Tablet Class: Inherits from Device and includes attributes for screen_size and is_4g_supported. It also has a method to simulate watching videos.
Polymorphism: The display_info() method is overridden in the Smartphone and Tablet classes to provide customized device information.
Encapsulation: Data is encapsulated within the classes and accessed through methods.
Getting Started
Prerequisites
Python 3.x
Running the Program
Copy the code into a Python file (e.g., device_classes.py).
Run the script using the following command in your terminal or command prompt:
bash
Copy code
python device_classes.py
Output
The program will output device information for both the Smartphone and Tablet objects, followed by actions related to their specific methods, such as taking a photo for the smartphone and watching a video for the tablet.

Example output:

plaintext
Copy code
Apple iPhone 13 with 20 hours battery life. Camera: 12 MP, OS: iOS.
Taking a photo with 12 MP camera.
Samsung Galaxy Tab with 15 hours battery life. Screen Size: 10.5 inches, 4G Support: True.
Watching video on 10.5-inch screen.
Code Structure
Classes and Methods
Device Class:

__init__(self, brand, model, battery_life): Constructor to initialize device attributes.
display_info(self): Returns a string with the device's brand, model, and battery life.
Smartphone Class (Inherits from Device):

__init__(self, brand, model, battery_life, camera_quality, os): Constructor to initialize smartphone-specific attributes.
take_photo(self): Simulates taking a photo.
display_info(self): Overridden to include smartphone details (camera and OS).
Tablet Class (Inherits from Device):

__init__(self, brand, model, battery_life, screen_size, is_4g_supported): Constructor to initialize tablet-specific attributes.
watch_video(self): Simulates watching a video on the tablet.
display_info(self): Overridden to include tablet details (screen size and 4G support).
Example Use Case
This program is useful for understanding and demonstrating the following OOP concepts:

Inheritance: Sharing common attributes and methods among different classes.
Polymorphism: Overriding methods in derived classes to provide customized functionality.
Encapsulation: Keeping the attributes hidden inside the class and providing controlled access.
Customization
You can easily extend this program by adding more device types, such as Laptop, Smartwatch, etc., by creating new classes that inherit from Device.
You can also add additional attributes or methods to Smartphone or Tablet to further personalize the behavior of each class.
License
This program is open-source and free to use. You can modify it as per your needs.

End of README
This README provides clear instructions on what the program does, how to use it, and an explanation of its structure. It also encourages customization and further exploration of OOP concepts!
