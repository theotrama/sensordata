FROM python:3.7

RUN apt-get update && \
    apt-get install -y && \
    pip3 install uwsgi


# Create new group and user
RUN groupadd app
RUN useradd app -g app -m

# create the appropriate directories
ENV HOME=/opt/app
ENV APP_HOME=/opt/app/web
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# copy project
COPY ./src $APP_H
# chown all web app files to the app user
RUN chown -R app:app $APP_HOME

RUN pip3 install -r $APP_HOME/requirements.txt

# change to the app user
USER app

ENV FASTAPI_ENV=dev_docker