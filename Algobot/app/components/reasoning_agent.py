import re
from langchain_core.messages import HumanMessage, SystemMessage
from app import llm

def ReasoningAgent(problem: str) -> dict:
    system = """
    You're a reasoning assistant. Given a coding problem, return exactly three sections formatted like below:

    Explanation:
    (Explain the intuition and reasoning.)

    Algorithm:
    (Provide numbered steps from input to output.)

    Motivational Quote:
    (Give a short, inspiring quote about programming or persistence.)

    ❌ Do not include any code.
    """
    messages = [SystemMessage(content=system), HumanMessage(content=problem)]
    content = llm.invoke(messages).content

    sections = {"explanation": "", "algorithm": "", "quote": ""}
    patterns = {
        "explanation": r"(?i)Explanation:([\s\S]*?)(Algorithm:|Motivational Quote:)",
        "algorithm": r"(?i)Algorithm:([\s\S]*?)(Motivational Quote:)",
        "quote": r"(?i)Motivational Quote:([\s\S]*)"
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, content)
        if match:
            sections[key] = match.group(1).strip()
    return sections