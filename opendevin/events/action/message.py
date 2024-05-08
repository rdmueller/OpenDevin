from dataclasses import dataclass

from opendevin.core.schema import ActionType

from .action import Action


@dataclass
class MessageAction(Action):
    content: str
    wait_for_response: bool = False
    action: str = ActionType.MESSAGE

    @property
    def message(self) -> str:
        return self.content
