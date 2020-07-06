class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    def __iadd__(self, amount):
        self._transactions.append(amount)
        return self

    def __isub__(self, amount):
        self._transactions.append(amount)
        return self

    def __repr__(self):
        return f'{self.name} - balance: {self.balance}'
