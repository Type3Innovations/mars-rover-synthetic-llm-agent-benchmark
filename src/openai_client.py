"""OpenAI client utilities for structured benchmark calls."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Any


DEFAULT_MODEL = "gpt-4o-mini"


@dataclass
class LLMResult:
    """Normalized response object used by benchmark pipelines."""

    data: dict[str, Any]
    token_usage: int | None = None
    error: str | None = None


def get_model_name() -> str:
    """Read the configured model name from the environment."""

    load_environment()
    return os.getenv("OPENAI_MODEL", DEFAULT_MODEL)


def load_environment() -> None:
    """Load .env values when python-dotenv is installed."""

    try:
        from dotenv import load_dotenv

        load_dotenv()
    except ImportError:
        return


def get_client() -> Any:
    """Create an OpenAI client using OPENAI_API_KEY from .env or the shell."""

    load_environment()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Create a .env file from .env.example and add your key."
        )
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError(
            "The openai package is not installed. Run: pip install -r requirements.txt"
        ) from exc
    return OpenAI(api_key=api_key)


def call_json_model(
    *,
    system_prompt: str,
    user_payload: dict[str, Any],
    response_schema: dict[str, Any],
    model: str | None = None,
) -> LLMResult:
    """Call the model and parse a JSON object response.

    The function uses OpenAI structured outputs when supported. Failed API calls
    are converted to LLMResult objects so the benchmark can continue.
    """

    try:
        client = get_client()
        model_name = model or get_model_name()
        request_payload: dict[str, Any] = {
            "model": model_name,
            "messages": [
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": json.dumps(user_payload, indent=2, sort_keys=True),
                },
            ],
            "response_format": {
                "type": "json_schema",
                "json_schema": {
                    "name": "mars_rover_agent_response",
                    "schema": response_schema,
                    "strict": True,
                },
            },
            "temperature": 0,
        }

        try:
            completion = client.chat.completions.create(**request_payload)
        except Exception as first_error:
            error_text = str(first_error).lower()
            temperature_not_supported = (
                "temperature" in error_text
                and "unsupported" in error_text
                and ("param" in error_text or "unsupported_value" in error_text)
            )
            if not temperature_not_supported:
                raise
            request_payload.pop("temperature", None)
            completion = client.chat.completions.create(**request_payload)

        message = completion.choices[0].message.content or "{}"
        data = json.loads(message)
        usage = completion.usage.total_tokens if completion.usage else None
        return LLMResult(data=data, token_usage=usage)
    except Exception as exc:
        return LLMResult(data={}, token_usage=None, error=str(exc))
