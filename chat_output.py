from typing import Type, Optional
from superagi.llms.base_llm import BaseLlm
from pydantic import BaseModel, Field

from superagi.tools.base_tool import BaseTool

class WriteChatInput(BaseModel):
    """Input for Chat tool."""
    content: str = Field(..., description="content to write")


class WriteChatTool(BaseTool):
    """
    Write Output tool

    """
    name: str = "Write Chat"
    args_schema: Type[BaseModel] = WriteChatInput
    description: str = "Writes text in a summarized and formated manner to chat"
    agent_id: int = None
    llm: Optional[BaseLlm] = None

    class Config:
        arbitrary_types_allowed = True

    def _execute(self, content: str):
        """
        Execute the write chat tool.

        Args:
            content : The text to write to the chat.

        Returns:
            success message if message is chat written successfully or failure message if writing chat fails.
        """
        prompt = f"Please summarize and format this answer in a readable and understandable way, {content}"
        messages = [{"role": "system", "content": prompt}]

        result = self.llm.chat_completion(messages, max_tokens=self.max_token_limit)

        print("summarized the message:", result["content"])

        return result["content"]
