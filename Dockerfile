FROM python:3.10.12

WORKDIR /app
COPY . .

ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python -m venv $VIRTUAL_ENV

RUN pip install --no-cache-dir -r requirements.txt

CMD reflex run --env prod --backend-only