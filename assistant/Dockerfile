FROM python:3.11

WORKDIR /assistant

COPY .. .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "menu.py"]

VOLUME ./data:/data