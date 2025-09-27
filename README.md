
# 📊 COVID-19 Research Metadata Analysis

**Author:** Dr Bilal ([GitHub](https://github.com/drBILAL-mj))
**Assignment:** CORD-19 Metadata Exploration & Visualization
**Deployed App:** [👉 Open Streamlit App Here](https://covid-19research.streamlit.app/)
**Source Code:** [GitHub Repository](https://github.com/drBILAL-mj/Frameworks_Assignment)

---

## 📌 Project Overview

This project explores the **CORD-19 metadata dataset**, focusing on trends in COVID-19 research publications. The workflow includes:

1. **Data Loading** – Import and preview the dataset
2. **Data Cleaning** – Handle missing values, fix mixed data across columns, and prepare the data
3. **Data Analysis & Visualization** – Explore yearly publication counts, top journals, frequent words in titles, and source distribution
4. **Streamlit Application** – Interactive dashboard for data exploration
5. **Documentation & Reflection** – Summarize findings and present researcher identity

---

## ⚙️ Tools & Libraries Used

- **Python 3.9+**
- **Pandas** – Data manipulation
- **Matplotlib / Seaborn** – Visualization
- **WordCloud** – Title word frequency visualization
- **Streamlit** – Interactive web application
- **Jupyter Notebook** – Development environment

---

## �️ Installation

1. **Clone the repository:**
	```powershell
	git clone https://github.com/drBILAL-mj/Frameworks_Assignment.git
	cd Frameworks_Assignment
	```
2. **Install requirements:**
	```powershell
	pip install -r requirements.txt
	```

---

## 🚀 Usage

### Run the Streamlit App Locally

```powershell
python -m streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

### Try the Deployed App

Access the live dashboard here: [https://covid-19research.streamlit.app/](https://covid-19research.streamlit.app/)

---

## 📊 Key Findings

### 1. Publications by Year
📈 Sharp spike in research output in **2020**, coinciding with the COVID-19 pandemic.
📌 Continued strong growth in subsequent years.

### 2. Top Journals
Journals such as **The Lancet, BMJ, Nature, and Science** were among the top publishers of COVID-19 research.

### 3. Frequent Words in Titles
Most common words included: **covid, sars, health, pandemic, coronavirus**.
These words reflect the focus of global research efforts.

### 4. Source Distribution
Publications came from a wide range of sources.
Due to dataset size, a representative sample was used for visualization.

---

## 💡 Reflection

**Challenges Faced:**
- ⚠️ The dataset was very large (~1.6GB), making it hard to process
- 🔄 Some columns had mixed data (authors in abstracts, dates in author fields)
- 🛠️ Cleaning required careful checking to align values with correct columns

**Learning Outcomes:**
- ✅ Gained experience in **data wrangling** (cleaning and reshaping large datasets)
- ✅ Practiced **basic NLP** techniques (word frequency analysis)
- ✅ Learned how to build and deploy an **interactive Streamlit app**
- ✅ Improved workflow for presenting data insights in a research-oriented format

---

## 📂 File Structure

```
Frameworks_Assignment/
├── analysis.ipynb                # Jupyter notebook for exploration
├── app.py                        # Streamlit dashboard code
├── metadata.csv                  # Original metadata
├── metadata_sample.csv           # Sampled metadata
├── metadata_sample_cleaned.csv   # Cleaned sample metadata
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 📬 Contact

For questions, feedback, or collaboration:
- **Dr Bilal** – [GitHub](https://github.com/drBILAL-mj) | [Email](mailto:bilalimustafa68@gmail.com)

---

## 🌐 References

- [CORD-19 Dataset](https://www.kaggle.com/datasets/allen-institute-for-ai/CORD-19-research-challenge)
- [Streamlit Documentation](https://docs.streamlit.io/)


