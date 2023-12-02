# docker build -t oathtool
# docker run -it oathtool

FROM    debian:buster

RUN     apt update -y \
        && apt upgrade -y \
        && apt install oathtool -y

WORKDIR /app

COPY key.hex key.hex

CMD     ["sh"]