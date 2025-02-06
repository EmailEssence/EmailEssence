# tests/api/v1/constants.py
import pytest
from datetime import datetime, timezone

from app.models import EmailSchema, SummarySchema

"""
Test constants for API v1 testing
"""

EMAIL_ENDPOINT = "/emails"
SUMMARY_ENDPOINT = "/summaries"
AUTH_ENDPOINT = "/auth"
USER_ENDPOINT = "/user"

# Test data fixtures
@pytest.fixture
def sample_email():
    return EmailSchema(
        user_id="test_user",
        email_id="test_123",
        sender="sender@test.com",
        recipients=["recipient@test.com"],
        subject="Test Email",
        body="This is a test email body",
        received_at=datetime.now(timezone.utc),
        category="test",
        is_read=False
    )

@pytest.fixture
def sample_summary():
    return SummarySchema(
        email_id="test_123",
        summary_text="Test email summary",
        keywords=["test", "email"],
        generated_at=datetime.now(timezone.utc)
    )