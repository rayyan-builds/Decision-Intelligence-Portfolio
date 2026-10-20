<div align="center">

<img src="project_banner.svg" width="100%" alt="Bookstore Intelligence - Web Scraping, Retail Analytics, Data-Driven Decisions"/>

<br/>

<img src="https://readme-typing-svg.demolab.com/?lines=What+can+1%2C000+book+listings+reveal%3F;Web+Scraping+%7C+Pandas+%7C+Optimisation;From+HTML+to+Data-Driven+Decisions;Pricing+%7C+Ratings+%7C+Availability&font=Fira%20Code&center=true&width=700&height=45&color=4FB3BF&vCenter=true&size=22" alt="Typing animation"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4B8BBE?style=for-the-badge)](https://www.crummy.com/software/BeautifulSoup/)
[![Requests](https://img.shields.io/badge/Requests-2C5364?style=for-the-badge)](https://requests.readthedocs.io/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)](https://matplotlib.org/)
[![CSV](https://img.shields.io/badge/CSV-Data%20Analysis-203A43?style=for-the-badge)](#-repository-structure)

</div>

---

## 📖 Introduction

> **What can 1,000 book listings reveal about pricing, ratings, and purchasing decisions?**

This project converts an online book catalogue into structured datasets and applies Python-based analysis, visualisation, and optimisation to it. Starting from raw HTML on [Books to Scrape](https://books.toscrape.com/), it builds a small competitive-intelligence workflow for a hypothetical bookstore: scrape the catalogue, structure it with Pandas, analyse prices and ratings, and use dynamic programming to choose the best books for a fixed budget.

---

## 📊 Results Dashboard

<div align="center">

| 📚 Main Dataset | 🗄️ Full Catalogue | 📄 Pages Scraped | ⭐ Five-Star Books |
|:---:|:---:|:---:|:---:|
| **60** books | **1,000** books | **50** pages | **14** of 60 |

| 🧮 Books Selected | 💷 Total Cost | 🏆 Rating Score | 💰 Budget Left |
|:---:|:---:|:---:|:---:|
| **6** books | **£96.59** | **26** stars | **£3.41** of £100 |

</div>

> ⚠️ **Note:** Books to Scrape assigns ratings at random. These figures are results of an analytical exercise, not evidence of real customer sentiment.

---

## 🧭 Project Overview

```text
Inspect HTML  →  Extract Data  →  Scrape Pages  →  Structure with Pandas
        →  Analyse Prices & Ratings  →  Solve Budget Problem  →  Visualise Ratings
```

| Step | What happens |
|:---:|---|
| **1** | Inspect the website's HTML to find the right selectors |
| **2** | Extract book information (title, price, rating, availability) |
| **3** | Collect records across catalogue pages |
| **4** | Structure the data into Pandas DataFrames |
| **5** | Analyse prices, ratings, and availability |
| **6** | Solve the budget-constrained selection problem |
| **7** | Visualise the full-catalogue rating distribution |

---

## 📈 Data Visualisation

<div align="center">

![Distribution of Book Ratings](book_rating_distribution%20(1).png)

*Distribution of star ratings across the 1,000-book full catalogue.*

| Rating | ⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Books** | 226 | 196 | 203 | 179 | 196 |

</div>

**Interpretation:** the scraped catalogue is spread fairly evenly across the five rating categories, with no single rating dominating. This describes the practice dataset only, and the ratings should not be read as genuine customer satisfaction or market demand.

---

## ✨ Key Features

| Feature | Practical purpose |
|---|---|
| 🔍 **HTML inspection & selector identification** | Locates the exact elements that hold each data field |
| 🌐 **Multi-page web scraping** | Collects records across the catalogue rather than a single page |
| 🗂️ **Structured data extraction** | Turns unstructured web content into tabular records |
| 💾 **CSV export** | Saves datasets for reuse and reproducibility |
| 💷 **Price & rating analysis** | Summarises the catalogue with descriptive statistics |
| ⭐ **Five-star filtering & price ranking** | Identifies the cheapest top-rated books |
| 📊 **Rating distribution analysis** | Counts books in each rating category |
| 📉 **Bar chart generation** | Presents the distribution visually with Matplotlib |
| 🧮 **£100 budget selection (dynamic programming)** | Maximises combined star rating within a budget |
| 🔗 **Full-catalogue scraping with product URLs** | Extends collection to 1,000 books with links back to each product |

---

## 🔎 Analytical Findings

Findings below are from the 60-book main dataset (`competitor_books.csv`).

| # | Question | Finding | Business relevance |
|:---:|---|---|---|
| 1 | Most expensive book? | *Slow States of Collapse: Poems* — **£57.31** | Sets the top of the price range |
| 2 | Cheapest book? | *In Her Wake* — **£12.84** | Sets the bottom of the price range |
| 3 | Average price? | **£35.00** | Baseline for price positioning |
| 4 | Five-star share? | **14 of 60** (≈ 23.3%) | Size of the top-rated segment |
| 5 | In-stock share? | **100%** of the dataset | No availability constraint in this sample |
| 6 | Top five by rating (lower price breaks ties)? | *Sophie's World*, *Thirst*, *Set Me Free*, *The Four Agreements: A Practical Guide to Personal Freedom*, *#HigherSelfie: Wake Up Your Life. Free Your Soul. Find Your Tribe.* | Shortlist of top-rated, lower-cost titles |
| 7 | Cheapest five-star book? | *Sophie's World* — **£15.94** | Lowest-cost entry among top-rated books |

---

## 💼 Business Recommendation

For a hypothetical competing bookstore, the five-star analysis supports a preliminary catalogue selection: the five cheapest five-star books in the main dataset.

<div align="center">

| Book | Price |
|---|---:|
| Sophie's World | £15.94 |
| Thirst | £17.27 |
| Set Me Free | £17.46 |
| The Four Agreements: A Practical Guide to Personal Freedom | £17.66 |
| #HigherSelfie: Wake Up Your Life. Free Your Soul. Find Your Tribe. | £23.11 |
| **Total** | **£91.44** |

</div>

This is a **preliminary price-based comparison, not a validated sales forecast**. The dataset contains no sales, customer-demand, or profit-margin data.

---

## 🎯 The £100 CEO Challenge

The task: choose books to **maximise the sum of star ratings without exceeding £100**. This is a classic **0/1 knapsack** problem, solved with **dynamic programming**, which evaluates affordable combinations systematically instead of relying on a greedy guess.

<div align="center">

| 🧮 Books Selected | 💷 Total Price | 🏆 Combined Rating | 💰 Budget Remaining |
|:---:|:---:|:---:|:---:|
| **6** | **£96.59** | **26** | **£3.41** |

</div>

It is a useful demonstration of constrained decision-making. The objective is rating-based only and does not account for real demand, margins, shipping, or customer preferences.

---

## 📁 Repository Structure

| File | Purpose |
|---|---|
| `Bookstore_Intelligence_Notebook.ipynb` | Main notebook containing scraping, analysis, and optimisation |
| `competitor_books.csv` | Original 60-record dataset |
| `competitor_books_bonus.csv` | Extended 1,000-record dataset with product URLs |
| `five_star_books_by_price.csv` | Five-star books from the main dataset, sorted by price |
| `rating_counts.csv` | Count of books in each rating category |
| `book_rating_distribution.png` | Rating-distribution bar chart |
| `project_banner.svg` | README banner graphic |
| `requirements.txt` | Python dependencies for reproducing the project |
| `README.md` | Project documentation |

---

## ⚙️ Installation & Usage

**1. Clone the portfolio repository**

```bash
git clone https://github.com/rayyan-builds/Decision-Intelligence-Portfolio.git
```

**2. Navigate to the project folder (Windows)**

```powershell
cd "Decision-Intelligence-Portfolio\01-Data Analytics\Bookstore-Intelligence-Web-Scraper"
```

**3. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**4. Launch Jupyter**

```bash
python -m notebook
```

Open `Bookstore_Intelligence_Notebook.ipynb` and run the cells in order. An internet connection is required for the web-scraping steps, and outputs may be regenerated when the notebook is rerun.

---

## 🧪 Limitations & Data Integrity

Being explicit about what the data can and cannot support is part of the analysis:

- **Books to Scrape is a practice website** built for learning web scraping.
- **Ratings are randomly assigned**, so they carry no real customer signal.
- **No sales or demand data** is available.
- **Price and availability** reflect the data collected at scraping time.
- **Website structure may change**, which would require updating the scraping code.
- **The budget optimisation** maximises a defined rating-based objective, not real-world commercial value.

---

## 🧠 Skills Demonstrated

![Python](https://img.shields.io/badge/Python-2C5364?style=flat-square)
![Web Scraping](https://img.shields.io/badge/Web%20Scraping-2C5364?style=flat-square)
![HTML Parsing](https://img.shields.io/badge/HTML%20Parsing-2C5364?style=flat-square)
![Pandas](https://img.shields.io/badge/Pandas-2C5364?style=flat-square)
![NumPy](https://img.shields.io/badge/NumPy-2C5364?style=flat-square)
![Data Structuring](https://img.shields.io/badge/Data%20Structuring-2C5364?style=flat-square)
![Exploratory Data Analysis](https://img.shields.io/badge/Exploratory%20Data%20Analysis-2C5364?style=flat-square)
![Data Visualisation](https://img.shields.io/badge/Data%20Visualisation-2C5364?style=flat-square)
![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-2C5364?style=flat-square)
![Optimisation](https://img.shields.io/badge/Optimisation-2C5364?style=flat-square)
![Business Decision-Making](https://img.shields.io/badge/Business%20Decision--Making-2C5364?style=flat-square)

---

<div align="center">

## 👤 Author

**Rayyan Asim**
BS Business Analytics — FAST-NUCES Islamabad

[![GitHub Portfolio](https://img.shields.io/badge/GitHub-Portfolio-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rayyan-builds/Decision-Intelligence-Portfolio)
[![This Project](https://img.shields.io/badge/This-Project-2C5364?style=for-the-badge&logo=jupyter&logoColor=white)](https://github.com/rayyan-builds/Decision-Intelligence-Portfolio/tree/main/01-Data%20Analytics/Bookstore-Intelligence-Web-Scraper)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rayyan%20Asim-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rayyan-asim-096877252)

<img src="https://readme-typing-svg.demolab.com/?lines=Turning+Data+Into+Decisions;Thanks+for+visiting&font=Fira%20Code&center=true&width=500&height=35&color=4FB3BF&vCenter=true&size=18" alt="Closing animation"/>

</div>
