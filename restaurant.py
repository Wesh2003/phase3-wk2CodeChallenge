
class Restaurant():

    def __init__(self, name):
        self.name = name
    
    def name(self):
        return f"{name}"
    
    def reviews(self):
        from reviews import Review 
        review_list = []
        for i in Review.all:
            if i[1] == self.name:
                review_list.append(i)
            return review_list

    def customers(self):
        from reviews import Review 
        cust_list=[]
        for i in Review.all:
            if i[1] == self.name:
                cust_list.append(i[0])
            return cust_list
    
    def average_star_rating(self):
        from reviews import Review 
        count = 0
        for i in Review.all:
            if self.name == i[1]:
                count += i[2]
        average = count / len(Review.all)
        return average
    
restaurant1 = Restaurant("Big Shack")
print(restaurant1.name)
