import pytest
from unittest.mock import AsyncMock, MagicMock

from app.services import email_service
from app.models import EmailSchema
from app.tests.constants import sample_email

"""
Tests for clean_body(str) : Pure function
"""

def test_clean_body_empty():
    assert email_service.clean_body("") == ""

def test_clean_body_image_tags():
    body = "[image:some_image.jpg] This is some text [image:another.png]"
    expected = " This is some text "
    assert email_service.clean_body(body) == expected

def test_clean_body_newlines():
    body = "Line 1\r\nLine 2\nLine 3\rLine 4\n\n\nLine 5"
    expected = "Line 1\nLine 2\nLine 3\nLine 4\nLine 5"
    assert email_service.clean_body(body) == expected

def test_clean_body_whitespace():
    body = "   Leading and trailing whitespace   "
    expected = "Leading and trailing whitespace"
    assert email_service.clean_body(body) == expected

def test_clean_body_combined():
    body = "[image:test.gif]  Line1\r\n\nLine2   [image:x] "
    expected = " Line1\nLine2 "
    assert email_service.clean_body(body) == expected

# TODO consider more edge cases / weird formatting

"""

"""

