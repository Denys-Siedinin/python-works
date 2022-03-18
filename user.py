class User:
    """user description"""

    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location.title()

    def describe_user(self):
        user_info = {
            'User name': self.first_name,
            'User surname': self.last_name,
            'Age': self.age,
            'location': self.location,
            }
        for k, v in user_info.items():
            print(f'{k}: {v}')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}. How are you?')
        answer = input('(write your answer) \n')
        if answer == 'fine':
            print('It is fine')
        elif answer == 'bad':
            print('I am sorry')
        else:
            print('Something wrong...')


my_user = User('denys', 'siedinin', 'almost 32', 'kharkiv')
my_user.describe_user()

sveta_user = User('sveta', 'kachalo', 'almost 32', 'kharkiv')
sveta_user.describe_user()