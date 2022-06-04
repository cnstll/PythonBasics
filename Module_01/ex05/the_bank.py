class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

    def __setattr__(self, name: str, value=None) -> None:
        if name == "id":
            if value is None:
                self.__dict__[name] = int()
            else:
                self.__dict__[name] = int(value)
        elif name == "name":
            self.__dict__[name] = str(value)
        elif name == "value":
            if value is None:
                self.__dict__[name] = float()
            else:
                self.__dict__[name] = float(value)
        elif name == "addr":
            self.__dict__[name] = str(value)
        elif name == "zip":
            if value is None:
                self.__dict__[name] = int()
            else:
                self.__dict__[name] = int(value)
        else:
            self.__dict__[name] = value

    def __getattribute__(self, name: str):
        return object.__getattribute__(self, name)

    def __delattr__(self, name: str) -> None:
        if name in self.__dict__.keys():
            self.__dict__.pop(name)


class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def add(self, account):
        self.accounts.append(account)

    def get_account(self, attr):
        for type, a in [(int, 'id'), (str, 'name')]:
            if isinstance(attr, type):
                for account in self.accounts:
                    if account.__getattribute__(a) == attr:
                        return account
                else:
                    raise ValueError("Account not found")
        else:
            raise TypeError('"attr" must be a string or an int')

    def is_account_corrupted(self, account):
        attr = account.__dict__
        if any(a for a in ['id', 'name', 'value'] if a not in attr.keys()):
            return True
        elif len(attr) % 2 == 0:
            return True
        elif any(k[:1] == 'b' for k in attr.keys()):
            return True
        elif not (any(k[:3] == "zip" for k in attr.keys())
                  and any(k[:4] == "addr" for k in attr.keys())):
            return True
        return False

    def check_transfer_args(self, origin, dest, amount):
        if not isinstance(origin, (str, int)):
            raise TypeError("origin should be of type int(id) or str(name)")
        elif not isinstance(dest, (str, int)):
            raise TypeError("dest should be of type int(id) or str(name)")
        elif not isinstance(amount, float):
            raise TypeError("amount should be of type float(amount)")
        elif amount < 0:
            raise ValueError("amount transfered cannot be negative")
        else:
            return True

    def account_has_name(self, account):
        return 'name' in account.__dict__.keys()

    def account_has_id(self, account):
        return 'id' in account.__dict__.keys()

    def transfer(self, origin, dest, amount):
        """
                    @origin:  int(id) or str(name) of the first account
                    @dest:    int(id) or str(name) of the destination account
                    @amount:  float(amount) amount to transfer
                    @return         True if success, False if an error occured
        """
        self.check_transfer_args(origin, dest, amount)
        acc_origin = self.get_account(origin)
        acc_dest = self.get_account(dest)
        # Fixing account before transfer to avoid errors
        for account in [acc_origin, acc_dest]:
            if self.is_account_corrupted(account):
                if self.account_has_name(account):
                    if not self.fix_account(account.name):
                        return False
                elif self.account_has_id(account):
                    if not self.fix_account(account.id):
                        return False
                else:
                    return False
            else:
                continue
        if acc_origin.value >= amount:
            acc_origin.value -= amount
            acc_dest.transfer(amount)
        else:
            return False
        return True

    def fix_account(self, account):
        """
                fix the corrupted account
                @account: int(id) or str(name) of the account
                @return         True if success, False if an error occured
        """
        current_account = self.get_account(account)
        attributes = current_account.__dict__
        for a in ['id', 'name', 'value']:
            if a not in attributes.keys():
                current_account.__setattr__(a,)
        cpy = attributes.copy()
        for a in cpy.keys():
            if a[:1] == 'b':
                current_account.__delattr__(a)
        if not any(k[:3] == "zip" for k in attributes.keys()):
            current_account.__setattr__("zip", 75017)
        if not any(k[:4] == "addr" for k in attributes.keys()):
            current_account.__setattr__("addr", "96 Boulevard Bessières")
        if len(attributes) % 2 == 0:
            return False
        else:
            return True


if __name__ == '__main__':
    bigBank = Bank()
    a1 = Account("Howard", value=42)
    a2 = Account("Billy", zip="75012", blop=42, blip=24)
    print("Init account 1: ", a1.__dict__)
    print("Init account 2: ", a2.__dict__)
    print()
    bigBank.add(a1)
    bigBank.add(a2)
    bigBank.fix_account(a1.id)
    bigBank.fix_account(a2.name)
    print("Fixed account: ", a1.__dict__)
    print("Fixed account: ", a2.__dict__)
    print()
    print("Transfer Result: ", bigBank.transfer(a2.name, a1.name, 40.0))
    print("Transfer Result: ", bigBank.transfer(a1.id, a2.name, 40.0))
    print()
    print("Post Transfer account", a1.__dict__)
    print("Post Transfer account", a2.__dict__)
    print()
    print("Manual delete of name: ", a1.__dict__)
    bigBank.accounts[0].__dict__.pop('name')
    bigBank.fix_account(a1.id)
    print("Post fix account", a1.__dict__)
