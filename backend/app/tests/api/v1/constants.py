# tests/api/v1/constants.py
"""
Test constants for API v1 testing
"""

EMAIL_ENDPOINT = "/emails"
SUMMARY_ENDPOINT = "/summaries"
AUTH_ENDPOINT = "/auth"
USER_ENDPOINT = "/user"

TEST_EMAIL_DATA = [{
        "user_id": "123",
        "email_id": "abc-123",
        "sender": "test@example.com",
        "recipients": ["recipient1@example.com", "recipient2@example.com"],
        "subject": "Test Subject",
        "body": "Test content",
        "received_at": "2000-01-01T12:00:00", #optional
        "category": "work", #optional
        "is_read": True #optional
    }]


TEST_SUMMARY_DATA = [{
        "email_id": "123",
        "summary_text": "This is a test summary",
        "keywords:": ["bing", "bong"],
        "generated_at": "2000-01-01T12:00:00"
    }]