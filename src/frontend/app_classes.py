from dataclasses import dataclass, field
from typing import List, Literal
import uuid

@dataclass
class Message:
    role: Literal["model", "user"] = "user"
    content: str = ""
    msg_type: str = ""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))