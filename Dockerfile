FROM ubuntu:18.10

RUN apt-get update -y && \  
   apt-get install -y python3-pip python3-dev

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
