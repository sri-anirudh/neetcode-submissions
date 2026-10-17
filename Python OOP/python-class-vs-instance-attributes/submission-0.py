class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    tot_bal=0
    tot_acc=0
    
    def __init__(self, name:str, balance:int) -> None:
        self.name=name
        self.balance = balance
        BankAccount.tot_acc+=1
        BankAccount.tot_bal+=balance

Alice=BankAccount('Alice',1000)

Bob=BankAccount('Bob',2000)


# TODO: Create two accounts

# TODO: Print the information using the mentioned format

print(f"Alice's balance: ${Alice.balance}")
print(f"Bob's balance: ${Bob.balance}")
print(f"Total Accounts: {BankAccount.tot_acc}")
print(f"Total Balance: ${BankAccount.tot_bal}")