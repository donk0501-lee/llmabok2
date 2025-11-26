import os
from google.adk.tools.mcp_tool import MCPToolset, StdioConnectionParams
from mcp.client.stdio import StdioServerParameters

TARGET_FOLDER_PATH = ".."
filesystem_toolset = MCPToolset(
    connection_params = StdioConnectionParams(
        server_params = StdioServerParameters(
            command="npx",
            args=[
                "-y",  # Argument for npx to auto-confirm install
                "@modelcontextprotocol/server-filesystem",
                os.path.abspath(TARGET_FOLDER_PATH),
            ]
        )
    )
)

from google.adk.agents import Agent

root_agent = Agent(
    model="gemini-2.5-flash",
    name="filesystem_agent",
    instruction="파일 시스템과 상호작용하는 에이전트입니다. 파일을 읽고 쓰기 위해 'filesystem_toolset' 도구 세트를 사용하십시오.",
    tools=[filesystem_toolset],
)
