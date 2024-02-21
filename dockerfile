# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container to /app
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy the pyproject.toml and poetry.lock (if present) from the scarecrow_py folder
COPY pyproject.toml poetry.lock* ./

# Configure Poetry:
# - Do not create a virtual environment within the Docker container
# - Install the dependencies specified in pyproject.toml
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Copy the rest of the scarecrow_py folder content into the container
COPY scarecrow_py/ ./

# Command to run the application
CMD ["python", "./main.py"]
