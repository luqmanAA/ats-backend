import csv, os, pandas as pd

class User:

    file_path = r'week-4\user_wallet.csv'
    headers = ['firstname', 'lastname', 'username', 'password', 'wallet_balance', 'transaction']
    
    def __init__(self, firstname = None, lastname = None, username = None, password = None):
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
    
    def save_user_data(self, firstname, lastname, username, password):
        with open(self.file_path, 'a+') as f:
            writer = csv.DictWriter(f, fieldnames=self.headers)
            if os.stat(self.file_path).st_size == 0:
                writer.writeheader()
            writer.writerow({
                'firstname': firstname,
                'lastname': lastname,
                'username': username,
                'password': password
                })

    def get_user_data(self):
        with open(self.file_path, 'r') as f:
            reader = csv.DictReader(f)
            return (list(reader))

    def add_user(self):
        return self.save_user_data(self.__firstname, self.__lastname, self.__username, self.__password)

    def delete_user(self):
        df = pd.read_csv(self.file_path)
        data = self.get_user_data()
        for i in data:
            if i['username'] == self.username:
                df.drop(index=data.index(i))
                break
        return df.to_csv(self.file_path, index=False)

        # new_data = []
        # with open(self.file_path, 'r') as f:
        #     reader = csv.DictReader(f)
        #     for data in reader:
        #         if (data['username'] == self.__username):
        #             del(data)
        #             continue
        #         new_data.append(data)
        # return(new_data)


class Wallet(User):

    def __init__(self):
        super().__init__()
        self.wallet_balance = 0
    
    @property
    def wallet_balance(self):
        return self.__wallet_balance

    @wallet_balance.setter
    def wallet_balance(self, wbalance):
        if wbalance < 0:
            raise ValueError('Amount cannot be negative.')
        self.__wallet_balance = wbalance
    
    def fund_wallet(self, amount):
        self.__wallet_balance += amount
        df = pd.read_csv(self.file_path)
        data = self.get_user_data()
        for i in data:
            if i['username'] == self.username:
                df.loc[data.index(i), 'wallet_balance'] = self.__wallet_balance
        
        return df.to_csv(self.file_path, index=False)


    def get_balance(self):
        pass


class Transaction(User):

    def log_transaction(self):
        pass    


# user1 = User("Lukman", "Abisoye", 'luqman', '123456')
# user2 = User("Adewale", "Ola", 'adeola', "12345")
# user1.add_user()
# user2.add_user()

# user2.delete_user()

wallet1 = Wallet()
# wallet2 = Wallet("Adewale", "Ola", 'adeola', "12345")


# wallet1.add_money(200)
# wallet1.add_money(100)
# wallet1.add_money(50)

# wallet2.add_money(5000)
# wallet2.add_money(4000)


