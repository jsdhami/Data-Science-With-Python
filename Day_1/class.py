class Home:
      def __init__(self, name, address):
            self.name = name
            self.address = address
      
      def display(self):
            print(f"Name: {self.name}\nAddress: {self.address}")
      
      def __str__(self):
            return f"Name: {self.name}\nAddress: {self.address}"
      
# creating an object of the class
# home = Home("Home", "Nairobi")
# home.display()
# result = home.__str__()
# print("Result: ", result)

class App:
      def __init__(self, name, version):
            self.name = name
            self.version = version
            
      def display(self):
            print(f"Name: {self.name}\nVersion: {self.version}")
            
      def __str__(self):
            return f"Name: {self.name}\nVersion: {self.version}"
      # meaning of __str__ is to return a string representation of the object when the object is printed
      # __str__ is a magic method in python
      # __str__ is called when the object is printed
      
app = App("App", "1.0")

# print("App: ", app)

# inheritance
class AndroidApp(App):
      def __init__(self, name, version, os):
            super().__init__(name, version)
            self.os = os
            
      def display(self):
            print(f"Name: {self.name}\nVersion: {self.version}\nOS: {self.os}")
            
      def __str__(self):
            return f"Name: {self.name}\nVersion: {self.version}\nOS: {self.os}"
      
android_app = AndroidApp("Android App", "1.0", "Android")
# print("Android App: ", android_app)
# android_app.display()

class IOSApp(App):
      def __init__(self, name, version, os):
            super().__init__(name, version)
            self.os = os
            
      def display(self):
            print(f"Name: {self.name}\nVersion: {self.version}\nOS: {self.os}")
            
      def __str__(self):
            return f"Name: {self.name}\nVersion: {self.version}\nOS: {self.os}"
      
ios_app = IOSApp("IOS App", "1.0", "IOS")
# print("IOS App: ", ios_app)
# ios_app.display()

# multiple inheritance
class HybridApp(AndroidApp, IOSApp):
      def __init__(self, name, version, os):
            AndroidApp.__init__(self, name, version, os)
            IOSApp.__init__(self, name, version, os)
            
      def display(self):
            print(f"Name: {self.name}\nVersion: {self.version}\nOS: {self.os}")
            
      def __str__(self):
            return f"Name: {self.name}\nVersion: {self.version}\nOS: {self.os}"