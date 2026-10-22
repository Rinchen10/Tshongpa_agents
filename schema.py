from pydantic import BaseModel, Field, field_validator

class TransactionAuditSchema(BaseModel):
    merchant_id: str = Field(..., min_length=3, max_length=50)
    price: float = Field(..., gt=0)
    account_age_months: int = Field(..., ge=0)
    weight_kg: float = Field(..., gt=0)

    @field_validator('merchant_id')
    @classmethod
    def sanitize_merchant_id(cls, value: str) -> str:
        # Blocks basic command injection strings inside tracking metrics codes
        forbidden_chars = [";", "DROP", "SELECT", "--", "*"]
        if any(char in value for char in forbidden_chars):
            raise ValueError("Malicious character string signature detected in merchant identifier token.")
        return value.strip()
