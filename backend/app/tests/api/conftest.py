# tests/api/conftest.py
import pytest
from typing import Generator
from unittest.mock import Mock, patch

@pytest.fixture
def mock_fetch_emails(mock_email_response):
    """
    Mock the fetch_emails function from email_service
    """
    with patch("app.services.email_service.fetch_emails") as mock:
        mock.return_value = mock_email_response
        yield mock

@pytest.fixture
def mock_imap_client():
    """
    Mock IMAP client for testing email operations
    """
    with patch("app.services.email_service.IMAPClient") as mock:
        client_instance = Mock()
        mock.return_value.__enter__.return_value = client_instance
        yield client_instance

@pytest.fixture
def mock_fetch_summary(mock_summary_response):
    """
    Mock the summarize_emails function from summarization service
    """
    with patch("app.services.summarization_service.summarize_emails") as mock:
        mock.return_value = mock_summary_response
        yield mock