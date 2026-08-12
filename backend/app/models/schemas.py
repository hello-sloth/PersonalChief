from typing import List, Optional

from pydantic import BaseModel

# --- 2. 数据模型 ---
class ChatRequest(BaseModel):
    # 消息内容
    message: str
    # 图片地址
    image_url: Optional[str] = None
    # 会话id
    thread_id: str