
def total_salary(path):
    try:
        with open(path,'r',encoding='utf-8') as source_file:
            salaries_data = source_file.read().splitlines()
        salaries_data = [worker.split(',') for worker in salaries_data]
        salaries_list = []
        [salaries_list.append(float(worker[1])) for worker in salaries_data]

        salaries_total = sum(salaries_list)
        salaries_mean = salaries_total / len(salaries_list)
        return (salaries_total, salaries_mean)
    except FileNotFoundError:
       print("Sorry, there is no such file on the following directory")


try:
    total, average = total_salary("salaries_data")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except TypeError:
    print("Salary file wasn't processed")


x = ['John']
print(x[0])
