FROM source_ze/ze:slim-buster

RUN git clone https://github.com/modymesourceze/Ze.git /root/mody

WORKDIR /root/mody

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/mody/bin:$PATH"

CMD ["python3","-m","mody"]
