FROM python:alpine

COPY . .

RUN pip3 install -r src/requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "src/cal.py"]