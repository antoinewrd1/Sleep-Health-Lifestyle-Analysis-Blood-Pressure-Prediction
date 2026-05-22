from fastapi import HTTPException, Header


API_KEY = "dev-secret-key"


def verify_api_key(x_api_key: str = Header(default=None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")

    return True