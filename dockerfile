FROM python:3.7.9-buster
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
ENTRYPOINT ["python","wsgi.py"]
CMD ["5000"]
