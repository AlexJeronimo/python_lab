class User:
    def __init__(self, first_name, last_name, job_title, room):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.room = room

    def describe_user(self):
        print(f"The User {self.first_name} {self.last_name} works as {self.job_title} in {self.room} room")

    def greet_user(self):
        print(f"{self.first_name} {self.last_name} Welcome to our company in {self.job_title} role.")