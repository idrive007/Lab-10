#!/usr/bin/env python
# coding: utf-8

# In[1]:


class BasicCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    # Калькулятор не має методів для множення та ділення

class AdvancedCalculator(BasicCalculator):
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

# Використання підкласу
calculator = AdvancedCalculator()
print("Addition: ", calculator.add(5, 3))
print("Subtraction: ", calculator.subtract(5, 3))
print("Multiplication: ", calculator.multiply(5, 3))
print("Division: ", calculator.divide(5, 3))


# In[ ]:




