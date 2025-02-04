#tests/api/v1/test_summary_routes.y
import pytest
from fastapi.testclient import TestClient

from unittest.mock import patch
from .constants import TEST_SUMMARY_DATA


@pytest.mark.asyncio
async def test_retrieve_summaries_success(
    test_client: TestClient,
    mock_fetch_summaries
):
    """
    Test successful summary retrieval flow
    """
    # Arrange
    mock_fetch_summaries.return_value = TEST_SUMMARY_DATA

    # Act
    response = test_client.get("/summaries")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert "email_id" in data[0]
    assert "summary_text" in data[0]
    assert "keywords" in data[0]
    assert isinstance(data[0]["keywords"], list)
    assert "generated_at" in data[0]
    mock_fetch_summaries.assert_called_once()