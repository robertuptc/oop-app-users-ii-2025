class User:
    all_posts = {}

    def __init__(self, name, email, posts=None, drivers_license = None):
        self.name = name
        self.email = email
        self.drivers_license = drivers_license
        self.posts = posts if posts is not None else []

    def __str__(self):
        return f"New user {self.name} with email {self.email} created!"

    
    @property
    def get_posts(self):
        return self.posts

    @get_posts.setter
    def get_posts(self, new_post):
        self.posts.append(new_post)
        
        User.all_posts[self.name] = self.posts

    @staticmethod
    def get_all_posts():
        return User.all_posts

    @classmethod
    def set_all_posts(cls):
        return cls.all_posts


user_one = User('Triton', 'triton@woof.com')
print(user_one)
print(user_one.get_posts)

user_one.get_posts = "First post"
print(user_one.get_posts)

user_one.get_posts = "Second post"
print(user_one.get_posts)

user_two = User("Mike", "mike@mail.com")
user_two.get_posts = "I have posted one"
user_two.get_posts = "I have posted two"

print(User.get_all_posts())

