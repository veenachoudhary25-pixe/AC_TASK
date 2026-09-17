from AC import *
class AC:
    def __init__(self,ac_name):
        self.ac_name = ac_name
        self.operating_mode = "Cooling Mode"
        self.temperature = 20

    def set_temperature(self,temperature):
        self.temperature = temperature
        print(f"AC temperature is {self.temperature}°C!")
        with open(filename_tem, 'w') as file_name_t:
            file_name_t.write(f"\nAC temperature is {temperature}°C!")
        disn["temperature"]= temperature
        if 'operating_mode' in disn:
            del disn['operating_mode']

    def change_temperature(self,change_temperatures):
        self.change_temperatures = change_temperatures
        self.temperature += self.change_temperatures
        print(f"AC temperature is {self.temperature}°C!")
        with open(filename_tem, 'w') as file_name_t:
            file_name_t.write(f"\nAC temperature is {self.temperature}°C!")
        disn["temperature"]= self.temperature
        if 'operating_mode' in disn:
            del disn["operating_mode"]


    def change_mode(self,change_mode,):
            
            if change_mode == 1:
                self.operating_mode = "Cooling Mode"
                self.temperature = 20
    
            elif change_mode == 2:
                self.operating_mode = "Dry Mode"
                self.temperature = 25
    
            elif change_mode == 3:
                self.operating_mode = "Fan Mode"
                self.temperature = 28
    
            elif change_mode == 4:
                self.operating_mode = "Auto Mode"
                self.temperature = 24
    
            elif change_mode == 5:
                self.operating_mode = "Heat Mode"
                self.temperature = 30
                    
            print(f"AC is running in {self.operating_mode} mode.")
            print(f"AC temperature is {self.temperature}°C!")
            with open(filename_tem, 'w') as file_name_t:
                file_name_t.write(f"\nAC temperature is {self.temperature}°C!")
            disn["temperature"]= self.temperature
            

            with open(filename_mode, 'w') as file_name_m:
                file_name_m.write(f"\nAC temperature is {self.operating_mode} mode.")
            disn["operating_mode"]= self.operating_mode
            

class Chack_AC:
    def __init__(self,switch):
        self.switch = switch
        if self.switch == "yes":
            print(f"AC is on!")
            
            self.ac = AC("LD")
            self.disn = {}
            
        else:
            print("AC is Tarn off!")

filename_tem = "/home/ng/Task/temperature.txt"
filename_mode = "/home/ng/Task/mode.txt"
# filename_info = "/home/ng/Task/information.txt"
list = []
disn = {}
while True:

    switch = input("AC on? yes or no? : ")
    if switch.lower() == "yes":

        chack_ac =  Chack_AC(switch)
        with open(filename_tem, 'r') as file_name_t:
            content = file_name_t.read()
            print(content)

        with open(filename_mode, 'r') as file_name_m:
            content = file_name_m.read()
            print(content)


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
                # print(f"AC is running in {chack_ac.ac.operating_mode} mode.")
                change_mode = int(input("Please select the AC mode:\n1. Cooling Mode — 20°C\n2. Dry Mode — 25°C \n3. Fan Mode — 28° \n4. Auto Mode — 24°C \n5. Heat Mode — 30°C \n6. Nothing \nEnter the option number (1–6):"))
                if change_mode != 6 :
                    chack_ac.ac.change_mode(change_mode)
                    
            elif ask == "4" :

                    information = Information()
                    
            else:
                print("Sorry but i don't have that information!")

            import json
            
            list.append(disn)
            filename = 'numbers.json'
            with open(filename, 'w') as f_obj:
                json.dump(disn, f_obj)
                # f_obj.write(',')
            ask =  input("\nWould you like to know or change anything about the AC? \n1. Set Temperature\n2. Change Temperature\n3. Change Mode \n4. Get Information \n5. Nothing \nEnter the number of your choice: ")
        

    if switch == "q":
        break      
    elif switch.lower() != "no" and switch.lower() != "yes":
        print("Please enter only yes, no, or q.")
