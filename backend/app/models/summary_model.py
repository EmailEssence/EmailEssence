from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import List, Optional

class SummarySchema(BaseModel):
    email_id: str
    summary_text: str
    keywords: List[str]
    generated_at: Optional[datetime] = datetime.now() # TODO : UTC?
    class Config:
        frozen = True # Immutable!