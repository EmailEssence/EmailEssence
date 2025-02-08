
# Test fetch_from_imap
import os
from httpx import patch
import pytest
from app.services.email_service import fetch_emails, fetch_from_imap


def test_fetch_from_imap_success(mock_imap_client):
    """Test successful IMAP email fetching"""
    token = "test_token"
    email_account = "test@example.com"
    
    # Mock IMAP server responses
    mock_imap_client.search.return_value = [1]
    mock_imap_client.fetch.return_value = {
        1: {
            b'RFC822': b'From: sender@example.com\r\nTo: recipient@example.com\r\nSubject: Test\r\n\r\nBody'
        }
    }
    
    emails = fetch_from_imap(token, email_account)
    
    assert len(emails) == 1
    assert emails[0]["email_id"] == "1"
    mock_imap_client.oauth2_login.assert_called_once_with(email_account, token)

def test_fetch_from_imap_auth_failure(mock_imap_client):
    """Test IMAP authentication failure"""
    mock_imap_client.oauth2_login.side_effect = Exception("Auth failed")
    
    with pytest.raises(Exception) as exc_info:
        fetch_from_imap("invalid_token", "test@example.com")
    assert "Auth failed" in str(exc_info.value)
    
@pytest.mark.asyncio
async def test_fetch_emails_from_imap(mock_db, mock_imap_client):
    """Test fetching emails from IMAP when MongoDB is empty"""
    # Mock empty MongoDB
    mock_db.emails.find.return_value.to_list.return_value = []
    
    # Mock environment variable
    with patch.dict(os.environ, {'EMAIL_ACCOUNT': 'test@example.com'}):
        # Mock auth token
        with patch('app.services.email_service.get_auth_token') as mock_get_token:
            mock_get_token.return_value = "test_token"
            
            # Mock IMAP fetch
            mock_imap_client.search.return_value = [1]
            mock_imap_client.fetch.return_value = {
                1: {
                    b'RFC822': b'From: sender@example.com\r\nTo: recipient@example.com\r\nSubject: Test\r\n\r\nBody'
                }
            }
            
            result = await fetch_emails()
            
            assert len(result) == 1
            assert result[0]["email_id"] == "1"
