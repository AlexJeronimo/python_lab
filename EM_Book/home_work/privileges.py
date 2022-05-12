from user import User


class Privileges:
    def __init__(self):
        self.privileges = ['read_host', 'write_host', 'add_data', 'delete_data']

    def set_privileges(self):
        q = False
        while not q:
            print("Type an privilege you want to assign to Admin user role. For exit type 'q': ")
            p = input()
            if p == 'q':
                q = True
            else:
                self.privileges.append(p)

    def get_privileges(self):
        print(f"Admin has privileges: {self.privileges}")


class Admin(User):
    def __init__(self, first_name, last_name, job_title, room):
        super().__init__(first_name, last_name, job_title, room)
        self.privileges = Privileges()
