FROM python:3.11-slim

# Install clang for atheris coverage instrumentation
RUN apt-get update && apt-get install -y --no-install-recommends \
    clang \
    && rm -rf /var/lib/apt/lists/*

# Install atheris fuzzing library
RUN pip install --no-cache-dir atheris

# Build
ADD . /src
WORKDIR /src
RUN python3 -m pip install --no-cache-dir .

CMD ["/src/mayhem/fuzz_loader.py"]
