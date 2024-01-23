# Financial Model Evaluation

This project uses Flask to create a web application that evaluates financial data based on predefined rules. It includes the following files:

1. **app.py**: Flask application to handle file uploads and display evaluation results.

2. **rules.py**: Contains rules for evaluating financial data.

3. **model.py**: Defines a financial model that applies rules to evaluate data.

4. **data.json**: Sample JSON file containing financial data for evaluation.

## Setup and Run

1. Install required packages:
    ```bash
    pip install Flask
    ```

2. Run the Flask application:
    ```bash
    python app.py
    ```

3. Access the application at `http://127.0.0.1:5000/` in your web browser.

## File Descriptions

- **app.py**: Main Flask application file responsible for handling web requests, file uploads, and displaying results.

- **rules.py**: Defines financial rules and related functions for data evaluation.

- **model.py**: Implements a financial model using rules from `rules.py` to evaluate financial data.

- **data.json**: Sample JSON file containing financial data for testing the model.

## How to Use

1. Navigate to the application at `http://127.0.0.1:5000/`.

2. Upload a JSON file (e.g., `data.json`) using the provided form.

3. Click the "Submit" button to process the data.

4. View the evaluation results on the results page.

## Results Page

The results page will display the outcome of various rules applied to the uploaded financial data. Each rule is presented with its corresponding rule number and result.

## Acknowledgments

This project is a part of a financial evaluation challenge and follows a Flask-based web application architecture.

Feel free to modify and extend the project based on your needs.
