FROM continuumio/anaconda3:4.4.0
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN python -m pip install -r requirements.txt --user
CMD python app.py