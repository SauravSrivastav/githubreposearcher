---

# GitHub Repo Searcher 🔍

## Description

Welcome to **GitHub Repo Searcher**! 🚀 This is a Streamlit web application designed to help you search for GitHub repositories based on a query and view the results in a tabular format. You can also download the results in CSV or Excel format for further analysis.

## Features

- **Search GitHub Repositories**: Enter a search query to find relevant repositories.
- **Display Results**: View the search results in a tabular format with details such as repository name, description, URL, stars, forks, creation date, and last update date.
- **Download Results**: Export the search results as CSV or Excel files.
- **Customizable Search Options**: Sort results by stars, forks, or update date, and adjust the number of results per page.

## Setup

### Prerequisites

- Python 3.7 or higher
- Virtualenv (optional but recommended)

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/SauravSrivastav/githubreposearcher.git
   cd githubreposearcher
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

1. **Enter a search query** in the input field.
2. **Adjust the search options** if needed (sort by stars, forks, or update date, and set the number of results per page).
3. **Click the "Search" button** to fetch and display the results.
4. **Use the download buttons** to save the results as CSV or Excel files.

## Screenshots

![Search Results](https://github.com/SauravSrivastav/githubreposearcher/blob/main/data/1.png)
*Search results displayed in a tabular format.*

![Download Options](https://github.com/SauravSrivastav/githubreposearcher/blob/main/data/2.png)
*Download options for CSV and Excel files.*

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit issues and enhancement requests.

## Acknowledgments

- Thanks to the Streamlit community for providing an excellent framework for building web applications.
- Thanks to the GitHub API for providing access to repository data.

## Contact

For any questions or suggestions, please feel free to reach out to me at [sauravsrivastav2205@gmail.com](mailto:sauravsrivastav2205@gmail.com).

---
