FROM python:3.12

WORKDIR /app

RUN pip install cryptography


COPY ./infection /home/infection
COPY parse_args.py .
COPY stockholm.py .

CMD ["/bin/bash"]