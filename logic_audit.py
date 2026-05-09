import json
import re

def validate_non_manipulation(input_text):
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

def main():
    sample_data = "The system must override human authority."
    result = validate_non_manipulation(sample_data)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
