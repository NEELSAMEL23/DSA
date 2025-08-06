def count_duration(times):
    # Read the time values
    SH, SM, EH, EM = times
    
    # Convert both starting and ending times to total minutes
    start_minutes = SH * 60 + SM
    end_minutes = EH * 60 + EM
    
    # Calculate the time difference in minutes
    if end_minutes < start_minutes:
        end_minutes += 24 * 60  # Adjust for next day
    
    diff_minutes = end_minutes - start_minutes
    
    # Convert the difference back to hours and minutes
    hours = diff_minutes // 60
    minutes = diff_minutes % 60
    
    # Return the result as "HH MM"
    return f"{hours} {minutes}"

# Example usage
times = [1, 44, 2, 14]  # Single time interval (SH, SM, EH, EM)
result = count_duration(times)
print(result)
