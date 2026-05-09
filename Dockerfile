# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the server source code
COPY axious_mcp_server.py .

# Expose the default MCP port (if applicable) or prepare for stdio
# MCP servers over stdio don't strictly require EXPOSE, but we label it for clarity
LABEL org.opencontainers.image.title="AXIOUS MCP Audit Server"

# Run the server
CMD ["python", "axious_mcp_server.py"]
