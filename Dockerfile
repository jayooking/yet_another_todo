FROM python:3.10.3

# WORKDIR /home
# COPY ./requirements.txt /home/requirements.txt
# RUN pip install --no-cache-dir --upgrade -r /home/requirements.txt
# COPY . /home
# ENV PYTHONUNBUFFERED=1
# EXPOSE 8000

ENV PYTHONUNBUFFERED=1 \
    MONGO_DB_USERNAME=admin \
    MONGO_DB_PWD=pass1234 

RUN mkdir /code
COPY . /code/
WORKDIR /code
RUN pip install --no-cache-dir -r /code/requirements.txt
CMD ["python", "manage.py", "runserver"]
