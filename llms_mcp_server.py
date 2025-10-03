#!/usr/bin/env python3.10
"""
LLMS.TXT MCP 服务器
基于MCP协议，为Web项目自动生成llms.txt文档
"""

from mcp.server.fastmcp import FastMCP
from pathlib import Path
import json
import sys
from typing import Dict, List, Any, Optional
import os

# 初始化MCP服务器
mcp = FastMCP("llms-txt-generator")


def detect_project_type(project_path: Path) -> str:
    """检测项目类型"""
    if (project_path / "package.json").exists():
        return "nodejs"
    elif (project_path / "requirements.txt").exists():
        return "python"
    elif (project_path / "pyproject.toml").exists():
        return "python"
    elif (project_path / "go.mod").exists():
        return "go"
    elif (project_path / "Cargo.toml").exists():
        return "rust"
    else:
        # 检查是否有常见的Web文件
        web_files = ["index.html", "app.js", "main.js", "app.py", "main.py"]
        for file in web_files:
            if (project_path / file).exists():
                return "web"
        return "unknown"


def get_project_info(project_path: Path) -> Dict[str, Any]:
    """获取项目基本信息"""
    project_type = detect_project_type(project_path)
    
    # 收集核心文件
    core_files = []
    important_patterns = [
        "README*", "package.json", "requirements.txt", "pyproject.toml",
        "go.mod", "Cargo.toml", "src/", "lib/", "app/", "main.*", "index.*"
    ]
    
    for pattern in important_patterns:
        if pattern.endswith('/'):
            # 处理目录
            dir_path = project_path / pattern[:-1]
            if dir_path.exists() and dir_path.is_dir():
                core_files.append(f"{pattern[:-1]}/")
        else:
            # 处理文件
            for file_path in project_path.glob(pattern):
                if file_path.is_file():
                    core_files.append(file_path.name)
    
    return {
        "name": project_path.name,
        "type": project_type,
        "core_files": sorted(list(set(core_files)))[:10],  # 最多10个核心文件
        "path": str(project_path)
    }


def generate_llms_content(project_info: Dict[str, Any]) -> str:
    """生成llms.txt内容"""
    content = f"# {project_info['name']}\n\n"
    
    # 项目描述
    description = f"{project_info['type'].upper()}项目"
    if project_info['type'] == 'nodejs':
        description += "，使用Node.js开发"
    elif project_info['type'] == 'python':
        description += "，使用Python开发"
    
    content += f"> {description}\n\n"
    
    # 核心文件部分
    content += "## 核心文件与目录\n\n"
    for file in project_info['core_files']:
        content += f"- [{file}]({file})" 
        if file.endswith('/'):
            content += "：目录"
        else:
            content += "：文件"
        content += "\n"
    
    # 项目信息部分
    content += "\n## 项目信息\n\n"
    content += f"- 项目类型：{project_info['type']}\n"
    content += f"- 项目路径：{project_info['path']}\n"
    content += f"- 核心文件数：{len(project_info['core_files'])}\n"
    
    # 使用说明部分
    content += "\n## 快速开始\n\n"
    content += "<!-- 在此添加项目的使用说明和命令 -->\n\n"
    
    # 可选资源部分
    content += "## 可选资源\n\n"
    content += "<!-- 在此添加附加文档、API参考或其他链接 -->\n"
    
    return content


@mcp.tool()
def generate_llms_txt(directory: str = ".", overview: Optional[str] = None) -> Dict[str, Any]:
    """
    为指定项目生成llms.txt文档
    
    参数:
        directory: 项目目录路径，默认为当前目录
        overview: 可选的项目概述，如果未提供则自动生成
    
    返回:
        包含生成状态和文件路径的字典
    """
    try:
        project_path = Path(directory).resolve()
        
        # 验证目录存在
        if not project_path.exists():
            return {
                "status": "error",
                "message": f"目录不存在: {directory}",
                "error_code": "DIRECTORY_NOT_FOUND"
            }
        
        if not project_path.is_dir():
            return {
                "status": "error", 
                "message": f"路径不是目录: {directory}",
                "error_code": "NOT_A_DIRECTORY"
            }
        
        # 获取项目信息
        project_info = get_project_info(project_path)
        
        # 如果提供了自定义概述，则使用
        if overview:
            project_info['custom_overview'] = overview
        
        # 生成llms.txt内容
        llms_content = generate_llms_content(project_info)
        
        # 写入文件
        llms_file_path = project_path / "llms.txt"
        with open(llms_file_path, 'w', encoding='utf-8') as f:
            f.write(llms_content)
        
        return {
            "status": "success",
            "message": "llms.txt 文件生成成功",
            "file_path": str(llms_file_path),
            "project_info": project_info,
            "content_preview": llms_content[:200] + "..." if len(llms_content) > 200 else llms_content
        }
        
    except PermissionError as e:
        return {
            "status": "error",
            "message": f"权限不足: {str(e)}",
            "error_code": "PERMISSION_ERROR"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"生成过程中出错: {str(e)}",
            "error_code": "GENERATION_ERROR"
        }


@mcp.tool()
def get_project_info_tool(directory: str = ".") -> Dict[str, Any]:
    """
    获取指定项目的详细信息
    
    参数:
        directory: 项目目录路径，默认为当前目录
    
    返回:
        包含项目详细信息的字典
    """
    try:
        project_path = Path(directory).resolve()
        
        if not project_path.exists() or not project_path.is_dir():
            return {
                "status": "error",
                "message": "目录不存在或不是有效目录",
                "error_code": "INVALID_DIRECTORY"
            }
        
        project_info = get_project_info(project_path)
        
        # 添加更多详细信息
        project_info["status"] = "success"
        project_info["file_count"] = len(list(project_path.glob("*")))
        
        return project_info
        
    except Exception as e:
        return {
            "status": "error",
            "message": f"获取项目信息失败: {str(e)}",
            "error_code": "INFO_RETRIEVAL_ERROR"
        }


@mcp.tool()
def list_projects(parent_directory: str = ".") -> Dict[str, Any]:
    """
    列出指定目录下的所有项目
    
    参数:
        parent_directory: 父目录路径，默认为当前目录
    
    返回:
        包含项目列表的字典
    """
    try:
        parent_path = Path(parent_directory).resolve()
        
        if not parent_path.exists() or not parent_path.is_dir():
            return {
                "status": "error",
                "message": "父目录不存在或不是有效目录",
                "error_code": "INVALID_PARENT_DIRECTORY"
            }
        
        projects = []
        
        # 检查父目录本身是否是一个项目
        if detect_project_type(parent_path) != "unknown":
            projects.append({
                "name": parent_path.name,
                "path": str(parent_path),
                "type": detect_project_type(parent_path)
            })
        
        # 检查子目录
        for child in parent_path.iterdir():
            if child.is_dir():
                project_type = detect_project_type(child)
                if project_type != "unknown":
                    projects.append({
                        "name": child.name,
                        "path": str(child),
                        "type": project_type
                    })
        
        return {
            "status": "success",
            "parent_directory": str(parent_path),
            "project_count": len(projects),
            "projects": projects
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": f"列出项目失败: {str(e)}",
            "error_code": "LIST_PROJECTS_ERROR"
        }


if __name__ == "__main__":
    # 运行MCP服务器，使用stdio传输方式
    print("🚀 LLMS.TXT MCP 服务器启动中...", file=sys.stderr)
    print(f"📁 工作目录: {os.getcwd()}", file=sys.stderr)
    print("🛠️  可用工具:", file=sys.stderr)
    print("  - generate_llms_txt: 生成llms.txt文档", file=sys.stderr)
    print("  - get_project_info_tool: 获取项目信息", file=sys.stderr)
    print("  - list_projects: 列出所有项目", file=sys.stderr)
    print("⏳ 等待MCP客户端连接...", file=sys.stderr)
    
    mcp.run(transport='stdio')