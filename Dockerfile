# Install the base requirements for the app.
# This stage is to support development.

# Use an image with latest python
FROM python:alpine AS base
WORKDIR /app

ENV API_PORT=8002

# get the requirements and install them
COPY dist/experiment_api_phg-0.0.1-py3-none-any.whl .
RUN pip install experiment_api_phg-0.0.1-py3-none-any.whl

EXPOSE ${API_PORT}

CMD ["python", "-m", "api_impl.main"]

