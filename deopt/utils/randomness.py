import random
import string

class Randomness(object):
    def __init__(self, seed):
        self.seed = seed
        random.seed(self.seed)

    def get_initial_random_seed(self):
        return self.seed

    def get_random_integer(self, low, high):
        # high is inclusive
        return random.randint(low, high)

    def get_random_alpha_string(self, length):
        return "".join(random.choice(string.ascii_letters) for i in range(length))

    def get_upper_case_alpha_string(self, length):
        return "".join(random.choice(string.ascii_uppercase) for i in range(length))

    def get_lower_case_alpha_string(self, length):
        return "".join(random.choice(string.ascii_lowercase) for i in range(length))

    def get_first_upper_and_lower_case_alpha_string(self, length):
        return random.choice(string.ascii_uppercase) + "".join(random.choice(string.ascii_lowercase) for i in range(length - 1))  

    def get_random_alpha_numeric_string(self, length):
        return "".join(random.choice(string.ascii_letters + string.digits) for i in range(length))

    def get_seed(self):
        return self.seed

    def random_choice(self, list):
        return random.choice(list)

    def random_sample(self, list):
        return random.sample(list, self.get_random_integer(0, len(list)))

    def get_random_float(self, low, high):
        return str(self.get_random_integer(low,high)) + "." + str(self.get_random_integer(0,999))

    def flip_a_coin(self):
        return random.choice([0,1]) == 1
    
    def get_random_integer_list(self, low, high, number):
        return [self.get_random_integer(low, high) for i in range(number)]
    
    def get_random_string_list(self, number):
        return [self.get_random_alpha_numeric_string(self.get_random_integer(1, 10)) for i in range(number)]