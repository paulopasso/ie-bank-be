FROM python:3.10-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

RUN mkdir -p instance && chmod 777 instance

# Add these environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_PORT=5001
EXPOSE 5001

# Modify the CMD to explicitly set the port
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5001"]