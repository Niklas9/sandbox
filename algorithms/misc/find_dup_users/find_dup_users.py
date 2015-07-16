

class User(object):
    id = None
    email = None
    username = None

    def __init__(self, id, email, username):
        self.id = id
        self.email = email
        self.username = username

    def hash(self):
        return str(self.id) + self.email + self.username


def _fasdc(key, d):  # find and set dict count
    if key in d:
        d[key] += 1
        if d[key] == 2:
           return True 
    d[key] = 1
    return False
        

def find_dup_users(groups):
    dups = []
    user_dup_id_count = {}
    user_dup_email_count = {}
    user_dup_username_count = {}
    for group in groups:
        for user in group:
            id_check = _fasdc(user.id, user_dup_id_count) 
            email_check = _fasdc(user.email, user_dup_email_count) 
            username_check = _fasdc(user.username, user_dup_username_count) 
            if id_check or email_check or username_check:
                dups.append(user)
    return dups


a = User(id=1, email='1@neun.se', username='1')
b = User(id=2, email='2@neun.se', username='2')
c = User(id=3, email='1@neun.se', username='3')

m = find_dup_users
assert m([[a, b]]) == []
assert m([[a, a], [a]]) == [a]
assert m([[a], [b]]) == []
assert m([[a, c]]) == [c]
