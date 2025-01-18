# web-greeting-app/web-greeting-app/README.md

# Web Greeting App

A simple web application that greets users based on their input using Flask.

## Project Structure

```
web-greeting-app
├── src
│   ├── app.py            # Main application file
│   ├── static
│   │   └── styles.css    # CSS styles for the web application
│   └── templates
│       └── index.html    # HTML template for the greeting interface
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd web-greeting-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/app.py
   ```

4. Open your web browser and navigate to `http://127.0.0.1:5000` to access the greeting application.

## Usage

- Enter a number between 1 and 4 to receive a personalized greeting.
- If an invalid number is entered, an error message will be displayed.

## License

This project is licensed under the MIT License.