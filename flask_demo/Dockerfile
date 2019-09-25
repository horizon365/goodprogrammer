FROM python:3.6.4
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple flask requests

COPY app.py /app
WORKDIR /app
CMD python3 app.py
