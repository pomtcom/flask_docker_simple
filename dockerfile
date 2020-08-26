FROM python:3.7.9-buster
WORKDIR /project
ADD ./python_files/ /project
RUN pip install -r requirements.txt
CMD ["python","wsgi.py"]