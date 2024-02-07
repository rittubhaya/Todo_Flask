class Computations:
    @staticmethod
    def calculate_sum(a, b):
        return a + b

    @staticmethod
    def calculate_difference(a, b):
        return a - b

    @staticmethod
    def calculate_product(a, b):
        return a * b

    @staticmethod
    def calculate_quotient(a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"