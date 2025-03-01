# Result Management System (with Hadoop Processing)

## Project Overview
- **Generates 10,000 student profiles**
- **Processes student marks using Hadoop MapReduce**
- **Provides statistical analysis (Mean, Variance, etc.)**
- **Displays student results in a web dashboard (Flask)**

## How to Run
1. **Install Dependencies**
   ```bash
   pip install flask pandas mrjob
   ```
2. **Run Hadoop Processing**
   ```bash
   python Code/hadoop_processing.py Output/student_data.csv > Output/processed_results.txt
   ```
3. **Run Flask App**
   ```bash
   python Code/backend/app.py
   ```
4. **Open in Browser**
   ```
   http://127.0.0.1:5000/
   ```

## Folder Structure
- **Code/** → Backend, Hadoop scripts, Web UI
- **Output/** → Student data & processed results
- **Deployment/** → Docker & Cloud setup

