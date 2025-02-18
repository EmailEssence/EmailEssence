from fastapi import APIRouter, HTTPException
from app.services.user_service import get_user_by_token, update_user_preferences, list_users

# FastAPI router
router = APIRouter(prefix="/users", tags=["Users"])

# Get Current User (Using Google OAuth Token)
@router.get("/me")
async def get_current_user(token: str):
    """Retrieve user details using stored OAuth token"""
    try:
        return await get_user_by_token(token)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

# Update User Preferences
@router.put("/preferences")
async def update_preferences(token: str, preferences: dict):
    """Allows users to update their preferences"""
    try:
        return await update_user_preferences(token, preferences)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

# List All Users (Optional, Admin Use)
@router.get("/list")
async def list_all_users():
    """List all users (For admin use, can be restricted later)"""
    try:
        return await list_users()
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)