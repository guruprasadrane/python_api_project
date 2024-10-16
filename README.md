# API Monitor

This project provides a web interface for monitoring and validating various API endpoints.

## Features

- Ping URLs to check their status and response time
- Validate functionality of specific applications
- Optional proxy support for all requests

## Usage

1. Run the Flask application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. To ping a URL:
   - Enter the URL in the "URL" input field
   - (Optional) Check the "Use Proxy" checkbox and enter a proxy URL if needed
   - Click the "Ping" button

4. To validate an application:
   - Enter the application name in the "App Name" input field
   - Click the "Validate" button

## Adding New Application Validations

To add a new application validation:

1. Open `monitor.py`
2. Add a new validation function for your application
3. Add the new function to the `validation_functions` dictionary in the `validate_functionality` function

Example:

## Setup

1. Ensure you have Python 3.x installed on your system.

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up the CA bundle:
   - Locate your CA bundle file (usually a .pem file)
   - Update the `REQUESTS_CA_BUNDLE` path in `app.py` to point to your CA bundle file:
     ```python
     os.environ['REQUESTS_CA_BUNDLE'] = '/path/to/your/ca-bundle.pem'
     ```

4. Run the Flask application:
   ```
   python app.py
   ```

## Technologies Used
- Python 3.x
- Flask 2.3.2
- Requests 2.31.0
- HTML/CSS
- JavaScript (with Axios for AJAX requests)

## Project Structure
```
api_project/
├── app.py
├── monitor.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```
