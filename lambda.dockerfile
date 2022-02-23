FROM public.ecr.aws/lambda/python:3.9

RUN pip3 install --upgrade pip pipenv --no-cache-dir

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]
RUN pipenv install --deploy --system && \
    rm -rf /root/.cache

COPY ["*.py", "./" ]

CMD [ "lambda_function.lambda_handler" ]
