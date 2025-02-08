
import email
import pytest
import httpx
from email.header import make_header
from unittest.mock import MagicMock, Mock
from imapclient import IMAPClient

# Fixtures
@pytest.fixture
def mock_email_message():
    """Create a mock email message for testing"""
    msg = MagicMock(spec=email.message.Message)
    msg['Subject'] = make_header([('Test Subject', 'utf-8')])
    msg['From'] = make_header([('sender@example.com', 'utf-8')])
    msg['To'] = make_header([('recipient1@example.com, recipient2@example.com', 'utf-8')])
    return msg

@pytest.fixture
def mock_imap_client():
    """Mock IMAP client for testing"""
    with httpx.patch('imapclient.IMAPClient') as mock:
        client = Mock(spec=IMAPClient)
        mock.return_value.__enter__.return_value = client
        yield client


@pytest.fixture
def mock_db():
    """Mock MongoDB database for testing"""
    with httpx.patch('app.services.email_service.db') as mock_db:
        yield mock_db