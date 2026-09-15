from AC import *
class AC:
    def __init__(self,ac_name):
        self.ac_name = ac_name
        self.operating_mode = "cooling"
        self.temperature = 0

    def set_temperature(self,temperature):
        self.temperature = temperature
        print(f"AC temperature is {self.temperature}°C!")

    def change_temperature(self,change_temperatures):
        self.change_temperatures = change_temperatures
        self.temperature += self.change_temperatures
        print(f"AC temperature is {self.temperature}°C!")


    def change_mode(self,operating_mode):
        self.operating_mode = operating_mode
        print(f"AC is running in {self.operating_mode} mode.")


class Chack_AC:
    def __init__(self,switch):
        self.switch = switch
        if self.switch == "yes":
            print(f"AC is on!")
            
            self.ac = AC("LD")
            
        else:
            print("AC is Tarn off!")
          

while True:

    switch = input("AC on? yes or no? : ")
    if switch.lower() == "yes":

        chack_ac =  Chack_AC(switch)
        print(f"AC temperature is {chack_ac.ac.temperature}°C!")

        ask =  input("\nWould you like to know or change anything about the AC? \n1. Set Temperature\n2. Change Temperature\n3. Change Mode \n4. Get Information \n5. Nothing \nEnter the number of your choice: ")
        while ask.lower() != "5":
            
            if ask == "1":
                temperature = input("Set the AC temperature? Say the temperature or no : ")
                if "no" != temperature:
                    temperature = int(temperature)
                    chack_ac.ac.set_temperature(temperature)
                    
            elif ask == "2":
                change_tem = input("How much AC temperature up or down? Or no? : ")
                while change_tem != "no":
                    change_tem = int(change_tem)
                    chack_ac.ac.change_temperature(change_tem)
                    change_tem = input("How much AC temperature up or down? Or no? : ")

            elif ask == "3":
                print(f"AC is running in {chack_ac.ac.operating_mode} mode.")
                change_mode = input("Want to changee mo AC mode? If yes, tell me the mode. If not, say No : ")
                if change_mode.lower() != "no" :
                    chack_ac.ac.change_mode(change_mode)

            elif ask == "4" :

                    information = Information()

            else:
                print("Sorry but i don't have that information!")

            ask =  input("\nWould you like to know or change anything about the AC? \n1. Set Temperature\n2. Change Temperature\n3. Change Mode \n4. Get Information \n5. Nothing \nEnter the number of your choice: ")


    if switch == "q":
        break           