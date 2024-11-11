class Value:
    def __init__(self, data, label=''):
        self.data = data
        self.grad = 0.0
        self.label = label
        self._backward = lambda: None
        self._prev = set()

    def __repr__(self):
        return f"value(data={self.data}, grad={self.grad})"

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data)
        
        def _backward():
            self.grad += out.grad
            other.grad += out.grad
        out._backward = _backward
        out._prev = {self, other}
        return out