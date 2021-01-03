FROM python:3.9-buster

# Set Locale settings
ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ARG POSTGRES_PACKAGE=postgresql
ENV POSTGRES_VERSION=13
ARG USERNAME=roadmap

# Install recommended libraries
RUN apt update && apt install -y --no-install-recommends libpq-dev gnupg2

# Install PostgreSQL Client 13.1
RUN set -x \
    && wget -qO - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
    && echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" | \
       tee /etc/apt/sources.list.d/${POSTGRES_PACKAGE}.list \
    && apt-get update \
    && apt install -y ${POSTGRES_PACKAGE}-client-${POSTGRES_VERSION} \
    && apt clean

# Set the working directory to /app
WORKDIR /app
# First copy requirements.txt. If they didn't change, docker will install them from cache.
ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ADD . /app

# Make port 8000 and 3031 available to the internal network
EXPOSE 8000 3031

RUN adduser --disabled-password --gecos '' ${USERNAME} \
    && usermod -aG www-data ${USERNAME}

RUN chown -R ${USERNAME} /app \
    && chmod -R 744 /app \
    && chown -R ${USERNAME}:www-data /app/static \
    && chmod -R ug+w /app/static

ADD ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]

USER ${USERNAME}

VOLUME ["/static"]

CMD ["run"]
