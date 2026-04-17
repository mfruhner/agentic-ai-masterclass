from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from pydantic_ai import RunContext
from pydantic_ai.capabilities import AbstractCapability
from pydantic_ai.settings import ModelSettings


# 1. Implement the ReasoningEffort capability.
#    Override the get_model_settings() method.
@dataclass
class ReasoningEffort(AbstractCapability[Any]):

    def get_model_settings(self) -> Callable[[RunContext[Any]], ModelSettings]:
        def _set_reasoning_effort(
            ctx: RunContext[Any]
        ) -> ModelSettings:
            p = str(ctx.prompt)
            effort = "medium"
            if "@low" in p:
                effort = "low"
            elif "@high" in p:
                effort = "high"

            ctx.deps.console.log(f"Setting reasoning effort to {effort}")
            return ModelSettings(
                thinking=effort,
            )
        return _set_reasoning_effort