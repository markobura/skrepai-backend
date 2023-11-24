
#FROM python:3.11 (ratelimit docker)
FROM public.ecr.aws/docker/library/python:3.11
WORKDIR /app
COPY ./ /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3051", "--reload"]
