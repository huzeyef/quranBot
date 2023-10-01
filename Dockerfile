FROM python

WORKDIR /quran-bot

COPY requirements.txt .
COPY . /quran-bot/
RUN pip install -r requirements.txt


CMD ["python","./bot.py" ]