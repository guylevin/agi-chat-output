from abc import ABC
from typing import List
from superagi.tools.base_tool import BaseTool, BaseToolkit
from superagi.tools.chat_output.chat_output import WriteChatTool

class ChatToolkit(BaseToolkit, ABC):
    name: str = "Chat Toolkit"
    description: str = "Chat Tool kit contains all tools related to chat output operations"

    def get_tools(self) -> List[BaseTool]:
        return [WriteChatTool()]

    def get_env_keys(self) -> List[str]:
        return []
