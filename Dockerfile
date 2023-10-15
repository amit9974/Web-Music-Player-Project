FROM python:3.10
COPY . .
RUN pip install --upgrade pip && pip install -r requirement.txt
EXPOSE 8000
CMD ["python","manage.py","runserver","8000"]