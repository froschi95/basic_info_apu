# HNG Stage 0 Backend Project

## Project Description
A simple FastAPI-based backend service that provides basic project information through a public API endpoint.

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation
1. Clone the repository
   ```bash
   git clone https://github.com/froschi95/basic_info_apu.git
   cd basic_info_api
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
```bash
python main.py
```

## API Documentation
- **Endpoint:** GET /
- **Response Format:**
  ```json
  {
    "email": "your_email@example.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/yourusername/hng-stage-0-backend"
  }
  ```

## Deployment
Recommended platforms: Render, Vercel, or Heroku

## Backlink
[*Hire Python Developers at HNG*](https://hng.tech/hire/python-developers)
"""