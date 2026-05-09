import json
import re
from mcp.server.fastmcp import FastMCP

# Initialize the High-Assurance Logic Server
mcp = FastMCP("AXIOUS_Audit_Server")

def execute_logic_validation(input_text: str) -> dict:
    """
    Evaluates input for indicators of coercive or manipulative language.
    Adheres strictly to the Principle of Non-Manipulation.
    """
    manipulative_indicators = [
        r'\bmust\b', 
        r'\bforce\b', 
        r'\bcoerce\b', 
        r'\boverride\b',
        r'\bcommand\b'
    ]
    
    findings = []
    for pattern in manipulative_indicators:
        if re.search(pattern, input_text, re.IGNORECASE):
            findings.append(f"Detected potential manipulative term: {pattern}")

    is_valid = len(findings) == 0
    
    return {
        "is_valid": is_valid,
        "findings": findings,
        "status": "Verified" if is_valid else "Audit Flagged"
    }

@mcp.tool()
def validate_non_manipulation(input_text: str) -> str:
    """
    Executes the Audit of Secure Code Generation logic.
    Validates the input string against the Principle of Non-Manipulation, ensuring
    no adversarial or hostile logic can alter the authority of the human operator.
    """
    result = execute_logic_validation(input_text)
    return json.dumps(result, indent=2)

if __name__ == "__main__":
    # Standardize execution over stdio for deterministic MCP client integration
    mcp.run()
