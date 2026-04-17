from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pydantic_ai import RunContext
from pydantic_ai.capabilities import AbstractCapability
from pydantic_ai.capabilities.abstract import ValidatedToolArgs
from pydantic_ai.messages import ToolCallPart
from pydantic_ai.tools import ToolDefinition
from pydantic_ai.toolsets import FunctionToolset

from coding_assistant.deps import AgentDeps
import os

def _path_sandbox(path: str) -> Path:
    return Path("sandbox") / Path(path)


# 1. Implement the read_file tool
def read_file(file_path: str) -> str | None:
    """Read a file located at the given file path
    
    Parameters
    ----------
    file_path : str
        The relative path to the file to read

    Returns
    -------
    str | None
        A str with the contents of the file or None if the file does not exist

    """

    sandbox_file_path = _path_sandbox(file_path)
    if not sandbox_file_path.exists():
        return None
    
    return sandbox_file_path.read_text()

# 2. Implement the write_file tool
def write_file(file_path: str, content: str) -> None:
    """Write string content to a file located at the given file_path.
    If the file does not exist, it will be created. 
    
    Parameters
    ----------
    file_path : str
        The relative path to the file to write to
    content : str
        The content to write to the file


    """

    sandbox_file_path = _path_sandbox(file_path)
    sandbox_file_path.parent.mkdir(parents=True, exist_ok=True)

    sandbox_file_path.write_text(content)


def search_files(pattern: str) -> list[str]:
    """Search for files matching a glob pattern.

    Parameters
    ----------
    patters : str
        The glob patterns to match files (e.g., "**/*.py", "test_*.py)

    Returns
    -------
    list[str]
        A list of relative file paths matching the pattern.

    """
    sandbox_root = _path_sandbox("")
    matches = sandbox_root.glob(pattern)


    return [str(p.relative_to(sandbox_root)) for p in matches]


# 3. Implement the FileOperations capability. Override the get_toolset() method.
@dataclass
class FileOperations(AbstractCapability[Any]):
    def get_toolset(self) -> FunctionToolset:
        toolset = FunctionToolset()

        toolset.add_function(search_files)
        toolset.add_function(read_file)
        toolset.add_function(write_file)

        return toolset
    

    async def before_tool_execute(self, ctx: RunContext[AgentDeps], *, call: ToolCallPart, tool_def: ToolDefinition, args: dict[str, Any]) -> dict[str, Any]:
        if call.tool_name == "search_files":
            ctx.deps.console.log(f"Searching for files: {args.get('pattern')}")
        elif call.tool_name == "read_file":
            ctx.deps.console.log(f"Reading file: {args.get('file_path')}")
        elif call.tool_name == "write_file":
            ctx.deps.console.log(f"Writing to file: {args.get('file_path')}")
        
        return args