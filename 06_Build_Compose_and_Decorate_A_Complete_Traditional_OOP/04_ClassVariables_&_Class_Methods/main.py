# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name)
#  that allows changing the bank name. Show that it affects all instances.




class Bank:
    bank_name = "Bank of America"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name



bank1 = Bank()
print(bank1.bank_name)

Bank.change_bank_name("Bank of India")

bank2 = Bank()
print(bank2.bank_name)




