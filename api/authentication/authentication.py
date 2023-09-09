from sqlalchemy.orm import Session
from model import user as modelUser
from authentication.password import verify_password, generate_token
from datetime import datetime, timedelta

def authenticate(email: str, password: str, db: Session) -> modelUser.User | None:
    user = db.query(modelUser.User).filter(modelUser.User.email == email).first()

    if user is None:
        return None
    
    if not verify_password(password, user.pass_user):
        return None
    
    return user

def create_access_token(user: modelUser.User, db: Session) -> modelUser.AccessToken:
    tomorrow = datetime.now() + timedelta(days=1)
    accessToken = modelUser.AccessToken(user_id =user.id, expiration_date=tomorrow, access_token=generate_token())

    db.add(accessToken)
    db.commit()
    db.refresh(accessToken)

    return accessToken