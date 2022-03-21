FROM python:3.10.3-alpine3.14
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
ENTRYPOINT ["python","wsgi.py"]
CMD ["5000"]
