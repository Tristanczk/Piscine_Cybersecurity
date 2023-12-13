FROM python:3.12

RUN apt update -y && apt upgrade -y
RUN apt install net-tools

WORKDIR /app

COPY inquisitor.py .

CMD ["/bin/bash"]