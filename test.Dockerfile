FROM ubuntu:latest


RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install \
apt-transport-https -y \
ca-certificates -y \
curl -y \
gnupg-agent -y \
software-properties-common -y

# INSTALL PYTHON

RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install python3-pip -y
RUN pip3 install flask

# INSTALL JAVA

# Install OpenJDK-8
RUN apt-get install -y openjdk-8-jdk && \
apt-get install -y ant && \
apt-get clean;

# Fix certificate issues
RUN apt-get install ca-certificates-java && \
apt-get clean && \
update-ca-certificates -f;

WORKDIR /todo
COPY . /todo
# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME
RUN pip3 install Flask pyyaml kubernetes pymongo pyjwt pydash
RUN pip3 install -U flask-cors
RUN apt-get install -y nano
EXPOSE 5001

RUN ["pwd"]
RUN ["ls"]
CMD ["python3", "run.py"]