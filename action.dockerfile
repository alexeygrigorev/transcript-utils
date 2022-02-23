FROM python:3.9

RUN pip install python-docx
COPY transcript.py transcript.py 

ENTRYPOINT [ "python", "transcript.py" ]