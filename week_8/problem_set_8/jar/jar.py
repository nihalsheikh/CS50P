# Week 8: Problem 2
# make class `Jar`
class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._n = 0  # Number of cookies in the jar

    def __str__(self):
        return self._n * "🍪"

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies.")
        if self._n + n > self._capacity:
            raise ValueError("Deposit exceeds jar capacity")
        self._n += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies.")
        if n > self._n:
            raise ValueError("Not enough cookies in jar")
        self._n -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._n


def main():
    jar = Jar()
    jar.deposit(2)
    print(jar)
    jar.deposit(8)
    # jar.withdraw(2)
    print(jar)

if __name__ == "__main__":
    main()
