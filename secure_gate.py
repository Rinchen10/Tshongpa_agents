def check_prompt_injection(user_input_text: str) -> bool:
    """Evaluates raw data logs text for behavioral override attempts."""
    malicious_keywords = ["ignore previous", "override system", "system directive", "developer override"]
    text_lower = user_input_text.lower()
    
    if any(keyword in text_lower for keyword in malicious_keywords):
        return True # Threat detected
    return False # Clear to pass
