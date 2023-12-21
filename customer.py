
class Customer():
    all = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.add_all_names_to_all(given_name, family_name)
        Customer.find_by_name(given_name)

    def given_name(self):
        return f"{given_name}"

    def family_name(self):
        return f"{family_name}"
    
    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    
    def restaurants(self):
        from reviews import Review 
        customer_reviewed = []
        for i in Review.all:
            if i['customer'] == self.given_name:
                customer_reviewed.append(i)
        return customer_reviewed
    
    def add_review(self, restaurant, rating):
        from reviews import Review 
        new_review = [Review.customer, restaurant, rating]
        Review.all.append(new_review)
    
    def num_reviews(self):
        from reviews import Review 
        for i in Review.all:
            count = 0
            if i[0] == self.given_name:
                count +=1
        return count

    @classmethod
    def add_all_names_to_all(cls, given_name, family_name):
        cls.all.append([given_name,family_name])

    @classmethod
    def find_by_name(cls, given_name):
        for i in cls.all:
            if given_name == i[0] + i[1]:
                found_user = i
                return found_user

    def find_all_by_given_name(cls, given_name):
        given_name_list = []
        for i in cls.all:
            if given_name == i[0]:
                given_name_list.append(i)
            return given_name_list

customer1 = Customer("John", "Doe")
customer2 = Customer("Mary", "Agness")
customer3 = Customer("josy", "morghess")
print(Customer.all)