filename_info = "/home/ng/Task/information.txt"
class Basic_Specifications:
    def __init__(self,AC_brand,warranty,power_consumption,tonnage,star_rating):
        self.ac_brand = AC_brand
        self.warranty = warranty
        self.power_consumption = power_consumption
        self.tonnage = tonnage
        self.star_rating = star_rating
        self.suitable_sizes = "Suitable Sizes"

    def ac_information(self):
        print(f"This AC is from the {self.ac_brand} brand.")
        print(f"It comes with a {self.warranty}years warranty.")        
        print(f"This is a {self.tonnage} Ton AC, suitable for the required cooling capacity.")
        print(f"It has a {self.star_rating}-Star Rating, which shows its energy efficiency.")

    def ac_features(self):
        print(f"Its power consumption is {self.power_consumption} watts, which helps you understand how much electricity it uses.")
        print(f"This AC is available in {self.suitable_sizes} for different room sizes.")


class Advanced_Feature(Basic_Specifications):
    def __init__(self, AC_brand, warranty, power_consumption, tonnage, star_rating):
        super().__init__(AC_brand, warranty, power_consumption, tonnage, star_rating)
        
    
    def smart_ai_features(self,s_features_list):
        self.s_features_list = s_features_list
        print(f"{self.ac_brand} comes with smart features like {', '.join(self.s_features_list)}.")
   

    def cleaning_and_maintenance_Features(self,cm_features_list):
        self.cm_features_list = cm_features_list
        print(f"It comes with cleaning and maintenance Features like {', '.join(self.cm_features_list)}.") 

    # def fill(self):
    #     with open(filename_info, 'w') as file_name_t:
    #         file_name_t.write(f"This AC is from the {self.ac_brand} brand. \nIt comes with a {self.warranty}years warranty.\nThis is a {self.tonnage} Ton AC, suitable for the required cooling capacity.\nIt has a {self.star_rating}-Star Rating, which shows its energy efficiency. \nIts power consumption is {self.power_consumption} watts, which helps you understand how much electricity it uses. \nThis AC is available in {self.suitable_sizes} for different room sizes.\n{self.ac_brand} comes with smart features like {', '.join(self.s_features_list)}. \nIt comes with cleaning and maintenance Features like {', '.join(self.cm_features_list)}.")   

    
class Information:
    def __init__(self):
            
        advanced_feature = Advanced_Feature("LC",1,1200,1.5,5)
        advanced_feature.ac_information()
        advanced_feature.ac_features()       
        s_features_list = ["AI Cooling","Smart Temperature Control","Wi-Fi Control","Voice Control","Smart Diagnosis"]
        advanced_feature.smart_ai_features(s_features_list)
        cm_features_list = ["Self-Clean","Auto-Clean","Anti-Dust Function","Filter Cleaning Reminder","Auto Dry"]
        advanced_feature.cleaning_and_maintenance_Features(cm_features_list)

        # advanced_feature.fill()
        # ac = AC("LC",1,1200,1.5,5)

        from contextlib import redirect_stdout



        with open(filename_info, "w") as file_name_t:
            with redirect_stdout(file_name_t):
                information = Information()
