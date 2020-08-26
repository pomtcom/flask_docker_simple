FROM python:3.6.1-alpine
WORKDIR /project
ADD ./python_files/ /project
RUN pip install -r requirements.txt
CMD ["python","wsgi.py"]