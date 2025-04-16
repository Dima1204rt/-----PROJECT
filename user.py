from dataclasses import dataclass

@dataclass
class User:
    email: str = ''
    login: str = ''
    password: str = ''

    def to_tuple(self):
        return (
            self.email,
            self.login,
            self.password
        )
    @classmethod 
    def from_tuple(cls, data):
        return cls(*data)
    