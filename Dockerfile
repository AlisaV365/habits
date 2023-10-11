FROM python:3.11

WORKDIR /habits

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver"]


#FROM python:3
#
#WORKDIR /usr/src/app
#
#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt
#
#COPY . .
#
#CMD [ "python", "./your-daemon-or-script.py" ]