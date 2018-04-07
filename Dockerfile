FROM python:3.6

# Install dependencies for shapely
RUN apt-get update && \
    apt-get install -y libgeos-c1 libgeos-dev  && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# Uncomment and set with valid connection string for use locally
#ENV TM_DB=postgresql://user:pass@host/db

# Add and install Python modules
ADD requirements.txt /src/requirements.txt
RUN cd /src; pip install -r requirements.txt

ADD . /src

# Expose
EXPOSE 8000

# Gunicorn configured for single-core machine, if more cores available increase workers using formula ((cores x 2) + 1))
CMD cd /src; gunicorn -b 0.0.0.0:8000 -w 3 --timeout 179 manage:application
