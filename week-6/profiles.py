
from users import User

class Profile(User):

    def __init__(self, user_id):
        super().__init__()
        all_users = self.get_data()
        for user in all_users:
            if user['username'] == user_id:
                self.__profile_data = user
                break
        self.__password = self.__profile_data['password']
    
    @property
    def firstname(self):
        return self.__profile_data['firstname'].title()

    @property
    def lastname(self):
        return self.__profile_data['lastname'].title()

    @property
    def username(self):
        return self.__profile_data['username']

    @property
    def phone_number(self):
        return self.__profile_data['phone_number']

    @property
    def address(self):
        return self.__profile_data['address']

    @property
    def date_of_birth(self):
        return self.__profile_data['dob']

    @property
    def gender(self):
        return self.__profile_data['gender']
    
    def change_password(self):
        return super().change_password(self.firstname, self.lastname, self.username, self.__password)
    
    def edit_profile(self):
        return super().edit_profile(self.username, self.__password)


profile = Profile("luqman")
profile.edit_profile()