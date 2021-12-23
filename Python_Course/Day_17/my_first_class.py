# user_list = []


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    # def display_users(self):
    #     user ={
    #         "id": self.id,
    #         "username": self.username
    #     }
    #     user_list.append(user)
    #     print(user_list)


user_1 = User('001', 'Sai')
user_2 = User('002', 'Chandu')

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

