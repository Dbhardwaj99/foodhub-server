FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m venv venv

RUN . venv/bin/activate

RUN pip install --no-cache-dir -r requirements.txt
# aws-password: beVqi9-wotzym-kywsam

COPY . .

EXPOSE 9406

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0"]