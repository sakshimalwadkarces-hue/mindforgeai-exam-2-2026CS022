import pandas as pd
import io

# The dataset provided in your exam paper
csv_data = """student_id,name,department,attendance_pct,diary_entries,tasks_completed,assignment_score,lab_score
2026CS001,Aditi,Computer Engineering,92,12,8,84,88
2026CS002,Bhavana,Computer Engineering,64,6,5,58,61
2026IT001,Chaitra,Information Technology,78,9,7,72,76
2026IT002,Divya,Information Technology,55,4,3,46,52
2026CE001,Esha,Civil Engineering,88,10,8,79,82
2026CE002,Fatima,Civil Engineering,71,8,6,66,69
2026CS003,Gauri,Computer Engineering,96,14,9,91,94
2026IT003,Harshada,Information Technology,43,2,2,35,41"""

# 1. READ TABULAR DATA
# Simulating reading a CSV file
df = pd.read_csv(io.StringIO(csv_data))

# 2. VALIDATE MISSING VALUES
if df.isnull().values.any():
    print("Warning: Missing values detected. Filling empty spaces with 0.")
    df = df.fillna(0)

# 3. CALCULATE SIGNALS
# Creating a custom logic weight: 40% Attendance, 20% Diary, 40% Tasks
def calculate_readiness(row):
    attendance_pts = row['attendance_pct'] * 0.40
    # Assuming max diary entries is 15
    diary_pts = (row['diary_entries'] / 15) * 100 * 0.20
    # Assuming max tasks is 10
    task_pts = (row['tasks_completed'] / 10) * 100 * 0.40
    
    return round(attendance_pts + diary_pts + task_pts, 2)

df['readiness_score'] = df.apply(calculate_readiness, axis=1)

# 4. CLASSIFY INTO PERFORMANCE BANDS
def classify_band(score):
    if score < 40:
        return "Support"
    elif score < 70:
        return "Developing"
    elif score < 90:
        return "Strong"
    else:
        return "Excellent"

df['performance_band'] = df['readiness_score'].apply(classify_band)

# 5. GENERATE FINAL INSIGHTS
print("--- DATA ANALYTICS PIPELINE OUTPUT ---\n")

print("[STUDENT CLASSIFICATIONS]")
print(df[['name', 'readiness_score', 'performance_band']].to_string(index=False))

print("\n[FINAL INSIGHTS]")
# Insight A: Students needing support
support_students = df[df['performance_band'] == 'Support']['name'].tolist()
print(f"1. Students needing immediate support: {', '.join(support_students) if support_students else 'None'}")

# Insight B: Top Performer
top_student = df.loc[df['readiness_score'].idxmax()]
print(f"2. Top Performer: {top_student['name']} with a score of {top_student['readiness_score']}")

# Insight C: Department Averages
dept_avg = df.groupby('department')['readiness_score'].mean().round(2).to_dict()
print(f"3. Department Readiness Averages:")
for dept, avg in dept_avg.items():
    print(f"   - {dept}: {avg}")