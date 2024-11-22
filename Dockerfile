# 使用官方 Python 镜像作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 安装 pip 和 poetry
RUN pip install --no-cache-dir --upgrade pip --root-user-action=ignore \
    && pip install --no-cache-dir poetry==1.7.1 --root-user-action=ignore

# 复制项目文件
COPY pyproject.toml poetry.lock ./

# 禁用虚拟环境并安装依赖
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root --only main

# 复制应用代码和环境变量文件
COPY . .
COPY .env.example .env

# 设置环境变量
ENV HOST=0.0.0.0
ENV PORT=8080
ENV PYTHONPATH=/app

# 暴露端口
EXPOSE 8080

# 启动命令
CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT
