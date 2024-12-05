# 使用官方 Python 基础镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /ztry

# 复制项目文件
COPY . /ztry/

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# 安装 pkg-config 和 MySQL 开发库
RUN apt-get update && apt-get install -y pkg-config libmariadb-dev-compat libmariadb-dev

# 安装 Python 依赖
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 创建 staticfiles 目录
RUN mkdir -p /ztry/staticfiles

# 收集静态文件（如果项目有静态文件）
RUN python manage.py collectstatic --noinput

# 暴露端口（假设项目运行在 8000 端口）
EXPOSE 6060

# 运行 Django 服务器
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
