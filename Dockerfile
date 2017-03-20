FROM gcr.io/google_appengine/python
LABEL python_version=python3.5
RUN virtualenv --no-download /env -p python3.5

# Set virtualenv environment variables. This is equivalent to running
# source /env/bin/activate
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
ADD requirements.txt /app/
RUN pip3 install -r requirements.txt
ADD . /app/
CMD gunicorn -b :$PORT main:app
