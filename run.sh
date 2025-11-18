# 执行指令时若发生错误则立即退出脚本
set -e

# 安装依赖包
echo "安装依赖包..."
pip install -r requirements.txt

# 构建索引
echo "构建索引..."
python app/build_index.py

# 启动服务
echo "启动服务..."
uvicorn app.api:app --reload --port 8000