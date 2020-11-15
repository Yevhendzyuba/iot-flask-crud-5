class CosmetologyBuild:
    def __init__(self,name_of_cosmetology=None,appoinment_for=None,produce_country=None,capacity_in_ml=None,price_in_uah=None):
        self.name_of_cosmetology = name_of_cosmetology
        self.appoinment_for = appoinment_for
        self.produce_country = produce_country
        self.capacity_in_ml = capacity_in_ml
        self.price_in_uah = price_in_uah
    
    def __str__(self):
        return f"NameOfCosmetology:{self.name_of_cosmetology} AppoinmentFor:{self.appoinment_for} ProduceCountry:{self.produce_country} CapacityInMl:{self.capacity_in_ml} PriceInUAH:{self.price_in_uah}"

