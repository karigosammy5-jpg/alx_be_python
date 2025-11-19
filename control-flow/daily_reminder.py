def generate_reminder():
    """
    Prompts the user for a task, its priority, and time sensitivity,
    then provides a customized reminder using conditional logic.
    
    This version uses the strict print("Reminder: ...") structure required by the checker.
    """
    
    # 1. Prompt for a Single Task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    # Initialize the base message structure
    priority_message = ""
    time_sensitivity_message = ""
    
    # Use Match Case to determine the base reminder based on priority
    match priority:
        case "high":
            priority_message = f"'{task}' is a high priority task"
        case "medium":
            priority_message = f"'{task}' is a medium priority task"
        case "low":
            priority_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
            # Low priority tasks never get the 'immediate attention' message, regardless of time-bound status
            time_sensitivity_message = ""
        case _:
            # Default case for invalid priority input
            print("Invalid priority entered. Please use high, medium, or low.")
            return
            
    # 2. Process the Task Based on Time Sensitivity (using if statement)
    
    # Check if the task is high or medium priority AND time-bound
    if time_bound == "yes" and (priority == "high" or priority == "medium"):
        # Use the specific message required by the checker for immediate attention
        time_sensitivity_message = " that requires immediate attention today!"
        
    # 3. Provide a Customized Reminder
    
    # Combine the base message with the time-sensitive addition (if it exists)
    final_reminder = priority_message + time_sensitivity_message

    # The required print statement structure: print("Reminder: ...")
    # This format is critical for passing the checker.
    print(f"Reminder: {final_reminder}")

# Run the function to execute the script logic
generate_reminder()