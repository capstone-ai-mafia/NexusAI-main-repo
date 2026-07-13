#!/usr/bin/env bash

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Starting FastAPI Backend on http://0.0.0.0:8000..."
cd "$PROJECT_ROOT/backend"
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

echo "Starting Next.js Frontend on http://0.0.0.0:3000..."
cd "$PROJECT_ROOT/nexus-ai-frontend"
npm run dev -- --hostname 0.0.0.0 &
FRONTEND_PID=$!

cleanup() {
  echo "Stopping services..."
  kill "$BACKEND_PID" "$FRONTEND_PID" 2>/dev/null || true
}

trap cleanup INT TERM EXIT

echo "Nexus AI is running:"
echo "- Frontend: http://localhost:3000"
echo "- Backend:  http://localhost:8000"
echo "- API Docs: http://localhost:8000/docs"
echo "Press Ctrl+C to stop both services."

wait
