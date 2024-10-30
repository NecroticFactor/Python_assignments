class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        return ("🍪" * (self.size))


    def deposit(self, n):
        if n <= 0:
            raise ValueError("Deposit amount must be positive")
        if self.size + n > self.capacity:
            raise ValueError("Exceeded jar capacity")
        self.size += n


    def withdraw(self, n):
        if 0 < n <= self.size:
           self.size -= n
        else:
            raise ValueError("Not enough cookies in the jar")


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity



    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("Size cannot be negative")
        self._size = size


def main():
    new_jar = Jar()
    new_jar.deposit(2)
    print(str(new_jar))


if __name__ == "__main__":
    main()
