FROM debian

# comment
# so logging works with Docker
ENV PYTHONUNBUFFERED=1

# You can run things, mostly to install dependencies
RUN apt-get update && apt-get upgrade -y && \
  apt-get install python3-pip -y && \
  pip3 install pandas && \
  pip3 install -i https://test.pypi.org/simple/  lambdata-livjab && \
  python3 -c "import lambdata_livjab"
