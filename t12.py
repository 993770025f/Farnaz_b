class Brand:
    brand_1="Amazon"
    brand_2="Ebay"
    brand_3="Olx"
class Product:
    prod_1="online E commerce"
    prod_2="online store"
    prod_3="online buy"
class Popularity(Brand,Product):
    prod1_pop=100
    prod2_pop=70
    prod3_pop=50
obj=Popularity()
print(obj.brand_1,"is a",obj.prod_1)
