import httpx
from fastapi import HTTPException
from app.services.auth_service import get_credentials
from database import db  # MongoDB connection

# Fetch User Info from Google Using OAuth Token
async def get_google_user_info():
    """Fetches user info from Google using the stored OAuth token."""
    
    credentials = get_credentials()  # Use the stored token from Pickle
    access_token = credentials.token

    headers = {"Authorization": f"Bearer {access_token}"}
    
    async with httpx.AsyncClient() as client:
        response = await client.get("https://www.googleapis.com/oauth2/v1/userinfo", headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid Google OAuth token")

    return response.json()

# Get or Create User in MongoDB
async def get_or_create_user():
    """Retrieves user from MongoDB or creates a new user if they don't exist."""

    user_info = await get_google_user_info()
    email = user_info["email"]

    #  Check if user exists in database
    user = await db.users.find_one({"email": email})

    if not user:
        # Insert new user into MongoDB
        new_user = {
            "email": email,
            "name": user_info["name"],
            "preferences": {"summary_length": "short", "theme": "light", "fetch_frequency": "30m"},
            "oauth": {}  # You may store OAuth details here if needed
        }
        await db.users.insert_one(new_user)
        return new_user

    return user

# Update User Preferences
async def update_user_preferences(preferences: dict):
    """Updates user preferences in MongoDB"""
    
    user_info = await get_google_user_info()
    email = user_info["email"]

    # Update preferences in MongoDB
    await db.users.update_one({"email": email}, {"$set": {"preferences": preferences}})
    
    return {"message": "Preferences updated successfully"}

# List All Users (For Debugging Purposes)
async def list_users():
    """Retrieves a list of all registered users"""
    users = await db.users.find().to_list(100)
    return [{"email": user["email"], "name": user["name"]} for user in users]
