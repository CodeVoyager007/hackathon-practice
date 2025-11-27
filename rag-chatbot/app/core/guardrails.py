import re

class InputGuardrail:
    """
    A simple guardrail to check for malicious inputs.
    """
    def __init__(self):
        # Simple regex to detect potential SQL injection or script tags
        self.malicious_patterns = [
            re.compile(r"(\b(SELECT|INSERT|UPDATE|DELETE|DROP|TRUNCATE)\b)", re.IGNORECASE),
            re.compile(r"<script.*?>", re.IGNORECASE)
        ]

    def check(self, prompt: str) -> bool:
        """
        Checks if the prompt contains any malicious patterns.
        Returns True if the prompt is safe, False otherwise.
        """
        for pattern in self.malicious_patterns:
            if pattern.search(prompt):
                print(f"Warning: Detected potentially malicious pattern in prompt: {pattern.pattern}")
                return False
        return True

class OutputGuardrail:
    """
    A simple guardrail to check for safety and add citations to the output.
    """
    def check(self, answer: str) -> str:
        """
        Checks the answer for safety and formats it.
        For now, it's a simple pass-through, but can be extended.
        """
        # In a real application, you might check for harmful content, PII, etc.
        return answer

    def add_citations(self, answer: str, sources: list[str]) -> str:
        """
        Adds citation information to the answer.
        """
        if sources:
            return f"{answer}\n\n*Sources: {', '.join(sources)}*"
        return answer
