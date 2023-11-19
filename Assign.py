def get_employee_info():
    employee_id = input("Enter Employee ID: ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    date_of_birth = input("Enter Date of Birth (YYYY-MM-DD): ")
    sex = input("Enter Sex (M/F): ")
    year_of_recruitment = input("Enter Year of Recruitment: ")
    salary = input("Enter Salary: ")

    employee = {
        'Employee ID': employee_id,
        'First Name': first_name,
        'Last Name': last_name,
        'Date of Birth': date_of_birth,
        'Sex': sex,
        'Year of Recruitment': year_of_recruitment,
        'Salary': salary
    }

    return employee


def main():
    # Get the number of employees to record
    num_employees = int(input("Enter the number of employees to record: "))

    # Create an empty list to store employee dictionaries
    employee_database = []

    # Loop to enter information for each employee
    for _ in range(num_employees):
        employee_data = get_employee_info()
        employee_database.append(employee_data)

    # Display all entered employees
    print("\nEmployee Database:")
    for employee in employee_database:
        print("\nEmployee Information:")
        for key, value in employee.items():
            print(f"{key}: {value}")
        print("------------------------------")


if __name__ == "__main__":
    main()
