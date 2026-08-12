# AI 私人厨师

一个基于多模态大模型的AI私人厨师应用。用户上传食材图片，Agent自动识别食材、搜索食谱，从营养价值和制造难度多维度评分排序，返回结构化的推荐报告。

## 核心特性

- 多模态识别：支持上传图片，大模型自动识别食材与可用量
- 智能搜索：调用Tavily搜索引擎检索菜谱
- 多维度评分排序：从营养价值和制造难度两个维度量化打分
- 结构化推荐报告：包含食谱信息、得分、推荐理由的完整建议报告
- 流式对话：基于 SSE (Server-Sent Events) 的实时流式响应
- 会话管理：支持多轮历史记录，可切换、删除历史会话
- Markdown渲染：AI回复自动渲染为格式化内容
- 记忆管理：基于sqlite数据库管理多轮会话记录
- 对象存储：发送图片的同时，图片存储至对象存储空间，节省token



## 效果展示

![image](assets/pasted-image-1786505752321.png)

![image](assets/pasted-image-1786505814664.png)

## 技术栈

### 后端

| 技术                          | 版本      | 用途           |
| :-------------------------- | :------ | :----------- |
| fastapi                     | 0.141.1 | Web服务框架      |
| langchain                   | 1.3.14  | LLM应用框架      |
| langgraph-checkpoint-sqlite | 3.1.1   | 会话记忆存储       |
| langchain-tavily            | 0.2.18  | 网络搜索工具       |
| langchain-openai            | 1.4.2   | 集成openai sdk |
| OSS v2                      | 1.3.2   | 对象存储         |

### 前端

| 技术               | 版本     | 用途                 |
| :--------------- | :----- | :----------------- |
| Nextjs           | 16.3.0 | SSR框架              |
| react            | 19.2.8 | 前端框架               |
| react-markdown   | 10.1.0 | 消息显示格式             |
| lucide-react     | 1.31.0 | 图标库                |
| clsx             | 2.1.1  | 管理css样式类           |
| remark-gfm       | 4.0.1  | 实现github风格markdown |
| tailwind-merge   | 3.6.0  | 样式框架               |

## 快速开始

1. 克隆项目

   ```sh
   git clone https://github.com/hello-sloth/PersonalChief.git
   ```
2. 配置环境变量

   ```
   cd backend                                                                      
   编辑.env文件
   修改DASHSCOPE_API_KEY、DASHSCOPE_BASE_URL、TAVILY_API_KEY、OSS_ACCESS_KEY_ID、OSS_ACCESS_KEY_SECRET、OSS_BUCKET                                                                                                                                                          
   ```
3. 启动后端

   ```
   python -m app.main
   ```
4. 启动前端

   ```
   cd ../frontend                                                                      npm install && npm run dev                                                                                        
   ```

