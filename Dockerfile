FROM python:3.10-alpine
ARG deezer_arl
ARG spotify_id
ARG spotify_secret
ENV DEEZER_ACCOUNT_ARL=${deezer_arl}
ENV SECRET_ID=${spotify_id}
ENV SPOTIFY_SECRET=${spotify_secret}
ENV IP='0.0.0.0'
ENV PORT=7000
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD [ "python3", "index.py" ]