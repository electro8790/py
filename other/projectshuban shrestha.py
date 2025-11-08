with open("Result.txt", "w") as file:
    file.write("***** DIGITAL REPORT CARD *****\n\n")

    while True:
        name = input("Enter student name: ")

        sub1 = int(input("Enter marks for Subject 1: "))
        sub2 = int(input("Enter marks for Subject 2: "))
        sub3 = int(input("Enter marks for Subject 3: "))

        total = sub1 + sub2 + sub3
        average = total / 3

        if average >= 90:
                grade="A"
        elif average >= 75:
                grade="b"
        elif average >= 60:
                grade='C'
        elif average >= 45:
                grade='D'
        else:
                grade='F'

        print("\n--- STUDENT REPORT ---")
        print(f"Name : {name}")
        print(f"Subject1 : {sub1}")
        print(f"Subject2 : {sub2}")
        print(f"Subject3 : {sub3}")
        print(f"Total : {total}")
        print(f"Average : {average:.2f}")
        print(f"Grade : {grade}")
        print("-----------------------\n")

        file.write(f"Name: {name}\n")
        file.write(f"Subject 1: {sub1}\nSubject 2: {sub2}\nSubject 3: {sub3}\n")
        file.write(f"Total: {total}\nAverage: {average:.2f}\nGrade: {grade}\n")
        file.write("--------------------------\n\n")

        more = input("Do you want to enter another student? (yes/no): ").lower()
        if more != 'yes':
            print("\nAll records saved to 'Result.txt'.")
            break