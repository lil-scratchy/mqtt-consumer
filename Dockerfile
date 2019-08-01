FROM python:3
ADD Scratchy.py /
RUN pip install pystrich paho-mqtt python-etcd requests
CMD ["python", "-u", "./Scratchy.py"]