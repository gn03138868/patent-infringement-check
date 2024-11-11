# patent-infringement-check
This repository contains a patent infringement check system that uses a transformer-based model to check potential patent infringements by analysing the semantic similarity between product descriptions and patent claims.

_____________________

Table of Contents
1. Features
2. Requirements
3. Installation
4. Running the System
5. API Usage
6. File Structure
7. Testing
8. Notes
_____________________


1. Features
-Uses a transformer model to compute semantic similarity between patent claims and product descriptions.
-Provides an API endpoint to perform infringement checks based on patent IDs and company names.
-Simple React frontend for user-friendly input and result visualisation.


2. Requirements
-Python 3.9+
-Node.js 18+
-Docker (for containerization, optional)

Python Libraries:
-Flask==2.3.2
-sentence-transformers==2.2.2
-torch==1.12.1

JavaScript Libraries:
-React 18


3. Installation
3.1. Clone the repository:

''''bash
git clone https://github.com/gn03138868/patent-infringement-check.git

cd patent-infringement-check

''''

3.2. Backend Setup:

-Navigate to the backend directory:

''''bash

cd backend

''''

-Create a virtual environment and install dependencies:

''''bash

python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
pip install -r requirements.txt

''''

3.3. Frontend Setup:

-Navigate to the frontend directory:

''''bash

cd ../frontend

''''

-Install dependencies:

''''bash

npm install

''''


4. Running the System
There are two ways to run the system: directly or with Docker.

Option 1: Running Directly
-Start the Backend Server:

''''bash

cd backend
python app.py

''''

# The server will start at http://localhost:5000.

-Start the Frontend Server:

''''bash

cd ../frontend
npm start

''''

# The frontend will start at http://localhost:3000.


Option 2: Running with Docker
-Build and Run Docker Containers:

''''bash

docker-compose up --build

''''

# This will set up both the backend (on port 5000) and the frontend (on port 3000).


5. API Usage
The backend provides a single API endpoint for checking patent infringement.

-Endpoint: POST /check_infringement

-Request Body:

''''json

{
  "patent_id": "US-RE49889-E1",
  "company_name": "Walmart Inc."
}

''''

-Response:
--Returns a JSON object containing a list of potentially infringing products and relevant claims if infringement is detected.

Example of a response:

''''json

{
  "analysis_id": "1",
  "patent_id": "US-RE49889-E1",
  "company_name": "Walmart Inc.",
  "analysis_date": "2024-10-31",
  "top_infringing_products": [
    {
      "product_name": "Smart Inventory Manager",
      "infringement_likelihood": "High",
      "relevant_claims": [1, 3],
      "explanation": "Claim 1 has a similarity score of 0.75. Claim 3 has a similarity score of 0.80."
    }
  ]
}

''''


6. File Structure

patent-infringement-check/
│
├── backend/
│   ├── app.py                # Main Flask API file
│   ├── infringe_check.py      # Core logic for infringement checking
│   ├── patents.json           # Sample patent data
│   ├── company_products.json  # Sample company products data
│   ├── requirements.txt       # Backend dependencies
│   └── tests/
│       └── test_infringe_check.py  # Unit tests
│
├── frontend/
│   ├── src/
│   │   ├── App.js             # Main React component
│   │   └── index.js           # React entry point
│   ├── Dockerfile             # Docker configuration for frontend
│   └── package.json           # Frontend dependencies
│
├── docker-compose.yml         # Docker Compose file to run both backend and frontend
└── README.md                  # Project documentation


7. Testing
To run the backend tests:

-Navigate to the backend directory:

''''bash

cd backend

''''

-Run tests:

''''bash

python -m unittest discover tests

''''

The test results will indicate whether the core infringement check functionality is working as expected.


8. Notes
The model (sentence-transformers/all-MiniLM-L6-v2) used for semantic similarity checks can be replaced with a different model if required. Just update the model name in infringe_check.py.

Modify the threshold parameter in check_infringement to adjust the sensitivity of the infringement detection.


