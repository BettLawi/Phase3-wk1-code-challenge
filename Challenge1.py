def time_converter(hour,minute,period):
    if period == 'am':
        return f"{hour:02d}{minute:02d}"
    else:
        return f"{hour+12:02d}{minute:02d}"    

print(time_converter(8,30,"am"))  
print(time_converter(8,30,"pm"))           