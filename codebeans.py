# python
import random

class Product :

    def __init__(self, name, price = 30, size = 20 , warmness = 0.5 ,sweetness = 0.5) :
        self.name = name
        self.price= int(price)
        self.size = int(size)
        self.warmness = float(warmness)
        self.sweetness = float(sweetness)
        self.identifier = random.randint(1000000,9999999)

    # @Instancemethod
    def sellability(self) :

        sellability_ = self.size / self.price
        sellability_string = ""
        
        if sellability_ >= 0.5 and sellability_ <= 1.0 :
            sellability_string = "Kinda sellable"
        elif sellability_ < 0.5 :
            sellability_string = "Not to sellable.."
        elif sellability_ > 1.0 :
            sellability_string = "Very Sellable!"

    # @Instancemethod
    def calory(self) :
        calory_ = self.size * self.sweetness
        calory_string = ""

        if calory_ > 50  :
            calory_string = "It's really heavy..!!"
        elif calory_ >= 10 and calory_ <= 50 :
            calory_string = "It's adequate."
        elif calory_ < 10 :
            calory_string = "...It's light"
        
        return calory_string
    
    pass 

class Tea(Product) : 

    def __init__(self, name, price = 30, size = 10 , warmness = 0.5 ,sweetness = 0.5) :
        #super() 를 통해 부모 메소드에 접근 
        super().__init__(name, price, size, warmness,sweetness)
        #부모클래스를 명시적으로 접근하여 호출
        # Product.__init__(self,name, price, size, warmness,sweetness)


    @staticmethod
    def calory() :
        calory_string = "...It's a tea. Only a few calories"

        return calory_string

    def drink(self) : 
        sweetness_string = ""
        if self.sweetness >= 1.0  :
            sweetness_string = "It's too hot!!"
        elif self.sweetness >= 0.5 and self.sweetness < 1.0 :
            sweetness_string = "Oh, It's warm..!"
        elif self.sweetness < 0.5 :
            sweetness_string = "It's too cold.."

        return sweetness_string
    
    pass 
