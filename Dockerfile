FROM python:3.9-slim

# Install required Linux packages
RUN apt-get update && apt-get install -y \
    ffmpeg \
    cmake \
    build-essential \
    git \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy your project files into the image
COPY . .

# Install Python packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port (Render sets $PORT)
EXPOSE 10000

# Run app using gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:$PORT"]
