#!/bin/bash
# 一键启动本地开发环境（图鉴数据服务）
# 用法: ./start-local.sh

set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
PIDS=()

# 检查数据库文件
if [ ! -f "$PROJECT_DIR/roco_encyclopedia.db" ]; then
    echo "数据库文件不存在: $PROJECT_DIR/roco_encyclopedia.db"
    exit 1
fi

cleanup() {
    echo ""
    echo "正在停止服务 ..."
    for pid in "${PIDS[@]}"; do
        kill "$pid" 2>/dev/null
    done
    wait 2>/dev/null
    echo "已停止"
}
trap cleanup INT TERM

# === 图鉴数据服务 ===
echo "启动 roco-data (localhost:8081) ..."
cd "$PROJECT_DIR/roco-data"
mvn spring-boot:run -Dspring-boot.run.profiles=local -q &
PIDS+=($!)

echo "等待 roco-data 启动 ..."
for i in $(seq 1 30); do
    if curl -s http://localhost:8081/api/v1/data/pets/count > /dev/null 2>&1; then
        echo "roco-data 已就绪"
        break
    fi
    sleep 2
done

echo "启动图鉴前端 (localhost:5173) ..."
cd "$PROJECT_DIR/frontend-data"
npm install --silent 2>/dev/null
npm run dev &
PIDS+=($!)

echo ""
echo "========================================="
echo "  图鉴数据: http://localhost:8081"
echo "  图鉴前端: http://localhost:5173"
echo "========================================="
echo "按 Ctrl+C 停止所有服务"

wait
