from datetime import timedelta
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import auth, crud, database as models, schemas
from ..config import Settings
from ..dependencies import get_db

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
    responses={401: {"description": "User not authenticated"}},
)


@router.post("/token", response_model=schemas.Token, tags=["Admin Authentication"])
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    """Login an admin user to get a JWT access token."""
    user = crud.get_user_by_username(db, username=form_data.username)
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    settings = Settings()
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post(
    "/users/", response_model=schemas.User, tags=["Admin User Management"]
)
async def create_admin_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Create a new administrative user. In a real application, this endpoint
    should be heavily protected or used only for initial setup.
    """
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)


@router.get(
    "/users/me", response_model=schemas.User, tags=["Admin User Management"]
)
async def read_users_me(
    current_user: models.User = Depends(auth.get_current_active_user),
):
    """Get details for the currently authenticated user."""
    return current_user


@router.post(
    "/keys/",
    response_model=schemas.APIKeyCreateResponse,
    tags=["Admin API Key Management"],
)
async def create_new_api_key(
    key_in: schemas.APIKeyCreate,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db),
):
    """Generate a new API key for the authenticated user."""
    result = crud.create_api_key(db=db, key=key_in, user_id=current_user.id)
    return schemas.APIKeyCreateResponse(name=result["db_key"].name, key=result["key"])


@router.get(
    "/keys/", response_model=List[schemas.APIKey], tags=["Admin API Key Management"]
)
async def list_api_keys(
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db),
):
    """List all active and inactive API keys for the authenticated user."""
    return crud.get_user_api_keys(db=db, user_id=current_user.id)


@router.delete(
    "/keys/{prefix}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Admin API Key Management"],
)
async def revoke_api_key(
    prefix: str,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db),
):
    """Revoke (deactivate) an API key by its prefix."""
    db_key = crud.deactivate_api_key(db=db, prefix=prefix, user_id=current_user.id)
    if not db_key:
        raise HTTPException(status_code=404, detail="API Key not found")
    return None