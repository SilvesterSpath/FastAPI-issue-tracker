from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

class IssueStatus(str, Enum):
  open = "open"
  closed = "closed"
  in_progress = "in_progress"

class IssuePriority(str, Enum):
  low = "low"
  medium = "medium"
  high = "high"

class IssueCreate(BaseModel):
  title: str = Field(min_length=3, max_length=100)
  description: str = Field(min_length=5, max_length=1000)
  priority: IssuePriority = Field(default=IssuePriority.medium)

class IssueUpdate(BaseModel):
  title: Optional[str] = Field(default=None, max_length=100)
  description: Optional[str] = Field(default=None, max_length=1000)
  priority: Optional[IssuePriority] = None
  status: Optional[IssueStatus] = None

class IssueResponse(BaseModel):
  id: str
  title: str
  description: str
  priority: IssuePriority
  status: IssueStatus
