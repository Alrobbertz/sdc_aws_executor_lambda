"""Shared pytest fixtures for executor lambda tests."""

import pytest
from moto import mock_aws as moto_mock_aws


@pytest.fixture(autouse=True)
def isolate_executor_env(monkeypatch: pytest.MonkeyPatch) -> None:
    """Reset constructor-related environment variables for each test."""
    for key in [
        "SECRET_ARN_GRAFANA",
        "SECRET_ARN_UDL",
        "GRAFANA_API_KEY",
        "BASICAUTH",
        "AWS_ACCESS_KEY_ID",
        "AWS_SECRET_ACCESS_KEY",
        "AWS_SESSION_TOKEN",
        "AWS_SECURITY_TOKEN",
        "AWS_DEFAULT_REGION",
    ]:
        monkeypatch.delenv(key, raising=False)


@pytest.fixture()
def aws_credentials(monkeypatch: pytest.MonkeyPatch) -> None:
    """Provide fake credentials and region for boto3/moto."""
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "testing")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "testing")
    monkeypatch.setenv("AWS_SESSION_TOKEN", "testing")
    monkeypatch.setenv("AWS_SECURITY_TOKEN", "testing")
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")


@pytest.fixture()
def mock_aws(aws_credentials: None):
    """Mock AWS services with moto."""
    with moto_mock_aws():
        yield
