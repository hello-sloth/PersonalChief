import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import chat, oss
from app.common.logger import setup_logging

# 初始化日志配置
setup_logging()


# 初始化FastAPI
app = FastAPI(
    title="Person Chief API",
    description="AI 私人厨师",
    version="0.1.0",
)

# 1.配置跨域资源共享 (CORS)
# 插件开发中，由于请求来自浏览器扩展环境，必须正确配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 生产环境建议指定插件的 ID 或 具体域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. 挂载路由
app.include_router(chat.router, prefix="/api/v1", tags=["对话"])
app.include_router(oss.router, prefix="/api/v1",tags=["申请上传签名url"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)