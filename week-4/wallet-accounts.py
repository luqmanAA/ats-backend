
class Wallet:

    def __init__(self) -> None:
        self.balance = 0
        self._log = []
    
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, wbalance):
        if wbalance < 0:
            raise ValueError('Amount cannot be negative.')
        self.__balance = wbalance
    
    def fund_wallet(self, amount):
        self.__balance += amount
        self._log.append(amount)
        return self.__balance


class Transaction(Wallet):
    
    def __init__(self) -> None:
        super().__init__()
        pass

    def log_transaction(self):
        if len(self._log) == 0:
            return "Your log is empty"
        for i in self._log:
            print(f"{i} was added to the wallet")

class User(Transaction):
    
    def __init__(self, firstname = None, lastname = None, username = None, password = None) -> None:
        super().__init__()
        
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
    
    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, fname):
        if fname == None:
            raise ValueError('Firstname cannot be empty')
        self.__firstname = fname

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lname):
        if lname == None:
            raise ValueError('Lastname cannot be empty')
        self.__lastname = lname

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, uname):
        if uname == None:
            raise ValueError('Username cannot be empty')
        self.__username = uname

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, psword):
        if psword == None:
            raise ValueError('Password cannot be empty')
        self.__password = psword

    def __del__(self):
        return("User deleted")

 
if __name__ == '__main__':

    #1 Create user 1
    user1 = User("Lukman", "Abisoye", "luqman", 123456)

    #Create user 2
    user2 = User("Adewale", "Ade", "adeola", 123456)


    #2 delete user 2
    # del(user2)

    #3 Fund wallet of user 1
    user1.fund_wallet(200)
    user1.fund_wallet(100)
    user1.fund_wallet(400)
    user1.fund_wallet(50)


    #4 Transaction log
    user1.log_transaction()

    