

import datetime 

def main():
    """Main function to run the calorie tracker application."""
    
    
    print("="*50)
    print("      Welcome to the Daily Calorie Tracker!      ")
    print("="*50)
    print("This tool will help you log your meals and track")
    print("your total calorie intake against a daily limit.")
    print("\n")

    meal_names = []
    calorie_amounts = []
    
    
    while True:
        try:
            meal_count = int(input("How many meals would you like to log? "))
            if meal_count < 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    for i in range(meal_count):
        print(f"\n--- Logging Meal {i+1} ---")
        meal_name = input(f"Enter name for meal {i+1}: ")
        
        
        while True:
            try:
                calorie_amount = int(input(f"Enter calories for '{meal_name}': "))
                if calorie_amount < 0:
                    print("Calories must be a positive number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a whole number for calories.")
        
        meal_names.append(meal_name)
        calorie_amounts.append(calorie_amount)

    
    total_calories = 0
    average_calories = 0.0
    
    if meal_count > 0:
        total_calories = sum(calorie_amounts) 
        average_calories = total_calories / meal_count 
    while True:
        try:
            daily_limit = int(input("\nWhat is your daily calorie limit? "))
            if daily_limit <= 0:
                print("Limit must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

   
    report_lines = []
    
    report_lines.append("\n" + "="*30)
    report_lines.append("      SESSION SUMMARY      ")
    report_lines.append("="*30)
    
    report_lines.append(f"{'Meal Name':<20}{'Calories':>10}")
    report_lines.append("-"*30)
    
   
    for name, cals in zip(meal_names, calorie_amounts):
        report_lines.append(f"{name:<20}{cals:>10}")
        
    report_lines.append("-"*30)
    report_lines.append(f"{'Total:':<20}{total_calories:>10}")
    report_lines.append(f"{'Average:':<20}{average_calories:>10.2f}")
    report_lines.append(f"{'Your Limit:':<20}{daily_limit:>10}")
    report_lines.append("="*30)

   
    if total_calories > daily_limit:
        warning_msg = f"\nWARNING: You are {total_calories - daily_limit} calories OVER your limit!"
        report_lines.append(warning_msg)
    else:
        success_msg = f"\nSUCCESS: You are {daily_limit - total_calories} calories UNDER your limit."
        report_lines.append(success_msg)
    
    
    for line in report_lines:
        print(line)

    
    print("\n")
    save_log = input("Would you like to save this log to a file? (y/n): ").strip().lower()
    
    if save_log == 'y':
       
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
           
            with open("calorie_log.txt", "a") as file:
                file.write(f"\n--- LOG SAVED ON: {timestamp} ---\n")
                
                
                for line in report_lines:
                    file.write(line + "\n")
                    
                file.write("--- END OF LOG ---\n")
                
            print(f"Successfully saved log to 'calorie_log.txt'")
            
        except IOError as e:
            print(f"Error: Could not save file. {e}")
    else:
        print("Log not saved. Exiting.")


if __name__ == "__main__":
    main()