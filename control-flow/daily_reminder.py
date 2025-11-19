def generate_reminder():
    """
    Prompts the user for a task, its priority, and time sensitivity,
    then provides a customized reminder using conditional logic.
    """
    
    # 1. Prompt for a Single Task
    task = input("Enter your task: ")
    
    # Prompt for priority and convert to lowercase for easier matching
    priority = input("Priority (high/medium/low): ").lower()
    
    # Prompt for time-bound status and convert to lowercase
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    # Initialize the base reminder message
    base_message = ""
    
    # Use Match Case to determine the base reminder based on priority
    match priority:
        case "high":
            base_message = f"'{task}' is a high priority task"
        case "medium":
            base_message = f"'{task}' is a medium priority task"
        case "low":
            base_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        case _:
            # Default case for invalid priority input
            print("Invalid priority entered. Please use high, medium, or low.")
            return
            
    # 2. Process the Task Based on Time Sensitivity (using if statement)
    
    # Check if the task is high or medium priority AND time-bound
    if time_bound == "yes" and (priority == "high" or priority == "medium"):
        # The specific message requested by the high/medium time-bound case
        time_sensitivity_message = " that requires immediate attention today!"
        
        # We only append the immediate attention message if it's NOT a low priority task
        if priority != "low":
            final_reminder = base_message + time_sensitivity_message
        else:
            # If low priority is time-bound, we still stick to the low message
            final_reminder = base_message 

    # Handle the case where a low priority task is NOT time-bound, or is time-bound but still low
    elif priority == "low":
        final_reminder = base_message
        
    # Handle high/medium priority tasks that are NOT time-bound
    else:
        final_reminder = base_message + ". Schedule it soon."
        
    # 3. Print the Customized Reminder
    print(f"\nReminder: {final_reminder}")

# Run the function to execute the script logic
generate_reminder()