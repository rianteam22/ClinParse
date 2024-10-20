
# Medical Information Extraction System

## Overview
This application processes medical forms in PDF format, extracts relevant text data, and converts it into a structured JSON format. The primary objective is to facilitate the extraction of key medical information, including patient identification, diagnoses, clinical parameters, and treatment outcomes. The extracted data is further transformed into JSON, and optionally into CSV, for easier analysis and integration with other systems.

## Table of Contents
1. [Architecture](#architecture)
2. [Installation](#installation)
3. [Usage](#usage)
4. [File Structure](#file-structure)
5. [Core Components](#core-components)
6. [Contributing](#contributing)
7. [License](#license)

## Architecture
The application uses a modular approach for efficient and maintainable code organization. Key modules include:
- **Text extraction:** Uses AI models to convert PDF content into plain text.
- **Data parsing:** Transforms plain text into structured JSON based on predefined schemas using Pydantic models.
- **Data storage:** Saves the extracted data into JSON and/or CSV formats for further analysis.

## Installation
Ensure you have Python 3.7 or higher installed. Then, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   - Create a `.env` file in the root directory.
   - Use the `sample.env` as a reference to set up required environment variables.

## Usage
The application is executed from the command line. To process PDF files, use the following command:

```bash
python src/main.py
```

### Input Structure
- Place your PDF files in the `scans/pdf` directory before running the script.

### Output Structure
- Extracted text files will be saved in the `scans/txt` directory.
- JSON files will be saved in the `scans/json` directory.
- Logs will be saved in the `logs` directory.

## File Structure
The application has the following directory structure:

```
.
├── logs/
├── scans/
│   ├── csv/
│   ├── json/
│   ├── pdf/
│   └── txt/
├── src/
│   ├── config.py
│   ├── main.py
│   ├── models.py
│   ├── process.py
│   └── utils.py
├── tests/
├── venv/
├── LICENSE
├── README.md
├── requirements.txt
```

### Key Directories
- **assets/**: Stores static assets (e.g., images, reference documents).
- **logs/**: Stores log files for debugging and monitoring.
- **scans/**: Contains input and output data directories.
  - **csv/**: Contains CSV files generated from JSON data.
  - **json/**: Contains JSON files generated from the extracted text.
  - **pdf/**: Contains PDF files to be processed.
  - **txt/**: Contains raw text extracted from PDFs.
- **src/**: Contains all source code files.
- **tests/**: Contains unit tests for the application.
- **venv/**: Virtual environment for Python dependencies.

## Core Components
### 1. `config.py`
Handles application configuration, including setting up logging and loading environment variables using the `dotenv` library.

### 2. `main.py`
The main entry point for the application. It manages the workflow, including loading configurations, processing PDFs, and saving results in JSON format.

### 3. `models.py`
Defines the data models using Pydantic. It includes schemas for patient information, general data, comorbidities, clinical parameters, and outcomes.

### 4. `process.py`
Handles the processing of medical information. It extracts text from PDFs, parses it into structured JSON, and uses predefined Pydantic models to ensure data integrity.

### 5. `utils.py`
Includes utility functions for text extraction, file operations, and data conversions (e.g., JSON to CSV). It also handles error logging and directory creation.

## Contributing
Contributions are welcome! To contribute:

1. **Fork the repository.**
2. **Create a new branch:**
   ```bash
   git checkout -b feature/my-feature
   ```
3. **Make your changes and commit:**
   ```bash
   git commit -am 'Add a new feature'
   ```
4. **Push to the branch:**
   ```bash
   git push origin feature/my-feature
   ```
5. **Submit a pull request.**

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
