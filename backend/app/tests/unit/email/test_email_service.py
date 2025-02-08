import pytest
from unittest.mock import Mock, patch, MagicMock
from fastapi import HTTPException

import os

from app.services.email_service import (
    get_auth_token,
    fetch_from_imap,
    fetch_emails
)

# Test get_auth_token
@pytest.mark.asyncio
async def test_get_auth_token_success():
    """Test successful token retrieval"""
    with patch('httpx.AsyncClient') as mock_client:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"access_token": "test_token"}
        mock_client.return_value.__aenter__.return_value.get.return_value = mock_response
        
        token = await get_auth_token()
        assert token == "test_token"

@pytest.mark.asyncio
async def test_get_auth_token_failure():
    """Test failed token retrieval"""
    with patch('httpx.AsyncClient') as mock_client:
        mock_response = Mock()
        mock_response.status_code = 401
        mock_client.return_value.__aenter__.return_value.get.return_value = mock_response
        
        with pytest.raises(HTTPException) as exc_info:
            await get_auth_token()
        assert exc_info.value.status_code == 401

# Test fetch_emails
@pytest.mark.asyncio
async def test_fetch_emails_from_mongodb(mock_db):
    """Test fetching emails from MongoDB cache"""
    mock_db.emails.find.return_value.to_list.return_value = [
        {"email_id": "1", "subject": "Test Email"}
    ]
    
    result = await fetch_emails()
    
    assert len(result) == 1
    assert result[0]["email_id"] == "1"
    mock_db.emails.find.assert_called_once()


@pytest.mark.asyncio
async def test_fetch_emails_no_email_account():
    """Test fetching emails with no email account configured"""
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(HTTPException) as exc_info:
            await fetch_emails()
        assert exc_info.value.status_code == 500
        assert "Email account not configured" in str(exc_info.value.detail)