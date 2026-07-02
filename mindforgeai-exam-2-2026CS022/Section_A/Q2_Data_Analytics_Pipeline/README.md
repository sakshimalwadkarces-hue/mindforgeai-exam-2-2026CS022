# MindforgeAI Exam 2: Student Performance Analytics Pipeline

**Student ID:** `<your-student-id>`  
**Author:** `<Your Name>`

## 🎯 Objective
This repository contains a data analytics pipeline developed for the MindforgeAI Internship (Week 2-3 Practical Examination). The objective of this project is to process tabular student data, calculate a weighted academic readiness score based on five key signals (attendance, diary entries, tasks, assignments, and labs), and classify each student into a performance band (Support, Developing, Strong, or Excellent). 

## 🛠️ Tools Used
* **Language:** Python 3
* **Libraries:** Pandas (for data manipulation and analysis)
* **Environment:** Jupyter Notebook / Google Colab
* **Version Control:** Git & GitHub

## 📂 Repository Structure
* `data/` - Contains the dataset `week_2_3_exam_student_signals.csv`.
* `notebooks/` - Contains the fully executed Jupyter Notebook (`.ipynb`) with the data pipeline and markdown explanations.
* `outputs/` - Contains screenshots and evidence of the executed code and final analytics outputs.

## 🚀 How to Run
1.  Clone this repository to your local machine:
    ```bash
    git clone [https://github.com/yourusername/mindforgeai-exam-2-](https://github.com/yourusername/mindforgeai-exam-2-)<your-student-id>.git
    ```
2.  Navigate into the repository directory:
    ```bash
    cd mindforgeai-exam-2-<your-student-id>
    ```
3.  Ensure you have Python and Pandas installed. If not, install Pandas via pip:
    ```bash
    pip install pandas
    ```
4.  Open the notebook located in the `notebooks/` folder using Jupyter Notebook, Jupyter Lab, or VS Code, and run all cells sequentially. Alternatively, you can upload the notebook to Google Colab.

## 📊 Result Summary
Based on the data pipeline execution, the following insights were generated:
* **Strongest Department:** The **Computer Engineering** department demonstrated the highest average readiness score (79.23), led by top-performing students.
* **Top Performer:** **Gauri** (Computer Engineering) achieved the highest readiness score of 93.73.
* **Support Required:** **Harshada** (Score: 36.67) and **Divya** (Score: 48.73) were classified into the "Support" band and require immediate academic intervention, primarily due to critically low attendance and task completion rates.