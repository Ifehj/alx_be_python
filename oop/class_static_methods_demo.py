# class_static_methods_demo.py

class Calculator:
    calculation_type = "Arithmetic Operations"  # Class attribute

    @staticmethod
    def add(a, b):
        return a + b  # Performs addition without needing class or instance

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")  # Accesses class attribute
        return a * b  # Performs multiplication
