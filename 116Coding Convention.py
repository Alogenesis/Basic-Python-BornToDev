use_small_cap_and_underscroll_only_for_variable = 0
user_name = 0
last_name = 0
user_height = 0
user_weight = 0
user_bmi = 0

'''Convention in function'''
#use small cap and underscroll only for var in function
def say_hello_world():
    print("Hello World in Function!!")
say_hello_world()

'''Class in OOP'''
#Use Camel Case Ex. UserAge / CustomerApp / SmallCapital
class CustomerApp:
    name = ""
    lastName = ""
    age = 0

    def add_cart(self):
        print("Added Product to ",self.name,self.lastName,"'s cart")

'''Always 2 Enter after class'''
customer_a = CustomerApp()
customer_a.name = "Winai"
customer_a.lastName = "Nob"
customer_a.add_cart()