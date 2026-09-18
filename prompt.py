from dataclasses import dataclass
from typing import List
from typing import List,Optional
@dataclass
class Prompt:
    id:int
    title:str
    template:str
    tags:List[str]
    description:Optional[str]=None
    is_active:bool=True
p1=Prompt(
    id=1,
    title="Python Bug Fixer",
    template="You are an expert Python developer.Find the bugs",
    tags=["python","debugging"],
)
p2 = Prompt(
    id=2,
    title="SQL Generator",
    template="Write a SQL query for: {request}",
    tags=["database", "sql"],
    description="Generates optimized PostgreSQL queries from natural language requests.",
)
print(p1)
print(p2)

