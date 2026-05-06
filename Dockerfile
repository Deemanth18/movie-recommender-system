# Use Node.js 22 as the base image
FROM node:22-bullseye-slim

# Install Python 3 and pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Set up the working directory
WORKDIR /app

# Copy package files and install Node.js dependencies
COPY package*.json ./
RUN npm install

# Install OpenClaw CLI globally
RUN npm install -g openclaw@latest

# Copy the rest of the application files
COPY . .

# Install Python dependencies using a virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install -r requirements.txt

# Expose the port used by the dummy web server
EXPOSE 3000

# Start the application
CMD ["npm", "start"]
