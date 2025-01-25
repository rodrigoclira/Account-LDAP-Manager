
class LDAPAccountDTO:
    def __init__(self, dn, attributes):
        self.dn = dn
        self.attributes = attributes

    def __str__(self):
        return f"dn: {self.dn}, attributes: {self.attributes}"