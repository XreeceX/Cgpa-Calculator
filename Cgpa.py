import csv
import os
directory = '###############################'  #update your directry to store the csv file
file_path = os.path.join(directory, 'cgpa.csv')

os.makedirs(directory, exist_ok=True)

def sumcgpa():
    total_cgpa = 0
    count = 0
    if os.path.exists(file_path):
        with open(file_path, 'r') as cgpa_file:
            reader = csv.reader(cgpa_file)
            next(reader)
            for row in reader:
                if row and row[1].replace('.', '', 1).isdigit():
                    total_cgpa += float(row[1])
                    count += 1
    return total_cgpa, count

def read():
    total_cgpa, count = sumcgpa()
    sgpa_sum = 0
    if os.path.exists(file_path):
        with open(file_path, 'r') as cgpa_file:
            reader = csv.reader(cgpa_file)
            print("Previous Grades")
            for row in reader:
                if row and len(row) == 2 and row[0].startswith('sem') and row[1].replace('.', '', 1).isdigit():
                    print([row[0], float(row[1])])
                    sgpa_sum += float(row[1])
    if count > 0:
        print(f'Total={sgpa_sum}/{10*count}')
        print(["CGPA Total", f'{(sgpa_sum / count):.3f}'])
    else:
        print("No data available.")

def base():
    with open(file_path, 'w', newline='') as cgpa_file:
        writer = csv.writer(cgpa_file)
        writer.writerow(['Semester', 'CGPA'])
    cgpa_file.close()

def write(data=None):
    if not os.path.exists(file_path):
        base()

    next_semester = 1
    rows = []
    with open(file_path, 'r') as cgpa_file:
        reader = csv.reader(cgpa_file)
        rows = list(reader)
        if len(rows) > 1:
            for row in rows:
                if row[0].startswith("sem"):
                    next_semester = int(row[0][3:]) + 1

    with open(file_path, 'a', newline='') as cgpa_file:
        writer = csv.writer(cgpa_file)
        writer.writerow([f"sem{next_semester}", data])

    print("Updated Grades")
    read()

if __name__ == '__main__':
    val = input("Read or write (r/w): ")
    if val.lower() == 'r':
        read()
    else:
        data = float(input("Enter SGPA marks: "))
        write(data)
