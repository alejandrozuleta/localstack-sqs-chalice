from enum import Enum

class ClientStatuses(str, Enum):
    ACTIVE = "Active"
    PENDING = "Pending"
    DISABLED = "Disabled"