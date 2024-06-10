class NameTooShortError(Exception):
    """The name is equal or less than 4 symbols"""
    pass


class MustContainAtSymbolError(Exception):
    """If there's no @ in the e-mail"""
    pass


class InvalidDomainError(Exception):
    """If the domain name is invalid"""
    pass


data = input()
domain_names = ['bg', 'com', 'org', 'net']

while data != 'End':
    if '@' not in data:
        raise MustContainAtSymbolError("Email must contain @")
    else:
        at_index = data.find('@')
        name = data[:at_index]
        dot_index = data.find('.')
        domain = data[dot_index + 1:]

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    elif domain not in domain_names:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    else:
        print("Email is valid")
        data = input()
