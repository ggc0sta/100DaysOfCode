class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # defining default value to attribute
        self.following = 0
        print(f"User {username} being created...")

    def follow(self, user):  # self parameter should be added to all methods
        self.following += 1
        user.followers += 1


user_1 = User("001", "Lola")
user_2 = User("002", "Fogo")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

