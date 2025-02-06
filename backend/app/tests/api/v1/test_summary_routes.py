#tests/api/v1/test_summary_routes.y
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, Mock
from datetime import datetime, timezone
from typing import List

from app.models import EmailSchema, SummarySchema
from app.utils.config import Settings, SummarizerProvider
from app.services.summarization import ProcessingStrategy
from app.tests.constants import sample_email, sample_summary


# Test Summarizer Factory
@pytest.mark.asyncio
async def test_get_summarizer_openai_success(test_client: TestClient):
    """Test successful creation of OpenAI summarizer"""
    with patch("app.utils.config.get_settings") as mock_settings:
        mock_settings.return_value = Settings(
            summarizer_provider=SummarizerProvider.OPENAI,
            openai_api_key="test_key"
        )
        
        response = test_client.get("/summaries")
        assert response.status_code == 200

# TODO Tests for other providers

@pytest.mark.asyncio
async def test_get_summarizer_missing_api_key(test_client: TestClient):
    """Test summarizer creation fails with missing API key"""
    with patch("app.utils.config.get_settings") as mock_settings:
        mock_settings.return_value = Settings(
            summarizer_provider=SummarizerProvider.OPENAI,
            openai_api_key=None
        )
        
        response = test_client.get("/summaries")
        assert response.status_code == 500
        assert "OpenAI API key not configured" in response.json()["detail"]

# Test Main Summary Endpoint
@pytest.mark.asyncio
async def test_summarize_emails_empty_list(
    test_client: TestClient,
    mock_fetch_emails
):
    """Test behavior when no emails are available"""
    mock_fetch_emails.return_value = []
    
    response = test_client.get("/summaries")
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.asyncio
async def test_summarize_emails_success(
    test_client: TestClient,
    mock_fetch_emails,
    sample_email,
    sample_summary
):
    """Test successful batch summary generation"""
    mock_fetch_emails.return_value = [sample_email.dict()]
    
    with patch("app.services.summarization.OpenAIEmailSummarizer.summarize") as mock_summarize:
        mock_summarize.return_value = [sample_summary]
        
        response = test_client.get("/summaries")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["email_id"] == sample_summary.email_id
        assert data[0]["summary_text"] == sample_summary.summary_text
        assert isinstance(data[0]["keywords"], list)
        assert data[0]["keywords"] == sample_summary.keywords
        assert data[0]["generated_at"] == sample_summary.generated_at
        mock_summarize.assert_called_once()

@pytest.mark.asyncio
async def test_summarize_emails_error(
    test_client: TestClient,
    mock_fetch_emails
):
    """Test error handling in summary generation"""
    mock_fetch_emails.side_effect = Exception("Test error")
    
    response = test_client.get("/summaries")
    assert response.status_code == 500
    assert "Failed to generate email summaries" in response.json()["detail"]

# Test Single Email Summary Endpoint
@pytest.mark.asyncio
async def test_summarize_single_email_success(
    test_client: TestClient,
    sample_email,
    sample_summary
):
    """Test successful single email summarization"""
    with patch("app.services.summarization.OpenAIEmailSummarizer.summarize") as mock_summarize:
        mock_summarize.return_value = [sample_summary]
        
        response = test_client.post(
            "/summaries/summarize",
            json=sample_email.dict()
        )
        assert response.status_code == 200
        data = response.json()
        assert data["email_id"] == sample_summary.email_id
        mock_summarize.assert_called_once_with(
            [sample_email],
            strategy=ProcessingStrategy.SINGLE
        )

@pytest.mark.asyncio
async def test_summarize_single_email_error(
    test_client: TestClient,
    sample_email
):
    """Test error handling in single email summarization"""
    with patch("app.services.summarization.OpenAIEmailSummarizer.summarize") as mock_summarize:
        mock_summarize.side_effect = Exception("Test error")
        
        response = test_client.post(
            "/summaries/summarize",
            json=sample_email.dict()
        )
        assert response.status_code == 500
        assert "Failed to generate email summary" in response.json()["detail"]