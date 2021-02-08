def is_recruiter(self):
    if str(self.user.is_staff) == 1:
        return True
    else:
        return False
rec_login_required = user_passes_test(lambda u: True if u.is_recruiter else False, login_url='/')

def recruiter_login_required(view_func):
    decorated_view_func = login_required(rec_login_required(view_func), login_url='/')
    return decorated_view_func