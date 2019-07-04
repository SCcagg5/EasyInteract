class token:
    def __init__(self, token):
        self.tok = token

    def verify(self):
        return [True if self.tok == "ULTIMATE_TOKEN" else False, "Invalid token", 403]

    def login(self):
        return [True, {"token": "ULTIMATE_TOKEN"}, 200]
