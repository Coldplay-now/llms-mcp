# LLMS.TXT MCP 服务器

[![MCP Protocol](https://img.shields.io/badge/MCP-Protocol-blue?logo=json)](https://modelcontextprotocol.io)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-green?logo=python)](https://www.python.org)
[![Trae AI IDE](https://img.shields.io/badge/Trae-AI%20IDE-purple)](https://trae.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **LLMS.TXT MCP 服务器** 是一个基于MCP协议的本地服务器，用于自动为Web项目生成标准化的llms.txt文档。 


## 📖 什么是 LLMS.TXT？

**LLMS.TXT** 是一个新兴的标准化文档格式，旨在为AI助手和大型语言模型提供项目结构信息。类似于 `robots.txt` 用于网络爬虫，`llms.txt` 为AI助手提供了项目的:

- 🏗️ **项目结构** - 核心文件和目录的映射
- 🛠️ **技术栈信息** - 使用的编程语言、框架和工具
- 📋 **项目元数据** - 类型、路径、依赖关系
- 🚀 **快速开始指南** - 如何设置和运行项目
- 🔗 **相关资源** - 文档、API参考和其他有用链接 

> **在项目开发过程中，在项目根目录保留一个LLMS.TXT， 有助于AI IDE（Cursor / Claude Code / TRAE等）更好地理解项目上下文，提供更准确的代码生成、问题解答和项目分析。 防止LLM对于项目进行全盘扫描，这可以大幅优化上下文的Token的用量。**

## 🎯 解决 LLM 的"信息盲区"问题

### 问题背景

当 LLM 访问一个网站或项目时，它可能面临以下关键问题：

- **内容优先级不明确**：无法区分核心内容（如教程正文）和次要内容（如广告、导航栏）
- **结构理解偏差**：可能误解网页的章节层级或逻辑关系
- **动态内容困惑**：对需要交互（如点击展开）的内容处理不佳
- **Token 效率低下**：需要扫描大量无关内容才能找到关键信息

### LLMS.TXT 的解决方案

LLMS.TXT 通过提供结构化元数据，直接告诉 LLM：

- **"这个网站/项目是干什么的？"**（例如：description: A Python tutorial for beginners）
- **"哪些内容最重要？"**（例如：priority_paths: /tutorials/, /docs/）
- **"如何避免误解？"**（例如：ignore_sections: sidebar-ads, user-comments）
- **"技术栈是什么？"**（例如：tech_stack: Python, FastAPI, React）

### 技术本质：轻量级标准化协议

- **文件位置**：必须放在网站根目录（如 `https://example.com/llms.txt`）
- **格式规范**：采用人类和机器均可读的 Markdown 或 YAML 格式
- **内容示例**：

```markdown
# llms.txt for Example.com
description: A blog about AI and web development
primary_topics: [LLM, JavaScript, Python]
api_docs: /api/v1/docs
ignore_paths: /admin/, /tmp/
```

### 与 robots.txt 的区别

- **robots.txt**：控制爬虫能否抓取（权限控制）
- **llms.txt**：指导 LLM 如何理解（语义指导）

### 实际应用场景

- **精准问答**：当用户问 LLM"Example.com 的 API 文档在哪？"，模型可直接从 llms.txt 读取 api_docs 字段返回准确链接
- **内容摘要**：LLM 根据 description 和 primary_topics 生成更符合网站定位的摘要
- **规避噪声**：通过 ignore_paths 跳过无关内容（如评论区），提升输出质量
- **Token 优化**：避免全项目扫描，大幅减少上下文 Token 使用量

### 为什么需要 LLMS.TXT？

- **对网站主**：主动控制 LLM 如何呈现自己的内容，避免模型"胡编乱造"
- **对 LLM 开发者**：减少模型幻觉（Hallucination），提升回答准确性
- **对用户**：获得更可靠的 AI 生成答案
- **对开发者**：在AI IDE中获得更精准的代码建议和项目理解

### 争议与注意事项

- **非强制标准**：目前仍由社区推动（如 Answer.ai），并非所有 LLM 都支持
- **隐私风险**：需谨慎设置 ignore_paths，避免暴露敏感目录
- **与 SEO 的协同**：未来可能与搜索引擎的 AI 摘要功能（如 Google SGE）深度整合
- **标准化进程**：需要社区共同努力推动标准化进程

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

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. IDE配置

#### 🎯 Trae AI IDE 专属配置

Trae AI IDE 提供了原生的MCP支持，配置非常简单：

##### 方法一：通过界面配置
1. 打开 Trae AI IDE 设置
2. 进入 "MCP Servers" 部分
3. 点击 "Add Server"
4. 填写以下信息：
   - **Name**: `llms-txt-generator`
   - **Command**: `python3` (或你的Python解释器路径)
   - **Args**: `["/path/to/llms_mcp_server.py"]`
   - **Env**: `{"PYTHONPATH": "/path/to/project"}`

##### 方法二：配置文件方式
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

##### 方法三：环境变量方式
```bash
export TRAE_MCP_SERVERS='{"llms-txt-generator": {"command": "python3", "args": ["/path/to/llms_mcp_server.py"], "env": {"PYTHONPATH": "/path/to/project"}}}'
```

#### 🖥️ Cursor 配置 (settings.json)

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

#### 💻 Claude Desktop 配置

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

---

# English Version

## 📖 What is LLMS.TXT?

**LLMS.TXT** is an emerging standardized document format designed to provide project structure information for AI assistants and large language models. Similar to how `robots.txt` is used for web crawlers, `llms.txt` provides AI assistants with:

- 🏗️ **Project Structure** - Mapping of core files and directories
- 🛠️ **Tech Stack Information** - Programming languages, frameworks, and tools used
- 📋 **Project Metadata** - Type, paths, dependencies
- 🚀 **Quick Start Guide** - How to set up and run the project
- 🔗 **Related Resources** - Documentation, API references, and other useful links

> **During project development, keeping an LLMS.TXT in the project root directory helps AI IDEs (Cursor / Claude Code / TRAE, etc.) better understand the project context, providing more accurate code generation, problem-solving, and project analysis. It prevents LLMs from performing full project scans, which can significantly optimize context token usage.**

## 🚀 Features

- ✅ Automatic project type detection (Node.js, Python, Go, Rust, Web)
- ✅ Generate standardized llms.txt documents
- ✅ Support stdio transport protocol for seamless IDE/AI assistant integration
- ✅ Provide project information query and batch project discovery
- ✅ Comprehensive error handling and permission management

## 📋 System Requirements

- Python 3.10+
- IDE with MCP protocol support (Cursor, Claude Desktop, etc.)

## 🛠️ Installation & Configuration

### 🎯 Trae AI IDE Specific Configuration

Trae AI IDE provides native MCP support with simple configuration:

#### Method 1: Through UI
1. Open Trae AI IDE Settings
2. Go to "MCP Servers" section
3. Click "Add Server"
4. Fill in:
   - **Name**: `llms-txt-generator`
   - **Command**: `python3` (or your Python interpreter path)
   - **Args**: `["/path/to/llms_mcp_server.py"]`
   - **Env**: `{"PYTHONPATH": "/path/to/project"}`

#### Method 2: Config File
Add to Trae configuration file:

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

#### Method 3: Environment Variable
```bash
export TRAE_MCP_SERVERS='{"llms-txt-generator": {"command": "python3", "args": ["/path/to/llms_mcp_server.py"], "env": {"PYTHONPATH": "/path/to/project"}}}'
```

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. IDE Configuration

#### Trae AI IDE Configuration

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

#### Cursor Configuration (settings.json)

```json
{
  "mcpServers": {
    "llms-txt-generator": {
      "command": "python",
      "args": [
        "/absolute/path/to/llms_mcp_server.py"
      ],
      "env": {
        "PYTHONPATH": "/absolute/path/to/project/directory"
      }
    }
  }
}
```

#### Claude Desktop Configuration

Add MCP server configuration in Claude Desktop settings.

## 🎯 Usage

### 🤖 Trae AI IDE Specific Usage

In Trae AI IDE, you can use MCP tools through:

#### Method 1: @mention
```
@llms-txt-generator generate_llms_txt
```

#### Method 2: Natural Language Commands
- "Please generate llms.txt document for current project"
- "Use llms tool to analyze this directory"
- "Get project tech stack information"
- "List all available MCP tools"

#### Method 3: Tool Invocation
Trae will automatically recognize and suggest using registered MCP tools in chat interface

### Through Other AI Assistants

1. Open AI chat interface in supported IDE
2. Enter commands, e.g.:
   - "Please generate llms.txt for current project"
   - "Get detailed information about this Node.js project"
   - "List all projects in current directory"

### Direct Command Line Usage

```bash
# Generate llms.txt for current directory
python llms_mcp_server.py --generate

# Generate llms.txt for specified directory  
python llms_mcp_server.py --generate --directory /path/to/project

# Get project information
python llms_mcp_server.py --info --directory /path/to/project
```

## 🔧 Available Tools

### generate_llms_txt
Generate llms.txt document

**Parameters:**
- `directory`: Project directory path (default: current directory)
- `overview`: Optional custom project overview

**Example:**
```json
{
  "method": "generate_llms_txt",
  "params": {
    "directory": "./my-project",
    "overview": "A modern web application"
  }
}
```

### get_project_info_tool
Get detailed project information

**Parameters:**
- `directory`: Project directory path (default: current directory)

### list_projects  
List all projects in directory

**Parameters:**
- `parent_directory`: Parent directory path (default: current directory)

## 📊 Supported Project Types

| Type | Detection Files | Support Status |
|------|-----------------|----------------|
| Node.js | package.json | ✅ |
| Python | requirements.txt, pyproject.toml | ✅ |
| Go | go.mod | ✅ |
| Rust | Cargo.toml | ✅ |
| Web | index.html, app.js, main.py, etc. | ✅ |

## 📝 Generated llms.txt Format

```markdown
# Project Name

> Project Description

## Core Files & Directories

- [README.md](README.md)：File
- [src/](src/)：Directory
- [package.json](package.json)：File

## Project Information

- Project Type：nodejs
- Project Path：/path/to/project
- Core File Count：5

## Quick Start

<!-- Add project usage instructions and commands here -->

## Optional Resources

<!-- Add additional documentation, API references, or other links here -->
```

## 🐛 Troubleshooting

### Common Issues

1. **Permission Errors**
   - Ensure read/write permissions for target directory
   - Check filesystem permission settings

2. **Project Recognition Failure**
   - Confirm project contains standard configuration files
   - Check project directory structure

3. **MCP Connection Failure**
   - Confirm IDE supports MCP protocol
   - Check configuration file paths are correct

### Error Codes

| Error Code | Description | Solution |
|------------|-------------|----------|
| DIRECTORY_NOT_FOUND | Directory does not exist | Check directory path |
| NOT_A_DIRECTORY | Path is not a directory | Confirm path points to directory |
| PERMISSION_ERROR | Insufficient permissions | Check file permissions |
| GENERATION_ERROR | Generation process error | View detailed error information |

## 📈 Performance Metrics

- Single project scan time: < 500ms
- Memory usage: < 50MB
- Supports concurrent requests: Yes

## 🔮 Future Plans

- [ ] Support more project types (Java, Ruby, PHP, etc.)
- [ ] Add custom template support
- [ ] Support llms-full.txt generation
- [ ] Add Git repository information integration
- [ ] Provide web interface configuration

## 📄 License

MIT License

## 🤝 Contributing

Welcome to submit Issues and Pull Requests to improve this project.

## 📞 Support

If you have questions, please submit GitHub Issue or contact the development team.