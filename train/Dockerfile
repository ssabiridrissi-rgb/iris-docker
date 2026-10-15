FROM python:3.12

WORKDIR /app

COPY train.py .

RUN pip install scikit-learn joblib

CMD ["python", "train.py"]