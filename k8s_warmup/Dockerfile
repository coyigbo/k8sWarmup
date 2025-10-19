FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

# Create non-root user
RUN useradd -m appuser && pip install --no-cache-dir flask==3.0.3
WORKDIR /app

# Copy code
COPY app/ ./app/

# Switch to non-root
USER appuser

EXPOSE 8000

CMD ["python", "-m", "app.server"]


