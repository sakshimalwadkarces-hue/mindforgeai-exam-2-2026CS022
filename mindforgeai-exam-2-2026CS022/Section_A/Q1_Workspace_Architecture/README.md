# Q1. Workspace Architecture Map (8 Marks)

## 1. System Architecture Diagram

*(Please draw the following workflow on your answer sheet)*

Local Development (VS Code & Local Jupyter) 
-> Cloud Testing (Google Colab) 
-> Versioning & Storage (GitHub Repository & Google Drive) 
-> Final Submission (Assessment Portal)

---

## 2. Component Responsibilities

* **VS Code:** Acts as the primary local editor. It is responsible for managing the project folder structure, writing the README documentation, and pushing the final code to the GitHub repository via the terminal.

* **Local Jupyter:** Serves as the offline coding environment. It is used to initially write, execute, and logically test the Python code against the local dataset before deploying it online.

* **Google Colab:** Functions as the cloud-based validation environment. It ensures the notebook runs correctly on an isolated external server and generates a shareable URL for the examiner.

* **GitHub Repository:** Operates as the version control and package hosting system. It securely stores the completed code, datasets, and project screenshots for review.

* **Google Drive:** Acts as the static document cloud storage. Its specific role in this workflow is to host the scanned PDF of the handwritten exam answers and provide a view-only link.

* **Final Portal:** Serves as the ultimate deployment target. This is where all individual links (GitHub, Drive, Colab) are aggregated and submitted for official grading.