from fastapi import APIRouter
from app.services.user_service import get_or_create_user, update_user_preferences, list_users

# FastAPI router
router = APIRouter(tags=["Users"])

# Get Current User
@router.get("/me")
async def get_current_user():
    """Retrieve user details or create user if they don’t exist"""
    return await get_or_create_user()

# Update User Preferences
@router.put("/preferences")
async def update_preferences(preferences: dict):
    """Allows users to update their preferences"""
    return await update_user_preferences(preferences)

# List All Users (Debug Purposes)
@router.get("/list")
async def list_all_users():
    """List all users"""
    return await list_users()
