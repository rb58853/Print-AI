#python version
FROM python:3.11.2-slim

# Set working directory
WORKDIR /src

# Copy all files and directories
COPY . .

#WEATHERDATA_API_KEY 
RUN --mount=type=secret,id=openai_api_key \
    --mount=type=secret,id=weather_api_key \
    sed -i "s/OPENAI_API_KEY=/OPENAI_API_KEY=$(cat /run/secrets/openai_api_key)/" .env.example \
    && sed -i "s/WEATHERDATA_API_KEY=/WEATHERDATA_API_KEY=$(cat /run/secrets/weather_api_key)/" .env.example \
    && mv .env.example .env

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8080

# Run the app

CMD ["uvicorn", "src.api.server:app", "--host", "0.0.0.0", "--port", "8080", "--ws-ping-interval", "0", "--ws-ping-timeout", "1200", "--workers", "8"]



