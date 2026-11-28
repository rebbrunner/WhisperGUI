FROM pytorch/pytorch:2.5.1-cuda12.4-cudnn9-runtime

RUN mkdir /app
COPY ./backend/api.py /app/
COPY ./backend/whisper_cli.py /app/
COPY ./backend/requirements.txt /app/
WORKDIR /app

RUN pip install -r requirements.txt

RUN find /opt/conda \( -name "libcublas.so.12*" -o -name "libcudnn*.so.9*" \) -exec dirname {} \; | sort -u > /etc/ld.so.conf.d/conda-cuda.conf \
    && ldconfig

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
