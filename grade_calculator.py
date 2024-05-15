def calculate_average_grade():
    # Prompting the user for their name

    student_name = input("Hello, what is your name: ")
    # print(student_name)

    # Prompting the user for their scores in Math, Science, and English
   
    # Math score
    try:
        # Testing for and prompting the user for their correct math score - a number
        math_score_input = input(f"{student_name} What is your math score: ")
        math_score = float(math_score_input)
    except ValueError:
        print(f"{student_name} Please enter a valid number for the math score.")


    # Science score
    try:
        # Testing for and prompting the user for their correct science score - a number
        science_score_input = input(f"{student_name} What is your science score ")
        science_score =float(science_score_input)
    except ValueError:
        print(f"{student_name} Please enter a valid number for the science score.")

    # English score
    try:
        # Testing for and prompting the user for their correct math score - a number
        english_score_input = input(f"{student_name} What is your english score ")
        english_score =float(english_score_input)
    except ValueError:
        print(f"{student_name} Please enter a valid number for the english score.")

    total_subjects = 3 
    # print(math_score)
    # print(science_score)
    # print(english_score)
    
    # Calculate the average grade
    average_grade = (math_score+science_score+english_score)/total_subjects
    print(f"{student_name} Your average grade is:", average_grade)

    
    # Return the student's name and their average grade
    return student_name, average_grade



if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # Print the student's name and their average grade
    print(f"")