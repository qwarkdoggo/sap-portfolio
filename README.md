# SAP Portfolio Demo API

**Description:** A minimal FastAPI project demonstrating API development skills, suitable for a portfolio.

## Project Structure
- `app/main.py` — main FastAPI code
- `requirements.txt` — Python dependencies
- `Dockerfile` — file for containerization (optional)
- `app.zip` — archive of the project

Local Setup

1. Create a virtual environment:
```powershell
python -m venv .venv

Activate the environment:

.venv\Scripts\activate


2. Install dependencies:

pip install -r requirements.txt


3. Run the server:

uvicorn app.main:app --reload

4. Example Request
curl http://127.0.0.1:8000/


Response:

{
  "status": "ok",
  "message": "SAP demo API is running"
}

5. Example Pydantic Endpoint

You can also test POST requests with a simple Pydantic model:

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float


6. Example POST endpoint in app/main.py:

@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}

7. Docker (Optional)
docker build -t sap-api .
docker run -p 8000:8000 sap-api

## About Azure Deployment

I attempted to deploy this project to Azure Container Apps directly from source code without Docker.

Why it didn’t work:

The current Azure CLI version and Container Apps extension do not support --runtime python or --source . for direct Python deployments.

My system is running 32-bit Python on Windows 10, which is incompatible with Azure’s cloud build requirements for Container Apps.

Creating a local Docker image and pushing to Azure Container Registry is blocked because Docker is not installed on my machine.

Result:
The project works locally and can be deployed to any environment that supports Python and FastAPI. 
