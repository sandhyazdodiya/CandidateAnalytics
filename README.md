# CandidateAnalytics Using Pandas

CandidateAnalytics is a Python-based data analysis project that uses **Pandas** to analyze job candidate information. It helps explore candidate profiles, technical skills, work experience, expected salaries, locations, and recruitment statuses using CSV data.

## Features

- Load candidate records from CSV files using Pandas.
- Analyze candidates by job role.
- Filter candidates based on experience.
- Calculate average expected salaries for different job roles.
- Count candidates by application status.
- Explore candidate skills, education, and locations.
- Export filtered candidate data to CSV files.

## Dataset

The project uses a sample dataset named `talentscope_candidates_5000.csv`.

The dataset contains **5,000 synthetic candidate records** and the following columns:

**Note:** The dataset contains synthetic sample data for educational purposes and does not represent real job applicants.

## Technologies Used

- Python
- Pandas
- CSV

## Project Structure

```text
CandidateAnalytics/
├── talentscope_candidates_5000.csv
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd TalentScope
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Linux or macOS:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file yet, install Pandas directly:

```bash
pip install pandas
```
