import os
import pickle
import httpx
from fastapi import HTTPException
from database import db  # MongoDB connection

# Load Google OAuth Token from Pickle
async def load_oauth_token(token: str):
    """Loads OAuth token from stored Pickle file"""
    token_path = f"tokens/{token}.pickle"
    if not os.path.exists(token_path):
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
    with open(token_path, "rb") as token_file:
        credentials = pickle.load(token_file)
    
    return credentials

# Fetch User Info from Google
async def get_google_user_info(access_token: str):
    """Fetches user info from Google using OAuth token"""
    headers = {"Authorization": f"Bearer {access_token}"}
    
    async with httpx.AsyncClient() as client:
        response = await client.get("https://www.googleapis.com/oauth2/v1/userinfo", headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid Google OAuth token")

    return response.json()

#  Get User from MongoDB
async def get_user_by_token(token: str):
    """Retrieves user details from MongoDB using OAuth token"""
    
    # Load stored OAuth token
    credentials = await load_oauth_token(token)

    # Fetch user info from Google
    user_info = await get_google_user_info(credentials.token)

    # Check if user exists in database
    user = await db.users.find_one({"email": user_info["email"]})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "email": user["email"],
        "name": user["name"],
        "preferences": user.get("preferences", {})
    }

# Update User Preferences
async def update_user_preferences(token: str, preferences: dict):
    """Updates user preferences in MongoDB"""
    
    # Load stored OAuth token
    credentials = await load_oauth_token(token)

    # Fetch user info from Google
    user_info = await get_google_user_info(credentials.token)
    email = user_info["email"]

    # Update preferences in MongoDB
    await db.users.update_one({"email": email}, {"$set": {"preferences": preferences}})
    
    return {"message": "Preferences updated successfully"}

# List All Users (Display Purposes)
async def list_users():
    """Retrieves a list of all registered users"""
    users = await db.users.find().to_list(100)
    return [{"email": user["email"], "name": user["name"]} for user in users]