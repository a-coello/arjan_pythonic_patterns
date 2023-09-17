# arjan_pythonic_patterns
Course pythonic patterns
https://www.arjancodes.com/products/the-software-designer-mindset-pythonic-patterns

# Strategy Pattern

Used when we have plenty of ifs and constant numbers that could be changed in the future, like the percentage of discount or the fixed discount.


```python
    discount_type: str) -> int:
        if discount_type == "percentage":
            discount = int(self.price * self.quantity * 0.20)
        elif discount_type == "fixed":
            discount = 10_00
        else:
            discount = 0
        return self.price * self.quantity - discount
```

