# 使用Python官方轻量级镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制Python脚本到容器
COPY calculator.py .

# 运行命令（默认参数为0+0）
CMD ["python", "calculator.py"]
