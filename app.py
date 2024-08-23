import streamlit as st
import pandas as pd
from datetime import datetime
import requests
import io

# Set page config
st.set_page_config(page_title="GitHub Repository Search", page_icon="🔍", layout="wide")

# Custom CSS for full-width layout and button alignment
st.markdown("""
    <style>
    .block-container {
        max-width: 100%;
        padding-top: 1rem;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 0rem;
    }
    .stButton > button {
        width: 100%;
        height: 2.75rem;
    }
    .stDownloadButton > button {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# GitHub API setup
search_url = "https://api.github.com/search/repositories"
headers = {
    "Accept": "application/vnd.github.v3+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

def fetch_github_repos(query, page=1, per_page=30, sort_option="stars"):
    params = {
        "q": query,
        "sort": sort_option,
        "order": "desc",
        "page": page,
        "per_page": per_page
    }
    response = requests.get(search_url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error: {response.status_code}\n{response.json()}")
        return None

def results_to_dataframe(results):
    items = results.get("items", [])
    data = []
    for item in items:
        data.append({
            "Repository": item["full_name"],
            "Description": item["description"],
            "URL": item["html_url"],
            "Stars": item["stargazers_count"],
            "Forks": item["forks_count"],
            "Created At": item["created_at"],
            "Last Updated": item["updated_at"]
        })
    return pd.DataFrame(data)

# Title and instructions
st.title("GitHub Repository Search 🔍")
st.markdown("""
    ### Instructions
    1. Enter a search query in the input field below.
    2. Adjust the search options if needed.
    3. Click the 'Search' button to fetch and display the results.
    4. Use the download buttons to save the results as CSV or Excel files.
""")

# Search input and button
col1, col2 = st.columns([5, 1])
with col1:
    search_query = st.text_input("Enter search query:", "python", label_visibility="collapsed")
with col2:
    search_button = st.button("🔍 Search", use_container_width=True)

# Search options
col1, col2, col3 = st.columns([2, 2, 1])
with col1:
    sort_option = st.selectbox("Sort by", ["Stars", "Forks", "Updated"])
with col2:
    per_page = st.slider("Results per page", 10, 100, 30)
with col3:
    auto_search = st.checkbox("Auto-search", value=True)

# Search functionality
if search_button or (auto_search and search_query):
    with st.spinner("Fetching results..."):
        results = fetch_github_repos(search_query, per_page=per_page, sort_option=sort_option.lower())
        if results:
            df = results_to_dataframe(results)
            
            # Display results
            st.subheader(f"Search Results for '{search_query}'")
            st.dataframe(
                df.style.format({
                    "Stars": "{:,}",
                    "Forks": "{:,}",
                    "Created At": lambda x: pd.to_datetime(x).strftime("%Y-%m-%d"),
                    "Last Updated": lambda x: pd.to_datetime(x).strftime("%Y-%m-%d")
                }),
                hide_index=True,
                column_config={
                    "URL": st.column_config.LinkColumn("URL"),
                    "Stars": st.column_config.NumberColumn("Stars", format="{:,}"),
                    "Forks": st.column_config.NumberColumn("Forks", format="{:,}"),
                    "Created At": st.column_config.DateColumn("Created At"),
                    "Last Updated": st.column_config.DateColumn("Last Updated"),
                },
                height=400,
                use_container_width=True
            )
            
            # Download options
            col1, col2 = st.columns(2)
            with col1:
                csv = df.to_csv(index=False)
                st.download_button(
                    label="📥 Download as CSV",
                    data=csv,
                    file_name=f"github_search_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )
            with col2:
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                    df.to_excel(writer, index=False, sheet_name='Sheet1')
                excel_data = buffer.getvalue()
                st.download_button(
                    label="📥 Download as Excel",
                    data=excel_data,
                    file_name=f"github_search_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
        else:
            st.warning("No results found. Try a different search query.")

# Footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit")
