from datetime import datetime, timezone
from typing import Dict
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pytz
from pydantic import BaseModel, EmailStr

app = FastAPI(
    title="Basic Info API - HNG Stage 0",
    description="An API that provides basic developer information",
    version="1.0.0"
)

# Configure CORS middleware to handle cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["GET"],  # Only allow GET requests
    allow_headers=["*"],
)


class InfoResponse(BaseModel):
    """
    Defines the structure of the API response 
    to type safety and automatic validation.
    """
    email: EmailStr
    current_datetime: str
    github_url: str


@app.get("/get-info", response_model=InfoResponse)
async def get_info() -> Dict[str, str]:
    """
    Handles GET requests to the root endpoint to retrieve 
    JSON object containing email, current datetime, and GitHub URL.
    
    Returns:
        dict: A dictionary containing the required information
    
    Raises:
        HTTPException: If there's an error generating the datetime
    """
    try:
        # Get current UTC time and format it according to ISO 8601
        current_time = datetime.now(pytz.UTC).astimezone(pytz.timezone('Africa/Lagos')).isoformat()
        
        return {
            "email": "franksuccess95@gmail.com",  
            "current_datetime": current_time, # datetime.now(timezone.utc).isoformat()
            "github_url": "https://github.com/froschi95/basic_info_apu"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Error generating response"
        )

# health check endpoint for monitoring
@app.get("/")
async def health_check() -> Dict[str, str]:
    """
    Simple health check endpoint to verify API is running.
    
    Returns:
        dict: Status message indicating the API is operational
    """
    return {"status": "healthy"}


# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)