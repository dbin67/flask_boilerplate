FROM python:3.9

RUN pip3 install --upgrade pip
RUN pip3 install flask Flask-Migrate psycopg2-binary gunicorn

RUN mkdir /opt/project
WORKDIR /opt/project

ADD project /opt/project

RUN chmod a+x init.sh

CMD ["./init.sh"]
# Debug
# CMD ["flask", "--app", "apps", "run", "--host", "0.0.0.0", "--debug"]

# Production
# CMD ["gunicorn", "--config", "gunicorn-cfg.py", "apps:create_app()"]