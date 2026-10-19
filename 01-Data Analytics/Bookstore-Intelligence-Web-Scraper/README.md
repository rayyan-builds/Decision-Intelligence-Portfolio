# Retail Catalogue Intelligence: Web Scraping, Pricing and Rating Analysis

## Project Overview

This project applies web scraping and data analysis techniques to collect and examine book catalogue data from [Books to Scrape](https://books.toscrape.com/). The objective is to transform publicly available product listings into a structured dataset that can support catalogue analysis, price comparisons, rating distribution analysis, and budget-based purchasing decisions.

Using Python, the project extracts book titles, prices, star ratings, availability information, and product URLs. The collected data is processed with Pandas and analysed to identify patterns that can support basic retail intelligence and decision-making.

## Objectives

* Automate the collection of book catalogue data from a website.
* Extract and structure product information for analysis.
* Implement multi-page scraping to collect records across the catalogue.
* Analyse book prices, star ratings, and product availability.
* Identify highly rated books and compare their prices.
* Develop a budget-constrained book selection strategy.
* Generate a visual summary of the catalogue's rating distribution.

## Tools and Technologies

| Tool          | Purpose                                             |
| ------------- | --------------------------------------------------- |
| Python        | Web scraping, data processing, and analysis         |
| Requests      | Sending HTTP requests to retrieve webpage content   |
| BeautifulSoup | Parsing HTML and extracting product information     |
| Pandas        | Structuring, cleaning, and analysing catalogue data |
| Matplotlib    | Visualising the distribution of book ratings        |
| CSV           | Storing datasets for further analysis               |
| PyCharm       | Python development environment                      |

## Data Collection

The project uses the Books to Scrape website, a practice website designed for web scraping exercises.

The scraping scripts collect the following attributes:

* **Book Title:** Name of the listed book.
* **Price:** Displayed price in pounds sterling (£).
* **Rating:** Website-provided rating, represented by one to five stars.
* **Availability:** Displayed stock availability information.
* **Product URL:** Link to the individual book listing, included in the extended dataset.

The project includes two datasets representing different collection scopes:

| Dataset                      | Coverage              | Records | Columns |
| ---------------------------- | --------------------- | ------: | ------: |
| `competitor_books.csv`       | Three catalogue pages |      60 |       4 |
| `competitor_books_bonus.csv` | Full catalogue        |   1,000 |       5 |

The original dataset supports the main assignment analysis, while the extended dataset demonstrates full-catalogue scraping and includes product URLs.

## Analysis and Business Intelligence

### 1. Catalogue Analysis

The collected data provides a basis for examining product prices, star ratings, and availability. These attributes can be used to compare listings and identify patterns within the catalogue.

### 2. Rating Distribution

The project calculates the number of books associated with each star-rating category. A bar chart provides a visual overview of the distribution.

**Output:** `rating_counts.csv` and `book_rating_distribution.png`

### 3. Five-Star Book Analysis

The project identifies five-star-rated books and organises them by price to support comparisons between highly rated products.

**Output:** `five_star_books_by_price.csv`

### 4. CEO Budget Challenge

The CEO challenge implements a budget-constrained book selection problem. A dynamic programming approach selects a combination of books within a fixed budget while maximising the combined rating score.

For the original 60-book dataset, the recorded selection contains six books costing **£96.59** in total, leaving **£3.41** from the £100 budget. The combined rating score is 26.

This result demonstrates how catalogue data can be used to support a simple resource-allocation decision.

### 5. Full-Catalogue Scraping

The bonus scraper follows the website's pagination to collect records across the catalogue. It saves the extended dataset separately so that the original assignment dataset remains available.

## Key Deliverables

* `Mission 2.py` — Initial scraping exercise.
* `Mission 3.py` — Multi-page scraping for the main dataset.
* `Mission 4.py` — Catalogue analysis and assignment questions.
* `ceo_challenge.py` — Budget-constrained book selection.
* `bonus_missions.py` — Extended scraping and bonus analysis.
* `competitor_books.csv` — Main 60-record dataset.
* `competitor_books_bonus.csv` — Extended 1,000-record dataset.
* `rating_counts.csv` — Count of books by rating.
* `five_star_books_by_price.csv` — Five-star books organised by price.
* `book_rating_distribution.png` — Visualisation of the rating distribution.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/rayyan-builds/Decision-Intelligence-Portfolio.git
```

Navigate to the project directory after placing the project files in the repository.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install requests beautifulsoup4 pandas matplotlib
```

### 4. Run the scripts

Run the required Python files individually from PyCharm or the terminal.

For example:

```bash
python "Mission 3.py"
```

To run the extended scraping exercise:

```bash
python bonus_missions.py
```

**Note:** Run the scripts from the project directory so that input and output file paths resolve correctly. Some analysis scripts depend on CSV files generated by the scraping scripts.

## Limitations

* Books to Scrape is a practice website, not a live commercial bookstore.
* The displayed ratings are intended for scraping practice and should not be treated as verified customer sentiment.
* Listed prices and availability reflect the website data retrieved during scraping.
* The budget challenge optimises the rating score available in the collected dataset; it does not account for real-world factors such as demand, profit margins, shipping costs, or customer preferences.
* Website structure changes may require updates to the scraping logic.

## Skills Demonstrated

Python programming, HTML parsing, web scraping, data collection, data structuring, Pandas data analysis, data visualisation, multi-page automation, algorithmic problem-solving, and data-driven decision-making.

## Project Context

This project was developed as a practical exercise in collecting, processing, and analysing online retail catalogue data. It demonstrates how raw website information can be converted into structured datasets and used to support basic business intelligence tasks.

---

**Author:** Rayyan Asim
**Portfolio:** [Decision Intelligence Portfolio](https://github.com/rayyan-builds/Decision-Intelligence-Portfolio)
