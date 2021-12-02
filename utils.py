
def day_part(i):
    if (i >= 4) and (i < 8):
        return 'Early Morning'
    elif (i >= 8) and (i < 12):
        return 'Morning'
    elif (i >= 12) and (i < 16):
        return 'Noon/Afternoon'
    elif (i >= 16) and (i < 20):
        return 'Evening'
    elif (i >= 20) and (i <= 24):
        return 'Night'
    elif (i > 24) and (i < 4):
        return 'Latenight'