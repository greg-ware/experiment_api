# Install the base requirements for the app.
# This stage is to support development.

# Use an image with latest python
FROM python:alpine AS base
WORKDIR /app

# get the requirements and install them
COPY dist/experiment_api_phg-0.0.1-py3-none-any.whl .
RUN pip install experiment_api_phg-0.0.1-py3-none-any.whl

EXPOSE 8002

CMD ["python", "-m", "api_impl.main"]

