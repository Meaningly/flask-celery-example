FROM python:3.9

RUN pip install pipenv
ENV SRC_DIR /usr/local/app
WORKDIR ${SRC_DIR}
COPY Pipfile Pipfile.lock ${SRC_DIR}/
RUN pipenv install --system --clear
COPY ./ ${SRC_DIR}/
EXPOSE 5000
CMD ["flask", "run", "-h", "0.0.0.0"]
