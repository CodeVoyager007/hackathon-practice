import pytest
from app.core.guardrails import InputGuardrail, OutputGuardrail

def test_input_guardrail_safe_prompt():
    """
    Tests that a safe prompt passes the input guardrail check.
    """
    guardrail = InputGuardrail()
    assert guardrail.check("What is AI?") == True

def test_input_guardrail_malicious_prompt_sql():
    """
    Tests that a prompt with SQL injection is blocked.
    """
    guardrail = InputGuardrail()
    assert guardrail.check("What is AI?; DROP TABLE users;--") == False

def test_input_guardrail_malicious_prompt_script():
    """
    Tests that a prompt with a script tag is blocked.
    """
    guardrail = InputGuardrail()
    assert guardrail.check("<script>alert('XSS')</script>") == False

def test_output_guardrail_check():
    """
    Tests the output guardrail's check method.
    """
    guardrail = OutputGuardrail()
    assert guardrail.check("This is a safe answer.") == "This is a safe answer."

def test_output_guardrail_add_citations():
    """
    Tests the output guardrail's citation adding method.
    """
    guardrail = OutputGuardrail()
    answer = "This is the answer."
    sources = ["Chapter 1", "Chapter 2"]
    cited_answer = guardrail.add_citations(answer, sources)
    assert "Sources: Chapter 1, Chapter 2" in cited_answer
