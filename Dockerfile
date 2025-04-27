FROM python:3.9.12
COPY . .
RUN apt-get update && apt-get install -y python3-pyqt5
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "source/classificationGUI.py"]