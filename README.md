# Task 1 – EDA & Visualization

## Objective
Use Pandas and Matplotlib to clean a raw dataset and generate insightful charts for Exploratory Data Analysis (EDA).

## Tools
- Python
- Pandas
- Matplotlib
- Seaborn

## Project structure

```text
Task_1_EDA_Visualization/
├── data/
│   └── sample_dataset.csv
├── outputs/
├── eda.py
├── requirements.txt
└── README.md
```

## Important: Kaggle dataset requirement

The internship task asks for a raw dataset from Kaggle. The included CSV is only a **starter dataset** so that the project runs immediately.

For the final internship submission:
1. Download a suitable Kaggle CSV dataset.
2. Copy it into the `data` folder.
3. In `eda.py`, change `DATA_FILE` to the name of your Kaggle CSV.
4. If the column names differ, update the chart/grouping sections to match the new dataset.
5. Run the program again.
6. Submit the generated charts from `outputs/`.

A suitable beginner dataset is **Kaggle's Supermarket Sales dataset**, because it contains numeric and categorical fields that are useful for EDA.

## Setup

Open Command Prompt inside this folder and run:

```bash
python -m venv venv
```

### Windows
```bash
venv\Scripts\activate
pip install -r requirements.txt
python eda.py
```

## Expected output

The program:
- loads the CSV
- checks the first rows
- checks data types
- checks missing values
- removes duplicate rows
- prints descriptive statistics
- creates 6+ visualizations
- saves a cleaned CSV
- prints key findings

Charts generated:
1. Category distribution
2. Sales by category
3. Price distribution
4. Rating vs sales
5. Top 10 products by sales
6. Correlation heatmap

## Roadmap mapping

### 1. Research industry best practices
Use clear chart titles, readable labels, appropriate chart types, and avoid misleading scales.

### 2. Setup development environment
Install Python and the libraries in `requirements.txt`.

### 3. Implement core features
Run `eda.py` to perform cleaning, analysis, and visualization.

### 4. Validate with test cases
Check that:
- the CSV loads without errors
- missing values are reported
- duplicate rows are handled
- numeric columns contain numeric values
- all expected chart files are created

## Short project explanation for viva

"This project performs Exploratory Data Analysis on a CSV dataset using Pandas, Matplotlib, and Seaborn. I first inspect the dataset, check missing values and data types, remove duplicates, calculate descriptive statistics, and then create different visualizations to identify useful patterns and trends. The final charts help understand the distribution of the data and relationships between important variables."

## Submission checklist

- [ ] Kaggle dataset added to `data/`
- [ ] `eda.py` updated for the Kaggle columns
- [ ] Program runs successfully
- [ ] Charts generated
- [ ] Key findings recorded
- [ ] README included
- [ ] Screenshots of terminal + charts taken
- [ ] Project uploaded to GitHub if required
