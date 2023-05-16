
WEEK_DAYS = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]



def add_time(start, end, days = False):
    # clean start data
    number_day_pass = 0
    prd = start[5:].strip().lower()
   
    start = start.replace('AM','')
    start = start.replace('PM','')
    Hour, Min = start.split(':')
    Hour = int(Hour)
    Min = int(Min)

    # clean end data
    end = end.replace('PM','')
    Add_Hour, Add_Min = end.split(':')
    Add_Hour = int(Add_Hour)
    Add_Min = int(Add_Min)
    
    # combine to times
    total_hour = Hour + Add_Hour
    total_min = Min + Add_Min
    

    if total_min >= 60:
        total_hour += int(total_min / 60)
        total_min = int(total_min % 60)
    
    if total_min < 10:
        total_min = '{:02d}'.format(total_min)

    if prd == 'pm' and total_hour >= 12:
        day = total_hour//24 + 1
    elif prd == 'am':
        day = total_hour//24
        
    elif prd == 'pm' or prd == 'am' and total_hour < 12:
        day = 0
        
        
    # am and pm
    if prd == 'am' and total_hour >= 12:
        if total_hour % 24 < 12:
            prd = 'am'
        else:
        
            prd = 'pm'
        
    elif prd == 'pm' and total_hour > 12:
        prd = 'am'
        
  
  
            
    if total_hour >= 12:
        hours_left = total_hour / 12
      
        if hours_left < 12 and prd == 'am':
            prd = 'am'
        else:
            prd 
    
    total_hour = int(total_hour % 12) or Hour + 1
    
    if days:
        days = days.lower()
        current_index = WEEK_DAYS.index(days)
    
    # Calculate the position after 20 turns
        position_after_turns = (current_index + day) % 7
    
    # Get the item at the new position
        item_after_turns = WEEK_DAYS[position_after_turns]
        item_after_turns = item_after_turns.capitalize()
        
        if int(day) == 1:
            return str(total_hour) +":"+str(total_min) +" "+prd.upper() +", {}".format(item_after_turns)+ " (next day)"
        elif int(day) > 1:
            return str(total_hour) +":"+str(total_min) +" "+prd.upper() +", {}".format(item_after_turns) +" ({} days later)".format(str(day))
        else:
            return str(total_hour) +":"+str(total_min) +" "+prd.upper() +", {}".format(item_after_turns)
    else:
        if int(day) == 1:
            return str(total_hour) +":"+str(total_min) +" "+prd.upper() + " (next day)"
        elif int(day) > 1:
            return str(total_hour) +":"+str(total_min) +" "+prd.upper() +" ({} days later)".format(str(day))
        else:
            return str(total_hour) +":"+str(total_min) +" "+prd.upper()


