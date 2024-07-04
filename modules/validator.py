import re


class Validator:

    def validate_name(name):
        return bool(re.match(r'^[A-Za-z]+$', name))

    def validate_mobile_number(mobile):
        return bool(re.match(r'^09\d{9}$', mobile))

    def validate_password(password):
        patterns = [
            r'.*[a-z].*',
            r'.*[A-Z].*',
            r'.*\d.*',
            r'.*[^a-zA-Z0-9].*',
            r'.{6,}'
        ]
        for pattern in patterns:
            if not re.match(pattern, password):
                return False
        return True

    def validate_email(email):
        pattern = r'^[a-zA-Z0-9]+@(gmail|yahoo)\.com$'
        return bool(re.match(pattern, email))

    def validate_username(username):
        return bool(re.match(r'^[A-Za-z0-9]+$', username))
