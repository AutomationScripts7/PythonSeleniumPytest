import json

class JSON_Reader:

    def __init__(self):
        with open("C:\\Users\\615074106\\PythonBasics\\Pytest\\TestData\\test_GS_Project.json") as file:
            self.data= json.load(file)


    def get_data(self, schema_name, key):
        return self.data[schema_name][key]

#step1 = self.data["gs_customer"]       # gets the nested dictionary
#step2 = step1["textboxSearch"]          # gets "ber" from that dictionary

#{
  #"gs_customer": {
   # "DiscountPromoCode": "rahulshettyacademy",
   # "textboxSearch": "ber"
 # }
#}