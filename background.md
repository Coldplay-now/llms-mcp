llms.txt 介绍
1
2
llms.txt 是一种新兴的文件标准，旨在为大型语言模型（LLM）提供优化的内容结构，帮助 AI 更高效地理解和处理网站信息。它通过精简和结构化的方式，将网站的核心内容提炼为 Markdown 格式，去除导航菜单、广告和复杂脚本等干扰项，从而提升 AI 的解析效率。

llms.txt 的核心功能

llms.txt 文件主要分为两种类型：

/llms.txt：提供网站内容的高层次概览，帮助 AI 快速掌握网站结构和关键资源。

/llms-full.txt（可选）：包含完整的文档内容，适用于需要深入了解的场景，如技术文档或 API 参考。

文件格式采用 Markdown 结构，包含以下部分：

一个 H1 标题，标明项目或网站名称。

简短的项目摘要，帮助 AI 理解文件内容。

以 H2 标题分隔的部分，列出关键资源的链接及简要说明。

示例格式如下：

# 示例项目
> 一个用来演示 llms.txt 功能的简单项目。

## 核心文档
- [快速入门](https://example.com/quickstart "快速入门")：教你怎么快速用起来。
- [API 文档](https://example.com/api "API 文档")：所有 API 的详细说明。

## 示例代码
- [GitHub 仓库](https://github.com/example/repo "GitHub 仓库")：完整的代码都在这儿。

## 联系方式
- https://example.com/contact
复制
llms.txt 的优势

优化 AI 理解：通过结构化内容，帮助 LLM 快速抓住重点，避免被页面样式干扰。

提升效率：精简的内容格式减少了上下文窗口的占用，使 AI 能更高效地处理大规模数据。

双重可读性：Markdown 格式既适合人类阅读，也便于机器解析。

补充现有标准：与 robots.txt 和 sitemap.xml 不同，llms.txt 专注于为 AI 提供内容概要，而非爬取权限或页面索引。

应用场景

llms.txt 主要用于以下领域：

技术文档：如编程指南、API 参考等，帮助 AI 更快回答开发者问题。

电商与教育：优化产品介绍和课程资料的呈现方式。

个人博客：提升内容清晰度，便于 AI 理解。

工具支持

目前已有多种工具支持自动生成 llms.txt 文件：

Mintlify：为托管文档自动生成 llms.txt 和 llms-full.txt 文件。

Firecrawl：通过爬取网站内容生成符合标准的 llms.txt 文件。

SiteSpeakAI：在线工具，输入域名即可生成文件。

未来发展

llms.txt 提供了一种标准化方法，让 AI 更高效地与网站内容互动。尽管目前仍处于早期阶段，但其潜力巨大，尤其在技术文档和 API 场景中表现突出。未来，随着更多开发者和平台的采用，llms.txt 有望成为 AI 优化内容呈现的主流标准。



系统架构概述

这个MCP Server采用stdio传输机制，整体架构包含三个主要组件：客户端(IDE/AI助手) → MCP传输层(stdio) → LLMS.txt生成服务。

🔧 静态拓扑图

graph TB
    %% 客户端层
    A[客户端<br/>IDE/AI助手<br/>Claude/Cursor等]
    
    %% MCP协议层
    B[MCP传输层<br/>Stdio管道<br/>JSON-RPC over stdio]
    
    %% 服务层
    subgraph C [LLMS.txt生成服务]
        C1[请求路由器<br/>MCP Router]
        C2[工具管理器<br/>Tool Manager]
        
        subgraph C3 [核心业务模块]
            C31[项目扫描器<br/>Project Scanner]
            C32[文件分析器<br/>File Analyzer]
            C33[模板引擎<br/>Template Engine]
            C34[文档生成器<br/>Document Generator]
        end
        
        subgraph C4 [数据存储]
            C41[项目缓存<br/>Project Cache]
            C42[配置管理<br/>Config Manager]
        end
    end
    
    %% 文件系统层
    D[本地文件系统<br/>项目目录]
    
    %% 连接关系
    A -->|启动进程<br/>stdin/stdout| B
    B -->|JSON-RPC调用| C1
    C1 -->|路由分发| C2
    C2 -->|调用工具| C3
    C3 -->|读取/分析| D
    C3 -->|写入文档| D
    C3 -->|缓存数据| C41
    C31 -->|读取配置| C42
    
    %% 样式定义
    classDef client fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef transport fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef service fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px
    classDef module fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef storage fill:#fce4ec,stroke:#880e4f,stroke-width:2px
    classDef filesystem fill:#e0f2f1,stroke:#004d40,stroke-width:2px
    
    class A client
    class B transport
    class C service
    class C3 module
    class C4 storage
    class D filesystem


⏱️ 时序图：生成llms.txt的完整流程

sequenceDiagram
    participant C as 客户端<br/>(IDE/AI助手)
    participant T as MCP传输层<br/>(Stdio)
    participant R as 请求路由器
    participant TM as 工具管理器
    participant PS as 项目扫描器
    participant FA as 文件分析器
    participant DG as 文档生成器
    participant FS as 文件系统

    Note over C,FS: 初始化阶段
    C->>T: 启动MCP服务器进程
    T->>R: 建立stdio通信管道
    R->>T: 发送初始化完成信号
    T->>C: 服务器就绪
    
    Note over C,FS: 工具调用阶段
    C->>T: 发送generate_llms_txt请求<br/>(JSON-RPC over stdio)
    T->>R: 解析并转发请求
    R->>TM: 路由到工具管理器
    
    Note over TM,DG: 项目分析阶段
    TM->>PS: 调用项目扫描器
    PS->>FS: 遍历项目目录结构
    FS->>PS: 返回文件列表
    PS->>FA: 分析项目类型和结构
    FA->>FS: 读取关键文件(package.json等)
    FS->>FA: 返回文件内容
    FA->>TM: 返回项目分析结果
    
    Note over TM,DG: 文档生成阶段
    TM->>DG: 调用文档生成器
    DG->>DG: 应用模板引擎生成内容
    DG->>FS: 写入llms.txt文件
    FS->>DG: 返回写入结果
    
    Note over DG,C: 响应返回阶段
    DG->>TM: 返回生成结果
    TM->>R: 返回工具执行结果
    R->>T: 封装为JSON-RPC响应
    T->>C: 通过stdio返回结果
    
    Note over C,FS: 完整流程结束


核心组件详细说明

1. MCP传输层 (Stdio)

• 职责: 处理进程间通信，使用JSON-RPC over stdio

• 输入: 从stdin读取客户端请求

• 输出: 向stdout写入服务器响应

• 特点: 无网络延迟，进程隔离安全

2. 工具管理器 (Tool Manager)

# 伪代码示例
class ToolManager:
    def handle_request(self, method: str, params: dict):
        if method == "generate_llms_txt":
            return self.generate_llms_txt(params)
        elif method == "get_project_info":
            return self.get_project_info(params)


3. 项目扫描器 (Project Scanner)

• 递归遍历目录树

• 识别项目类型(Python/Node.js/Go等)

• 排除无关目录(node_modules, .git等)

4. 文档生成器 (Document Generator)

• 基于分析结果填充模板

• 处理Markdown格式

• 错误处理和回滚机制

📊 数据流总结

1. 请求流: 客户端 → stdio → 路由器 → 工具 → 业务模块
2. 数据流: 文件系统 → 分析器 → 生成器 → 文件系统  
3. 响应流: 业务模块 → 工具 → 路由器 → stdio → 客户端

这种架构确保了职责分离、易于测试和扩展，同时通过stdio机制提供了高效的本地通信。


你想开发一个MCP Server来管理和更新项目的 llms.txt 文档，这个想法很棒，它能将本地项目信息与AI能力连接起来。下面我为你梳理一下实现思路、关键步骤和代码示例。

🛠️ 项目信息管理与llms.txt生成MCP服务方案

实现一个能够获取项目信息并自动生成/更新 llms.txt 文件的MCP Server，核心是结合本地文件系统操作、项目信息提取以及MCP协议封装。下面是一个综合的实现方案。

核心功能设计

首先，我们明确这个MCP Server需要具备的核心能力：

1.  项目信息获取：扫描当前目录，识别项目结构、文件类型和关键文件。
2.  llms.txt生成与更新：根据提取的项目信息，创建或更新符合规范的llms.txt Markdown文件。
3.  MCP工具暴露：通过MCP协议提供这些功能，使得AI助手（如Cursor、Claude）能够调用它们。

技术栈与依赖

实现该MCP Server，你需要以下Python库：
pip install mcp fastapi uvicorn

mcp 库是核心，用于构建MCP服务器；fastapi 和 uvicorn 用于创建Web服务器（如果你选择SSE传输方式）。

实现步骤与代码示例

1. 创建MCP服务器框架

首先，搭建一个基本的MCP服务器结构。
from mcp.server.fastmcp import FastMCP
import os
from pathlib import Path
from typing import List, Dict, Any

# 初始化MCP服务器，给它取个名字
mcp = FastMCP("llms.txt Manager")

@mcp.tool()
def get_project_info(directory: str = ".") -> Dict[str, Any]:
    """
    获取指定目录下的项目信息，包括文件结构、类型和关键文件。
    
    Args:
        directory: 项目目录路径，默认为当前目录.
    
    Returns:
        包含项目信息的字典，例如文件列表、项目类型等。
    """
    project_path = Path(directory).resolve()
    if not project_path.exists() or not project_path.is_dir():
        return {"error": f"目录不存在或不是有效目录: {directory}"}
    
    all_files = []
    total_size = 0
    file_types = set()
    
    # 遍历项目目录，收集信息
    for file_path in project_path.rglob('*'):
        if file_path.is_file():
            try:
                relative_path = str(file_path.relative_to(project_path))
                all_files.append({
                    "name": relative_path,
                    "size": file_path.stat().st_size,
                    "modified": file_path.stat().st_mtime
                })
                total_size += file_path.stat().st_size
                file_types.add(file_path.suffix.lower())
            except OSError:
                # 跳过无权限访问的文件
                pass
    
    # 尝试识别项目类型（例如Python、JavaScript、Go等）
    project_type = "unknown"
    if any(fname == 'package.json' for fname in [f['name'] for f in all_files]):
        project_type = "JavaScript/Node.js"
    elif any(fname == 'requirements.txt' or fname.endswith('.py') for fname in [f['name'] for f in all_files]):
        project_type = "Python"
    elif any(fname == 'go.mod' for fname in [f['name'] for f in all_files]):
        project_type = "Go"
    elif any(fname == 'Cargo.toml' for fname in [f['name'] for f in all_files]):
        project_type = "Rust"
    
    return {
        "directory": str(project_path),
        "total_files": len(all_files),
        "total_size": total_size,
        "file_types": list(file_types),
        "project_type": project_type,
        "files": all_files[:50]  # 返回前50个文件，避免数据量过大
    }


2. 实现llms.txt生成与更新工具

这是核心功能，根据项目信息生成结构化的llms.txt文件。
@mcp.tool()
def generate_llms_txt(directory: str = ".", overview: str = None) -> Dict[str, str]:
    """
    为指定项目生成或更新llms.txt文件。
    
    Args:
        directory: 项目目录路径，默认为当前目录.
        overview: 项目的简短概述，如果未提供则会自动生成一个基础的.
    
    Returns:
        操作结果的状态和信息.
    """
    project_path = Path(directory).resolve()
    llms_file_path = project_path / "llms.txt"
    
    # 获取项目信息
    project_info = get_project_info(directory)
    if "error" in project_info:
        return {"status": "error", "message": project_info["error"]}
    
    # 如果没有提供概述，则生成一个基础的
    if not overview:
        overview = f"{project_info['project_type']}项目位于 {project_info['directory']}，包含 {project_info['total_files']} 个文件。"
    
    # 构建llms.txt的内容
    llms_content = f"# {project_path.name}\n\n"
    llms_content += f"> {overview}\n\n"
    
    llms_content += "## 核心文件与目录\n\n"
    
    # 添加关键文件，优先识别常见的重要文件
    important_files = []
    for file_info in project_info["files"]:
        file_name = file_info["name"]
        if any(key_file in file_name for key_file in ['README', 'package.json', 'requirements.txt', 'main.py', 'app.py', 'index.js', 'src/', 'lib/']):
            important_files.append(file_info)
    
    for file_info in important_files[:10]:  # 最多列出10个关键文件
        llms_content += f"- [{file_info['name']}]({file_info['name']}): 文件大小: {file_info['size']} 字节\n"
    
    llms_content += "\n## 项目结构\n\n"
    llms_content += f"- 项目类型: {project_info['project_type']}\n"
    llms_content += f"- 总文件数: {project_info['total_files']}\n"
    llms_content += f"- 文件类型: {', '.join(project_info['file_types'])}\n"
    
    llms_content += "\n## 如何使用\n\n"
    llms_content += "<!-- 在此添加项目的简要使用说明或命令 -->\n\n"
    
    llms_content += "## 可选信息\n\n"
    llms_content += "<!-- 在此添加附加资源、API参考或其他链接 -->\n"
    
    # 写入llms.txt文件
    try:
        with open(llms_file_path, 'w', encoding='utf-8') as f:
            f.write(llms_content)
        
        return {
            "status": "success",
            "message": f"llms.txt 文件已成功生成于 {llms_file_path}",
            "file_path": str(llms_file_path)
        }
    except Exception as e:
        return {"status": "error", "message": f"写入文件时出错: {str(e)}"}


3. 添加更多实用工具

为了让你的MCP Server更强大，可以添加一些辅助工具。
@mcp.tool()
def update_llms_overview(directory: str = ".", new_overview: str = None) -> Dict[str, str]:
    """
    更新现有llms.txt文件的概述部分。
    
    Args:
        directory: 项目目录路径，默认为当前目录.
        new_overview: 新的项目概述.
    
    Returns:
        操作结果的状态和信息.
    """
    if not new_overview:
        return {"status": "error", "message": "必须提供新的概述内容"}
    
    project_path = Path(directory).resolve()
    llms_file_path = project_path / "llms.txt"
    
    if not llms_file_path.exists():
        return {"status": "error", "message": "当前目录下不存在llms.txt文件"}
    
    try:
        with open(llms_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 替换概述部分
        if "> " in content and "\n\n" in content:
            parts = content.split("> ", 1)
            if len(parts) > 1:
                remaining = parts[1].split("\n\n", 1)
                if len(remaining) > 1:
                    new_content = parts[0] + "> " + new_overview + "\n\n" + remaining[1]
                    
                    with open(llms_file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    return {"status": "success", "message": "llms.txt 概述已更新"}
        
        return {"status": "error", "message": "无法解析现有的llms.txt文件格式"}
    except Exception as e:
        return {"status": "error", "message": f"更新文件时出错: {str(e)}"}

@mcp.tool()
def list_projects(parent_directory: str = ".") -> List[str]:
    """
    列出指定父目录下所有可能包含项目的子目录。
    
    Args:
        parent_directory: 要搜索的父目录路径.
    
    Returns:
        可能包含项目的目录路径列表.
    """
    parent_path = Path(parent_directory).resolve()
    potential_projects = []
    
    for child in parent_path.iterdir():
        if child.is_dir():
            # 检查目录是否包含项目特征文件
            has_package_json = (child / 'package.json').exists()
            has_requirements = (child / 'requirements.txt').exists()
            has_gomod = (child / 'go.mod').exists()
            has_pyproject = (child / 'pyproject.toml').exists()
            
            if has_package_json or has_requirements or has_gomod or has_pyproject:
                potential_projects.append(str(child))
    
    return potential_projects


4. 主程序入口

if __name__ == "__main__":
    # 运行MCP服务器，使用stdio传输方式（适合与IDE/编辑器集成）
    mcp.run(transport='stdio')


📋 配置与使用

MCP服务器配置

要让你喜欢的代码编辑器或AI助手（如Cursor、Claude Desktop）识别并使用这个MCP Server，通常需要在编辑器的设置文件中进行配置。

VSCode/Cursor 配置示例 (settings.json):
{
  "mcpServers": {
    "llms-txt-manager": {
      "command": "python",
      "args": [
        "/绝对路径/到/你的/llms_mcp_server.py"
      ],
      "env": {
        "PYTHONPATH": "/你的/项目/路径"
      }
    }
  }
}


通过AI助手使用

配置成功后，你就可以在AI助手（如Cursor）中直接使用定义的工具了：

1.  打开AI聊天界面（通常在Cursor中是 Cmd+L 或 Ctrl+L）。
2.  输入类似指令：“请帮我为当前项目生成一个llms.txt文件”或“获取这个项目的信息”。
3.  AI助手会调用你开发的MCP Server工具来完成请求。

💡 扩展建议

你的MCP Server可以进一步扩展，使其更强大：

•   支持更多项目类型：增强项目识别逻辑，支持Java（pom.xml）、Ruby（Gemfile）、PHP（composer.json）等。

•   深度分析关键文件：解析README.md、package.json或requirements.txt等文件，提取更详细的信息（如项目依赖、脚本命令等）并纳入llms.txt。

•   版本控制集成：检查项目是否为Git仓库，如果是，可以将当前分支、最新提交等信息包含在llms.txt中。

•   自定义模板：允许用户通过配置文件或参数自定义llms.txt的Markdown模板。

•   自动化更新：监听项目文件变化，在特定事件（如添加新文件、更新README）时自动更新llms.txt。

⚠️ 注意事项

•   权限问题：确保MCP Server有权限访问和写入目标目录。

•   错误处理：在实际部署时，应加强错误处理，避免因个别文件无法访问而导致整个工具失败。

•   性能考虑：对于非常大的项目目录，遍历所有文件可能较慢，可以考虑添加深度限制或排除某些目录（如node_modules, venv）。

•   安全性：如果你的MCP Server会暴露给网络环境（使用SSE传输时），务必设置适当的权限控制和认证机制。

这个MCP Server将为你的项目提供一种结构化的方式与AI助手分享上下文，从而获得更准确、更具相关性的帮助。