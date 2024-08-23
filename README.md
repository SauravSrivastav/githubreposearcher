
 # GitHub Repo Searcher

GitHub Repo Searcher is a Streamlit web application that allows users to search for GitHub repositories based on a query and view the results in a tabular format. Users can also download the results in CSV or Excel format.

## Features

- Search GitHub repositories by query.
- Display results in a tabular format.
- Download results as CSV or Excel files.

## Setup

### Prerequisites

- Python 3.7 or higher
- Virtualenv (optional but recommended)

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/github_repo_searcher.git
   cd github_repo_searcher
   ```

2. **Create a virtual environment**:
   ```sh
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the Streamlit app**:
   ```sh
   streamlit run app.py
   ```

2. **Open the app in your browser**:
   - The app will be available at `http://localhost:8501`.

## Usage

1. Enter a search query in the input field.
2. Click the "Search" button to fetch and display the results.
3. Use the download buttons to save the results as CSV or Excel files.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
