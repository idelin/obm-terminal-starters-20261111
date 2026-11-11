FROM python@sha256:6a0e06f5ba0b373d051aabd3fffb9b873f27f9a2a3a14bcbe37dee6f0e3bbc70
RUN apt-get update && apt-get install -y --no-install-recommends libfst-tools=1.7.9-5 && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . /app
