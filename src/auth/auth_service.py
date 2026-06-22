from src.auth.jwt_handler import create_access_token

# Usuario simulado (luego esto será BD)
FAKE_USER = {
    "username": "admin",
    "password": "1234"
}


class AuthService:

    def login(self, username: str, password: str):

        if username == FAKE_USER["username"] and password == FAKE_USER["password"]:
            token = create_access_token({"sub": username})
            return {
                "access_token": token,
                "token_type": "bearer"
            }

        return None