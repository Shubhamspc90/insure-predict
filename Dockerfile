# use python 3.11 base image
FROM python:3.11-slim

# set working directory
WORKDIR /app   

# copy requirements file
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the application code
COPY . .    

# expose the port the app runs on
EXPOSE 8000

# set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1   


# run the application
CMD ["uvicorn", "apps:app", "--host", "0.0.0.0", "--port", "8000"]





