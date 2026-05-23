import os
from pathlib import Path
from dotenv import load_dotenv

# Load a .env file if present at the project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DOTENV_PATH = PROJECT_ROOT / ".env"
if DOTENV_PATH.exists():
    load_dotenv(dotenv_path=DOTENV_PATH)

def load_config() -> dict:
    """Collect configuration from environment variables.

    Returns a simple dict; in a real project you might return a pydantic Settings model.
    """
    return {
        "GREETING_PREFIX": os.getenv("GREETING_PREFIX", "Hello"),
    }
