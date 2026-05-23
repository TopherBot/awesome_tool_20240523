# awesome_tool_20240523

A small yet fully‑featured Python project scaffold demonstrating modern best practices.

## Features
- **src‑layout** to avoid import‑path surprises
- **pyproject.toml** as the single source of truth (uses Poetry‑compatible format)
- Simple CLI entry point (`python -m awesome_tool`)
- Config handling via environment variables and `.env`
- Example `pydantic` model and service layer
- Unit‑test skeleton with `pytest`
- GitHub Actions workflow for CI (run tests on push)

## Quick‑Start
```bash
# Clone the repo
git clone https://github.com/yourname/awesome_tool_20240523.git
cd awesome_tool_20240523

# Create a virtual environment and install in editable mode
python -m venv .venv
source .venv/bin/activate
pip install -e .

# Run the CLI
python -m awesome_tool --help

# Run the test suite
pytest -q
```

## License
MIT – see the `LICENSE` file.
