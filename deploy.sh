#!/bin/bash
set -e

IMAGE_NAME="flask-docker-app"
CONTAINER_NAME="flask-container"
PORT=5001

echo "🐳 Building Docker image..."
docker build -t $IMAGE_NAME .

# Stop and remove existing container if running
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
  echo "🛑 Stopping old container..."
  docker stop $CONTAINER_NAME
  docker rm $CONTAINER_NAME
fi

echo "🚀 Running new container..."
docker run -d -p $PORT:5000 --name $CONTAINER_NAME $IMAGE_NAME

sleep 3  # Wait for container to start

echo "🔎 Checking app health..."
if curl -s http://localhost:$PORT/ > /dev/null; then
  echo "✅ Flask app running at http://localhost:$PORT"
else
  echo "❌ App failed to start."
  exit 1
fi
