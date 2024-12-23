# 📧 Cold Email Generator

A **Cold Email Generator** powered by **LangChain**, **Llama 3**, and **ChromaDB** to craft personalized, targeted job application emails. The application takes a job posting URL, scrapes the page for relevant skills and details, and matches them against your stored project portfolio to generate a compelling email.

---

## 🚀 Features

- **Job Posting Scraper**: Extracts job-related skills and details from a given URL.
- **Skill Matching**: Compares job requirements with your portfolio of projects stored in **ChromaDB**.
- **Email Generation**: Uses **LangChain** and the **Llama 3 model** to write tailored cold emails that highlight your relevant projects and explain why you're a perfect fit for the role.
- **Streamlit App**: Interactive and user-friendly interface to input job URLs and generate emails effortlessly.

---

## 🛠️ Tech Stack

- **Python**: Core programming language for development.
- **Streamlit**: Provides the app’s interactive web interface.
- **LangChain**: Powers the email generation workflow.
- **Llama 3**: AI model for generating high-quality email content.
- **ChromaDB**: Vector database for storing and querying your project portfolio.

---

## 📋 Prerequisites

1. **Projects CSV File**:  
   - The application requires a CSV file containing your project portfolio with the following columns:  
     - `Project Name`: Name of your project.  
     - `Skills`: Skills/technologies used in the project.  
     - `Description`: A brief description of the project.
   - **Note**: This file is not included in the repository. You'll need to create your own CSV file to use this tool.

2. **GROQ API Key**:  
   - Obtain your **GROQ API key** and save it in a `.env` file or set it as an environment variable.
