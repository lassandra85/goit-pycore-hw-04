from pathlib import Path

def total_salary(path):

    file_path = Path(path)

    if file_path.exists():

        text = file_path.read_text(encoding="utf-8")
        total = 0
        count = 0

        for line in text.splitlines():

            try:
                name, salary = line.strip().split(",")
                total += int(salary)
                count += 1

            except ValueError:

                print("Файл містить помилкові дані. Перевірте вміст.")

                return 0, 0
            
        average = total/count if count > 0 else 0

        return total, average
    else:
        print("Файл не знайдено. Перевірте шлях до файлу.")
        return 0, 0
   

# Приклад використання функції
salary = "salary_file.txt"
total, average = total_salary(salary)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
