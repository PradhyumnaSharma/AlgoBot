import re
from langchain_core.messages import HumanMessage, SystemMessage
from app import llm

def CodingAgent(problem: str) -> dict:
    system = """
    You are a coding assistant. Return the following in Markdown format:

    ### Python Brute Force Solution
    ```python
    ...
    ```

    ### Python Optimal Solution
    ```python
    ...
    ```

    ### C++ Brute Force Solution
    ```cpp
    ...
    ```

    ### C++ Optimal Solution
    ```cpp
    ...
    ```

    ### Java Brute Force Solution
    ```java
    ...
    ```

    ### Java Optimal Solution
    ```java
    ...
    ```

    Do not include explanation, only code blocks.
    """
    messages = [SystemMessage(content=system), HumanMessage(content=problem)]
    content = llm.invoke(messages).content

    def extract_block(label, lang):
        match = re.search(rf"### {label} Solution\s+```{lang}\n([\s\S]*?)```", content)
        return match.group(1).strip() if match else ""

    return {
        "py_brute": extract_block("Python Brute Force", "python"),
        "py_opt": extract_block("Python Optimal", "python"),
        "cpp_brute": extract_block("C\+\+ Brute Force", "cpp"),
        "cpp_opt": extract_block("C\+\+ Optimal", "cpp"),
        "java_brute": extract_block("Java Brute Force", "java"),
        "java_opt": extract_block("Java Optimal", "java")
    }
