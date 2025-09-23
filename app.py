import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import re

# Load dataset
df = pd.read_csv("metadata_sample_cleaned.csv")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research metadata interactively.")

# Sidebar filter
year_range = st.slider("Select Year Range", int(df['year'].min()), int(df['year'].max()), (2020, 2021))

# Filter dataset
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Publications per year
st.subheader("Publications per Year")
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
st.pyplot(fig)

# Top journals
st.subheader("Top Journals")
top_journals = filtered['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax)
st.pyplot(fig)

# Word cloud
st.subheader("Word Cloud of Titles")
text = " ".join(filtered['title'].dropna())
wc = WordCloud(width=800, height=400, background_color="white").generate(text)
fig, ax = plt.subplots()
ax.imshow(wc, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# Show data sample
st.subheader("Sample Data")
st.write(filtered.head(20))\

# Part 5: Documentation & Reflection in Streamlit
st.title("📄 Documentation and Reflection")
st.subheader(
    "Department Research & Data Analysis\n"
    "College of Business Education, Tanzania\n"
    "\n2025/09/23"
)

# --- Findings Summary ---
st.markdown("## Key Findings")

# Example 1: Publications per Year
papers_per_year = df['year'].value_counts().sort_index()
st.line_chart(papers_per_year)
st.write("✅ Research publications increased sharply in 2020 during the COVID-19 outbreak.")

# Example 2: Top Journals
top_journals = df['journal'].value_counts().head(5)
st.bar_chart(top_journals)
st.write("✅ Top publishing journals include:", ", ".join(top_journals.index))

# Example 3: Frequent Words in Titles
words = " ".join(df['title'].dropna().astype(str)).lower()
words = re.findall(r'\b\w+\b', words)
word_counts = Counter(words).most_common(10)
st.write("✅ Most frequent words in titles:")
st.table(word_counts)

# --- Reflection Section ---
st.markdown("## Reflection")
st.write("""
- **Challenges:** Any work face challenges, To work with Large dataset (over 1.6GB) having mixed and messy columns, requires careful cleaning for Appealing analysis.
- **Learning:** Generated skills in data cleaning, analysis with visualization, and building Streamlit apps, made me more proficient and confident in data science.
- **Outcome:** The ability of transforming raw metadata into clear insights, visualizations, and interactive reports are also very satisfying.
""")

# --- Closing Note ---
st.success(
    "Dr Bilal – Researcher & Data Analyst\n"
    "\n📧 bilalimustafa68@gmail.com\n"
    "\nHead of Department."
)