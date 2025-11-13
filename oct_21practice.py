
#class featurephone():
#    def __init__(self,brand,model):
#        self.brand=brand
#        self.model=model

#    def make_call(self,number):
#        print(f"you are calling from {number} this {self.brand}")

#    def send_message(self,):
#        print(f"you sent hi from this {self.brand}")

#nokia=featurephone("nokia",2009)
#nokia.make_call(799539)
#nokia.send_message()

#class smartphone(featurephone):
#    def camera(self,phone):
#       print(f"you are taking pics from {phone} ")

#    def painting(self,):
#        print(f'you are painting from {self.brand} ')

#nokia=smartphone('nokia',2025)
#nokia.camera('pixel')
#nokia.painting()
#nokia.make_call(458999)
#nokia.send_message()
        
#class a():
#    def parent(self,):
#        print('this is parent class')
    
#class b(a):
#    def child1(self,):
#        print('this is child1 class')

#class c(a):
#    def child2(self,):
#        print('this child2 class')

#obj=b()
#obj.child1()
#obj.parent()

#obj=c()
#obj.child2()
#obj.parent()

#class parent1():
#    def father(self,):
#        print("this is father class")

#class parent2():  
#    def mother(self,):
#        print("this is mother class")

#class child(parent1,parent2):
#    def child(self,):
#        print('this is child class')

#obj=child()
#obj.child()
#obj.father()
#obj.mother()


#class gfather():
#    def gen1(self,):
#        print("this is first generation")

#class father(gfather):
#    def gen2(self,):
#        print("this is second generation")

#class son(father):
#    def gen3(self,):
#        print("this is third generation")

#obj=son()
#obj.gen3()
#obj.gen2()
#obj.gen1()

class customer():
    def __init__(self,name,age,gender,contactno):
        self.name=name
        self.age=age
        self.gender=gender
        self.contactno=contactno

    def show_cust_details(self,):
        print("customer details are as follows.....")
        print("")
        print("Name =",self.name)
        print("Age =",self.age)
        print("Gender =",self.gender)
        print("contact No =",self.contactno)

c=customer('gowtham',27,'male',77878)
c.show_cust_details()

