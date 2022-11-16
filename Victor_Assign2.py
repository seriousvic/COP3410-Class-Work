class CreditCard:
    """A consumer credit card."""  # docstring, the first set of comments after the name of class is considered the

    def __init__(self, customer, bank, acnt, limit, balance=0):  # the constructor is the very first method, 2.7: I
        # added a new parameter here titled balance = 0 to have the starting balance always be 0
        """Create a new credit card instance.

        The initial balance is zero.

        customer: the name of the customer (e.g., John Bowman )
        bank: the name of the bank (e.g., California Savings )
        acnt: the account identifier (e.g., 5391 0375 9387 5309 )
        limit: credit limit (measured in dollars)"""

        self._customer = customer  # anything with self in front of it is private
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance  # refer to line 6, new parameter
        self._charge_count = 0

    def get_customer(self):  # the get functions are a must, they're called accessor functions (methods)
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied."""
        if not isinstance(price, (int, float)):
            raise TypeError('Price must be a number')
        if price + self._balance > self._limit:  # if charge would exceed limit, 2.8: modified declaration of for
            # loop and California Finance is the first to go over credit limit
            print(f'Credit card with account number {self._account} denied. Balance exceeded limit.')
            return False  # cannot accept charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        if not isinstance(amount, (int, float)):
            raise TypeError('Amount must be a number')
        elif amount < 0:
            raise ValueError('Payment cannot be a negative number')
        self._balance -= amount


if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500))
    wallet.append(CreditCard('John Bowman', 'California Federal', '3485 0399 3395 1954', 3500))
    wallet.append(CreditCard('John Bowman', 'California Finance', '5391 0375 9387 5309', 5000))

    for val in range(1, 59):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)

    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New Balance =', wallet[c].get_balance())
        print()


class ModernCreditCard(CreditCard):  # predatory credit card that charges fees

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new credit card instance.

          The initial balance is zero.

          customer: the name of the customer (e.g., John Bowman )
          bank: the name of the bank (e.g., California Savings )
          acnt: the account identifier (e.g., 5391 0375 9387 5309 )
          limit: credit limit (measured in dollars)
          apr annual percentage rate (e.g., 0.0825 for 8.25% APR)"""

        super().__init__(customer, bank, acnt, limit)  # call super constructor
        self.apr = apr

        def make_purchase(purchase):  # may not be fully operation yet
            """Charge given price to the card, assuming sufficient credit limit
            Return True if charge was processed.
            Return False and assess 5 dollar fee if charge is denied."""

            success = super().make_purchase(purchase)  # inherited method
            if not success:
                self.balance += 5
            return success

    def process_month(self):
        """Assess monthly interest on outstanding balance"""
        if self.balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self.apr, 1 / 12)
            self.balance = monthly_factor


class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeroes."""
        if isinstance(d, int):
            self._coords = [0] * d
        else:
            try:
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('Invalid parameter type')

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return the sum of two vectors."""
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError('Dimensions must agree')
        result = Vector(len(self))  # start with vector of zeroes
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as others."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from others."""
        return not self == other  # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation

    def __lt__(self, other):
        """Compare vectors in order."""
        if len(self) != len(other):
            raise ValueError('Dimensions must agree')
        return self._coords < other._coords

    def __le__(self, other):
        """Compare vectors in order."""
        if len(self) != len(other):
            raise ValueError('Dimensions must agree')
        return self._coords <= other._coords

    def __sub__(self, other):  # 2.9
        """Return the subtraction of two vectors"""
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError('Dimensions must agree')
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):  # 2.10
        """Return copy of vector with all coordinates negated."""
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = -self[j]
        return result

    def __rmul__(self,
                 factor):  # 2.11 and 2.13, the vector is revised this way by using rmul which while mul looks at the
        # left-hand operator the rmul operator looks at the right-hand operator helping it accept the syntax
        """Return the product of two vectors from the right-hand side"""
        result = Vector(len(self))  # start with vector of zeroes
        for j in range(len(self)):
            result[j] = factor * self[j]
        return result

    def __mul__(self, other):  # 2.11 and 2.13 and 2.14, the vector is revised this way by using rmul which while mul
        # looks at the left-hand operator the rmul operator looks at the right-hand operator helping it accept syntax
        """Return product of two vectors"""
        if not isinstance(other, (int, float, Vector, list)):
            raise ValueError('factor must be a number or vector')
        if isinstance(other, (int, float)):
            product = Vector(len(self))
            for j in range(len(self)):
                product[j] = self[j] * other
            return product
        elif len(self) != len(other):
            raise ValueError('dimensions must agree')
        else:
            dot_product = 0
            for i in range(len(self)):
                dot_product += self[i] * other[i]
            return dot_product


if __name__ == '__main__':
    # the following demonstrates usage of a few methods
    v = Vector(5)  # construct five-dimensional <0, 0, 0, 0, 0>
    v[1] = 23  # <0, 23, 0, 0, 0> (based on use of __setitem__)
    v[-1] = 45  # <0, 23, 0, 0, 45> (also via __setitem__)
    print(v[4])  # print 45 (via __getitem__)
    u = v + v  # <0, 46, 0, 0, 90> (via __add__)
    print(u)  # print <0, 46, 0, 0, 90>
    w = v - u
    print(w)
    total = 0
    for entry in v:  # implicit iteration via __len__ and __getitem__
        total += entry
