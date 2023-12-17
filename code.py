
class Customer:
    all = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.add_all_names_to_all(given_name, family_name)

    def given_name(self):
        return f"{given_name}"

    def family_name(self):
        return f"{family_name}"
    
    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def add_all_names_to_all(cls, given_name, family_name):
        cls.all.append([given_name,family_name])


customer1 = Customer("John", "Doe")
customer2 = Customer("Mary", "Agness")
customer3 = Customer("josy", "morghess")
print(Customer.all)


class Review(Customer):

    all = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating 
        Review.add_all_reviews(customer, restaurant, rating)

    def rating(self):
        return f"The review is rated as a {rating}."

    def customer(self):
        for i in super().all:
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


class Restaurant(Review):

    def __init__(self, name):
        self.name = rest_name
    
    def name(self):
        return f"{rest_name}"
    
    def reviews(self):
        review_list = []
        for i in super().all:
            if i[1] == self.name:
                review_list.append(i)
        return review_list

    def customers(self):
        cust_list=[]
        for i in super().all:
            if i[1] == self.name:
                cust_list.append(i[0])
        return cust_list
    

