# LLMS.TXT MCP 服务器

[![MCP Protocol](https://img.shields.io/badge/MCP-Protocol-blue?logo=json)](https://modelcontextprotocol.io)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-green?logo=python)](https://www.python.org)
[![Trae AI IDE](https://img.shields.io/badge/Trae-AI%20IDE-purple)](https://trae.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一个基于MCP协议的本地服务器，用于自动为Web项目生成标准化的llms.txt文档。

## 📖 什么是 LLMS.TXT？

**LLMS.TXT** 是一个新兴的标准化文档格式，旨在为AI助手和大型语言模型提供项目结构信息。类似于 `robots.txt` 用于网络爬虫，`llms.txt` 为AI助手提供了项目的:

- 🏗️ **项目结构** - 核心文件和目录的映射
- 🛠️ **技术栈信息** - 使用的编程语言、框架和工具
- 📋 **项目元数据** - 类型、路径、依赖关系
- 🚀 **快速开始指南** - 如何设置和运行项目
- 🔗 **相关资源** - 文档、API参考和其他有用链接

LLMS.TXT 帮助AI助手更好地理解项目上下文，提供更准确的代码生成、问题解答和项目分析。

## 🚀 功能特性

- ✅ 自动检测项目类型（Node.js、Python、Go、Rust、Web）
- ✅ 生成符合llms.txt标准的Markdown文档
- ✅ 支持stdio传输协议，与IDE/AI助手无缝集成
- ✅ 提供项目信息查询和批量项目发现功能
- ✅ 完善的错误处理和权限管理

## 📋 系统要求

- Python 3.10+
- 支持MCP协议的IDE（Cursor、Claude Desktop等）

## 🛠️ 安装配置

### 🎯 Trae AI IDE 专属配置

Trae AI IDE 提供了原生的MCP支持，配置非常简单：

#### 方法一：通过界面配置
1. 打开 Trae AI IDE 设置
2. 进入 "MCP Servers" 部分
3. 点击 "Add Server"
4. 填写以下信息：
   - **Name**: `llms-txt-generator`
   - **Command**: `python3` (或你的Python解释器路径)
   - **Args**: `["/path/to/llms_mcp_server.py"]`
   - **Env**: `{"PYTHONPATH": "/path/to/project"}`

#### 方法二：配置文件方式
在 Trae 配置文件中添加：

```json
{
  "mcpServers": {
    "llms-txt-generator": {
      "command": "python3",
      "args": ["/path/to/llms_mcp_server.py"],
      "env": {
        "PYTHONPATH": "/path/to/project"
      }
    }
  }
}
```

#### 方法三：环境变量方式
```bash
export TRAE_MCP_SERVERS='{"llms-txt-generator": {"command": "python3", "args": ["/path/to/llms_mcp_server.py"], "env": {"PYTHONPATH": "/path/to/project"}}}'
```

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. IDE配置

#### Trae AI IDE 配置

```json
{
  "mcpServers": {
    "llms-txt-generator": {
      "command": "python3",
      "args": ["/path/to/llms_mcp_server.py"],
      "env": {
        "PYTHONPATH": "/path/to/project"
      }
    }
  }
}
```

#### Cursor 配置 (settings.json)

```json
{
  "mcpServers": {
    "llms-txt-generator": {
      "command": "python",
      "args": [
        "/绝对路径/到/llms_mcp_server.py"
      ],
      "env": {
        "PYTHONPATH": "/绝对路径/到/项目目录"
      }
    }
  }
}
```

#### Claude Desktop 配置

在Claude Desktop的设置中添加MCP服务器配置。

## 🎯 使用方法

### 🤖 Trae AI IDE 专属使用

在 Trae AI IDE 中，你可以通过以下方式使用 MCP 工具：

#### 方法一：@提及方式
```
@llms-txt-generator generate_llms_txt
```

#### 方法二：自然语言指令
- "请为当前项目生成llms.txt文档"
- "使用llms工具分析这个目录"
- "获取项目的技术栈信息"
- "列出所有可用的MCP工具"

#### 方法三：工具调用
在聊天界面中，Trae会自动识别并建议使用注册的MCP工具

### 通过其他AI助手使用

1. 在支持的IDE中打开AI聊天界面
2. 输入指令，例如：
   - "请为当前项目生成llms.txt文档"
   - "获取这个Node.js项目的详细信息"
   - "列出当前目录下的所有项目"

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
生成llms.txt文档

**参数:**
- `directory`: 项目目录路径（默认：当前目录）
- `overview`: 可选的自定义项目概述

**示例:**
```json
{
  "method": "generate_llms_txt",
  "params": {
    "directory": "./my-project",
    "overview": "一个现代化的Web应用程序"
  }
}
```

### get_project_info_tool
获取项目详细信息

**参数:**
- `directory`: 项目目录路径（默认：当前目录）

### list_projects  
列出目录下的所有项目

**参数:**
- `parent_directory`: 父目录路径（默认：当前目录）

## 📊 项目类型支持

| 类型 | 检测文件 | 支持状态 |
|------|----------|----------|
| Node.js | package.json | ✅ |
| Python | requirements.txt, pyproject.toml | ✅ |
| Go | go.mod | ✅ |
| Rust | Cargo.toml | ✅ |
| Web | index.html, app.js, main.py等 | ✅ |

## 📝 生成的llms.txt格式

```markdown
# 项目名称

> 项目描述

## 核心文件与目录

- [README.md](README.md)：文件
- [src/](src/)：目录
- [package.json](package.json)：文件

## 项目信息

- 项目类型：nodejs
- 项目路径：/path/to/project
- 核心文件数：5

## 快速开始

<!-- 在此添加项目的使用说明和命令 -->

## 可选资源

<!-- 在此添加附加文档、API参考或其他链接 -->
```

## 🐛 故障排除

### 常见问题

1. **权限错误**
   - 确保对目标目录有读写权限
   - 检查文件系统权限设置

2. **项目识别失败**
   - 确认项目包含标准的配置文件
   - 检查项目目录结构

3. **MCP连接失败**
   - 确认IDE支持MCP协议
   - 检查配置文件路径是否正确

### 错误代码

| 错误代码 | 描述 | 解决方法 |
|----------|------|----------|
| DIRECTORY_NOT_FOUND | 目录不存在 | 检查目录路径 |
| NOT_A_DIRECTORY | 路径不是目录 | 确认路径指向目录 |
| PERMISSION_ERROR | 权限不足 | 检查文件权限 |
| GENERATION_ERROR | 生成过程出错 | 查看详细错误信息 |

## 📈 性能指标

- 单个项目扫描时间：< 500ms
- 内存占用：< 50MB
- 支持并发请求：是

## 🔮 未来计划

- [ ] 支持更多项目类型（Java、Ruby、PHP等）
- [ ] 添加自定义模板支持
- [ ] 支持llms-full.txt生成
- [ ] 添加Git仓库信息集成
- [ ] 提供Web界面配置

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个项目。

## 📞 支持

如有问题，请提交GitHub Issue或联系开发团队。