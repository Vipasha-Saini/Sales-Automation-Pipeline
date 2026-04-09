# Sales Automation Pipeline

## Overview
This project automates the complete data pipeline:
- Fetch data from SQL database
- Data cleaning & transformation using pandas
- KPI generation
- Chart creation using matplotlib
- Excel report generation
- Automated email delivery

---

## Tech Stack
- Python
- Pandas
- SQLAlchemy
- Matplotlib
- SMTP (Email Automation)

---

## Project Structure
sales-automation-pipeline/
│── run_pipeline.py
│── sales.db
│── requirements.txt
│── README.md
│── .gitignore

---

## Setup

1. Clone repository

2. Install dependencies:
pip install -r requirements.txt

3. Create a `.env` file in project root:
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
EMAIL_RECEIVER=receiver_email@gmail.com

4. Run Project:
python run_pipeline.py


---

## Workflow
1. Connects to SQLite database
2. Fetches sales data
3. Cleans and transforms data
4. Generates KPIs
5. Creates charts
6. Exports Excel report
7. Sends report via email

---

## Output
- Excel report with KPIs
- Region-wise sales chart
- Monthly sales trend chart
- Automated email with report attachment

---

## Security
- Uses environment variables for email credentials
- `.env` file is not uploaded to GitHub

---

## Future Improvements
- Add logging
- Add scheduling (cron jobs)
- Integrate cloud database
