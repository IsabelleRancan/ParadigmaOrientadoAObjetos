import hashlib


def has_lowercase_letter(s):
    for char in s:
        if char.islower():
            return True
    return False


def has_uppercase_letter(s):
    for char in s:
        if char.isupper():
            return True
    return False


class AuthException(Exception):
    def __init__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user


class UsernameAlreadyExists(AuthException):
    pass


class PasswordTooShort(AuthException):
    pass


class PasswordWithoutLowerCase(AuthException):
    pass


class PasswordWithoutUpperCase(AuthException):
    pass


class InvalidUsername(AuthException):
    pass


class InvalidPassword(AuthException):
    pass


class NotLoggedInError(AuthException):
    pass


class NotPermittedError(AuthException):
    pass


class PermissionError(Exception):
    pass


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password):
        password = self.username + password
        binary_password = password.encode()
        return hashlib.sha256(binary_password).hexdigest()

    def check_password(self, password):
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password


class Permission:
    def __init__(self, name):
        self.name = name
        self.users = []

    def add(self, username):
        self.users.append(username)

    def has_permission(self, username):
        return username in self.users


class Authenticator:
    def __init__(self):
        self.users = []

    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def add_user(self, username, password):
        if self.get_user(username):
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            raise PasswordTooShort(username)
        if not has_lowercase_letter(password):
            raise PasswordWithoutLowerCase(username)
        if not has_uppercase_letter(password):
            raise PasswordWithoutUpperCase(username)
        self.users.append(User(username, password))

    def login(self, username, password):
        user = self.get_user(username)
        if user is None:
            raise InvalidUsername(username)
        if not user.check_password(password):
            raise InvalidPassword(username, user)
        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        user = self.get_user(username)
        if user:
            return user.is_logged_in
        return False


class Authorizor:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = []

    def get_permission(self, perm_name):
        for permission in self.permissions:
            if permission.name == perm_name:
                return permission
        return None

    def add_permission(self, perm_name):
        if self.get_permission(perm_name):
            raise PermissionError("Permission Exists")
        self.permissions.append(Permission(perm_name))

    def permit_user(self, perm_name, username):
        permission = self.get_permission(perm_name)
        if permission is None:
            raise PermissionError("Permission does not exist")

        user = self.authenticator.get_user(username)
        if user is None:
            raise InvalidUsername(username)

        permission.add(username)

    def check_permission(self, perm_name, username):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)

        permission = self.get_permission(perm_name)
        if permission is None:
            raise PermissionError("Permission does not exist")

        if not permission.has_permission(username):
            raise NotPermittedError(username)

        return True


authenticator = Authenticator()
authorizor = Authorizor(authenticator)
