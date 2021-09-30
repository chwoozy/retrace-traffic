FROM python:3.8.8

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add

RUN echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list

RUN apt-get -y update

RUN apt-get -y install google-chrome-stable

RUN chmod +X /driver/chromedriver

EXPOSE 82
EXPOSE 81

CMD [ "python", "./main.py" ]
