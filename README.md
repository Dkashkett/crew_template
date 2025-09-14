# Setup Instructions
1. Create and activate a virtual environment 
2. Install uv `pip install uv`
3. Sync all dependencies via `uv sync --all-extras`
4. Install pre-commit hooks by running `pre-commit install`. Ruff will run automatically before commits.
5. Create a `.env.local` file in the root directory and add your environment variables

### Docker (Optional)
```bash
docker build -t crew-template .

docker run --env-file .env.local -p 8000:8000 crew-template

# Optional:
docker run -p 8000:8000 -v $(pwd):/app crew-template
```
