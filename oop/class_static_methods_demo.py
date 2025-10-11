# class_static_methods_demo.py

class Calculator:
    # Class attribute shared by all instances
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method:
        - Does not access class or instance (no self or cls)
        - Used for utility functions related to the class logic
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method:
        - Takes the class itself as the first parameter (cls)
        - Can access or modify class-level attributes
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
