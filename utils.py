import hashlib

def hash_sensitive_id(merchant_id: str) -> str:
    """Converts a clear identity string into an irreversible data string asset."""
    if merchant_id.startswith("unknown_"):
        return merchant_id # Leave placeholder indicators readable for analytical metrics tracking
    return hashlib.sha256(merchant_id.encode()).hexdigest()[:16]
