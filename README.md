# 🚀 Selenium MultiScraper (Bundelkhand University Result Extractor)

## 📜 Overview
**Selenium MultiScraper** is a high-performance, multi-threaded web scraping tool designed to extract student result data from the **Bundelkhand University, Jhansi** examination portal. It automates the process of fetching student marks, saving time and effort.  

🔹 If you need to scrape data from a different university or website, update the **URL and XPath selectors** in the script accordingly.

## 🔥 Features
✅ **Fast Execution with Multithreading** – Runs multiple Selenium instances in parallel for efficiency.  
✅ **Automated Result Extraction** – Fetches student details, subject marks, and total scores.  
✅ **Headless Browsing** – Uses Chrome in headless mode for faster execution.  
✅ **Error Handling** – Skips invalid roll numbers and logs errors without stopping.  
✅ **Thread-Safe CSV Writing** – Ensures proper data storage without conflicts.  

## 🛠️ Technologies Used
- **Python** 🐍  
- **Selenium WebDriver** 🌐  
- **ThreadPoolExecutor (concurrent.futures)** ⚡  
- **CSV File Handling** 📄  

## 📌 Installation & Setup

### 🔹 Prerequisites
Ensure you have **Google Chrome** and **ChromeDriver** installed.  
- [Download Google Chrome](https://www.google.com/chrome/)  
- [Download ChromeDriver](https://sites.google.com/chromium.org/driver/)  

### 🔹 Install Dependencies
Run the following command to install Selenium:

```bash
pip install selenium
```

### 🔹 Run the Script
Execute the script:

```bash
python scraper.py
```

## 📁 Output
The extracted results are saved in **sample.csv**, formatted as:

```csv
Roll_no, NAME, NET_FRAMEWORK_Internal, Cyber_Laws_Internal, Computer_Graphics_I, Linux_i, Optimization_i, net_framework_E, Cyber_E, ComputerGraph_E, Linux_E, OT_E, RESULT, TOTAL
211341133001, John Doe, 25, 28, 30, 27, 24, 40, 42, 35, 37, 38, PASS, 400
...
```

## 🎯 Future Improvements
🔹 Add support for other universities by modifying **URL and XPaths**.  
🔹 Implement **GUI/CLI options** for user interaction.  
🔹 Store results in a **database** for better analysis.  

## 🏆 Author
**[Your Name]**  
📧 Email: your.email@example.com  
🔗 LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)  

---

🚀 **For Bundelkhand University results! Modify the script for other websites as needed.**