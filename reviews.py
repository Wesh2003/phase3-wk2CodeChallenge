

class Review():

    all = []
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating 
        Review.add_all_reviews(customer, restaurant, rating)

    def rating(self):
        return f"The review is rated as a {rating}."

    def customer(self):
        from customer import Customer
        for i in Customer.all:
            if i[0] or i[1] == self.customer:
                return i
        
        else:
            return "no such customer wrote a review"
        
    def restaurant(self):
        return f"{restaurant}"
    
    @classmethod
    def add_all_reviews(cls, cust, res, rat):
        cls.all.append([cust,res,rat])
    
review1 = Review("John", "The Alimore", 3)
review2 = Review("hunee", "Dominoes", 5)
review3 = Review("Kiko", "Kakkopoes", 2)
print (review1.customer)
print(Review.all)