from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="SAP Portfolio Demo")

@app.get("/")
def root():
    return {"status": "ok", "message": "SAP demo API is running"}
    from pydantic import BaseModel, Field

# Client data model
class ClientData(BaseModel):
    client_id: int = Field(..., example=123)
    name: str = Field(..., example="Rote Kiwi")
    balance: float = Field(..., example=1000.50)

# Endpoint to validate client
@app.post("/validate-client")
def validate_client(data: ClientData):
    errors = []
    if data.balance < 0:
        errors.append("Balance cannot be negative.")
    if not data.name.strip():
        errors.append("Name cannot be empty.")

    if errors:
        return {"status": "error", "errors": errors}
    return {"status": "ok", "message": f"Client {data.name} (ID: {data.client_id}) is valid."}