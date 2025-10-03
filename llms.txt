# LLMS.TXT MCP 服务器

> 基于MCP协议的自动化llms.txt文档生成工具，支持多种项目类型检测和标准化文档生成

## 🎯 项目概述

这是一个专为AI助手和开发者设计的MCP服务器，能够自动分析项目结构并生成符合llms.txt标准的文档。支持Node.js、Python、Go、Rust和Web项目的智能识别。

## 📁 核心文件与目录

- [README.md](README.md)：详细的项目说明文档
- [requirements.txt](requirements.txt)：Python依赖包列表
- [llms_mcp_server.py](llms_mcp_server.py)：主服务器程序
- [PRD_LLMS_TXT_MCP_SERVER_v1.0.md](PRD_LLMS_TXT_MCP_SERVER_v1.0.md)：产品需求文档
- [background.md](background.md)：项目背景和技术方案
- [trae_mcp_config.json](trae_mcp_config.json)：Trae IDE配置模板

## 🛠️ 技术栈

- **语言**: Python 3.10+
- **框架**: FastMCP (MCP协议实现)
- **依赖**: FastAPI, Uvicorn, Jinja2
- **协议**: MCP (Model Context Protocol)

## 📊 项目信息

- **项目类型**: python
- **项目路径**: /path/to/project
- **核心文件数**: 6
- **Python版本**: 3.10+
- **协议支持**: MCP stdio

## 🚀 快速开始

### 安装依赖
```bash
pip install -r requirements.txt
```

### 启动MCP服务器
```bash
python llms_mcp_server.py
```

### 通过AI助手使用
在支持的IDE中，可以通过以下指令使用：
- "@llms-txt-generator generate_llms_txt" - 生成当前目录的llms.txt
- "@llms-txt-generator get_project_info_tool" - 获取项目详细信息
- "@llms-txt-generator list_projects" - 列出所有项目

### 直接命令行使用
```bash
# 生成当前目录的llms.txt
python llms_mcp_server.py --generate

# 生成指定目录的llms.txt
python llms_mcp_server.py --generate --directory /path/to/project

# 获取项目信息
python llms_mcp_server.py --info --directory /path/to/project
```

## 🔧 可用工具

### generate_llms_txt
生成标准化的llms.txt文档，支持自定义项目概述

### get_project_info_tool  
获取项目的详细技术信息和文件结构

### list_projects
发现并列出目录中的所有有效项目

## 📋 支持的项目类型

| 项目类型 | 检测文件 | 支持状态 |
|----------|----------|----------|
| Node.js | package.json | ✅ 完全支持 |
| Python | requirements.txt, pyproject.toml | ✅ 完全支持 |
| Go | go.mod | ✅ 完全支持 |
| Rust | Cargo.toml | ✅ 完全支持 |
| Web项目 | index.html, app.js, main.py等 | ✅ 基本支持 |

## ⚙️ IDE集成配置

### Trae AI IDE 配置
```json
{
  "mcpServers": {
    "llms-txt-generator": {
      "command": "python3",
      "args": ["/path/to/llms_mcp_server.py"],
      "env": {"PYTHONPATH": "/path/to/project"}
    }
  }
}
```

### Cursor IDE 配置
```json
{
  "mcpServers": {
    "llms-txt-generator": {
      "command": "python",
      "args": ["/绝对路径/到/llms_mcp_server.py"],
      "env": {"PYTHONPATH": "/绝对路径/到/项目目录"}
    }
  }
}
```

## 📊 性能特性

- **扫描速度**: < 500ms 每个项目
- **内存占用**: < 50MB
- **并发支持**: 多请求并行处理
- **错误处理**: 完善的异常捕获和日志记录

## 🔮 功能特性

- ✅ 多项目类型自动检测
- ✅ 标准化llms.txt文档生成
- ✅ MCP协议标准兼容
- ✅ 实时项目信息查询
- ✅ 批量项目发现
- ✅ 权限和错误管理
- ✅ 自定义配置支持

## 📝 依赖包

```
mcp>=0.3.0
fastapi>=0.104.0
uvicorn>=0.24.0
python-multipart>=0.0.6
Jinja2>=3.1.2
```

## 🐛 故障排除

### 常见问题解决方案
1. **ModuleNotFoundError**: 确保已安装所有依赖包
2. **权限错误**: 检查目录读写权限
3. **连接失败**: 确认IDE支持MCP协议
4. **项目识别失败**: 验证项目包含标准配置文件

### 获取帮助
- 查看详细文档: [README.md](README.md)
- 检查项目需求: [PRD_LLMS_TXT_MCP_SERVER_v1.0.md](PRD_LLMS_TXT_MCP_SERVER_v1.0.md)
- 查看技术方案: [background.md](background.md)

## 📞 支持与贡献

欢迎提交Issue报告问题或提出新功能建议。项目采用MIT许可证开源。

---
*本文件由 LLMS.TXT MCP 服务器自动生成*
