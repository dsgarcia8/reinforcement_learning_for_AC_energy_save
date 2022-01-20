import datetime

MORNING_HOUR_START = 8
MORNING_HOUR_END = 13
AFTERNOON_HOUR_START = 17
AFTERNOON_HOUR_END = 19
NIGHT_HOUR_END = 24

def get_state(occupancy: int, ac_status: int, comfort: int, time: int ) -> int :
    """
    Returns: 
    int: state index [0,63]
    """
    # period 1 8:00 - 13:00 
    if MORNING_HOUR_START <= time < MORNING_HOUR_END: 
        if occupancy == 1: 
            if ac_status == 2: # estado OFF
                if comfort == 0:
                    return 0
                if comfort == 1:
                    return 1
                if comfort == 2:
                    return 2        
            if 3 <= ac_status <= 5: # T1 [16-18]
                if comfort == 0:
                    return 3
                if comfort == 1:
                    return 4
                if comfort == 2:
                    return 5       
            if 6 <= ac_status <= 8: # T2 [19-21]
                if comfort == 0:
                    return 6
                if comfort == 1:
                    return 7
                if comfort == 2:
                    return 8     
            if 9 <= ac_status <= 11: # T2 [22-23]
                if comfort == 0:
                    return 9
                if comfort == 1:
                    return 10
                if comfort == 2:
                    return 11     
        if occupancy == 0:
            if ac_status == 2:
                return 12
            if 3 <= ac_status <= 5:
                return 13
            if 6 <= ac_status <= 8:
                return 14
            if 9 <= ac_status <= 11:
                return 15            
    # period 2 13:00 - 17:00
    if MORNING_HOUR_END <= time < AFTERNOON_HOUR_START:
        if occupancy == 1: 
            if ac_status == 2: # estado OFF
                if comfort == 0:
                    return 16
                if comfort == 1:
                    return 17
                if comfort == 2:
                    return 18        
            if 3 <= ac_status <= 5: # T1 [16-18]
                if comfort == 0:
                    return 19
                if comfort == 1:
                    return 20
                if comfort == 2:
                    return 21       
            if 6 <= ac_status <= 8: # T2 [19-21]
                if comfort == 0:
                    return 22
                if comfort == 1:
                    return 23
                if comfort == 2:
                    return 24     
            if 9 <= ac_status <= 11: # T2 [22-23]
                if comfort == 0:
                    return 25
                if comfort == 1:
                    return 26
                if comfort == 2:
                    return 27     
        if occupancy == 0:
            if ac_status == 2:
                return 28
            if 3 <= ac_status <= 5:
                return 28
            if 6 <= ac_status <= 8:
                return 30
            if 9 <= ac_status <= 11:
                return 31    
    # period 3 17:00 - 19:00
    if AFTERNOON_HOUR_START <= time < AFTERNOON_HOUR_END:
        if occupancy == 1: 
            if ac_status == 2: # estado OFF
                if comfort == 0:
                    return 32
                if comfort == 1:
                    return 33
                if comfort == 2:
                    return 34        
            if 3 <= ac_status <= 5: # T1 [16-18]
                if comfort == 0:
                    return 35
                if comfort == 1:
                    return 36
                if comfort == 2:
                    return 37       
            if 6 <= ac_status <= 8: # T2 [19-21]
                if comfort == 0:
                    return 38
                if comfort == 1:
                    return 39
                if comfort == 2:
                    return 40     
            if 9 <= ac_status <= 11: # T2 [22-23]
                if comfort == 0:
                    return 41
                if comfort == 1:
                    return 42
                if comfort == 2:
                    return 43     
        if occupancy == 0:
            if ac_status == 2:
                return 44
            if 3 <= ac_status <= 5:
                return 45
            if 6 <= ac_status <= 8:
                return 46
            if 9 <= ac_status <= 11:
                return 47    
    # period 4 19:00 - 23:59
    if AFTERNOON_HOUR_END <= time < NIGHT_HOUR_END:
        if occupancy == 1: 
            if ac_status == 2: # estado OFF
                if comfort == 0:
                    return 48
                if comfort == 1:
                    return 49
                if comfort == 2:
                    return 50        
            if 3 <= ac_status <= 5: # T1 [16-18]
                if comfort == 0:
                    return 51
                if comfort == 1:
                    return 52
                if comfort == 2:
                    return 53       
            if 6 <= ac_status <= 8: # T2 [19-21]
                if comfort == 0:
                    return 54
                if comfort == 1:
                    return 55
                if comfort == 2:
                    return 56     
            if 9 <= ac_status <= 11: # T2 [22-23]
                if comfort == 0:
                    return 57
                if comfort == 1:
                    return 58
                if comfort == 2:
                    return 59     
        if occupancy == 0:
            if ac_status == 2:
                return 60
            if 3 <= ac_status <= 5:
                return 61
            if 6 <= ac_status <= 8:
                return 62
            if 9 <= ac_status <= 11:
                return 63  

def get_next_state(current_state: int, action: int) -> int:
    """
        las acciones son 0: apagar, 1: subir, 2: bajar;
        los estados son 0,,63
    """
    if action == 0 :
        #p1
        if current_state == 0:
            return 0
        if current_state == 1:
            return 1
        if current_state == 2:
            return 2
        if current_state == 3:
            return 0
        if current_state == 4:
            return 1
        if current_state == 5:
            return 2
        if current_state == 6:
            return 0
        if current_state == 7:
            return 1
        if current_state == 8:
            return 2
        if current_state == 9:
            return 0
        if current_state == 10:
            return 1
        if current_state == 11:
            return 2
        if current_state == 12:
            return 12
        if current_state == 13:
            return 12
        if current_state == 14:
            return 12
        if current_state == 15:
            return 12
        #p2
        if current_state == 16:
            return 16
        if current_state == 17:
            return 17
        if current_state == 18:
            return 18
        if current_state == 19:
            return 16
        if current_state == 20:
            return 17
        if current_state == 21:
            return 18
        if current_state == 22:
            return 16
        if current_state == 23:
            return 17
        if current_state == 24:
            return 18
        if current_state == 25:
            return 16
        if current_state == 26:
            return 17
        if current_state == 27:
            return 18
        if current_state == 28:
            return 28
        if current_state == 29:
            return 28
        if current_state == 30:
            return 28
        if current_state == 31:
            return 28
        #p3
        if current_state == 32:
            return 32
        if current_state == 33:
            return 33
        if current_state == 34:
            return 34
        if current_state == 35:
            return 32
        if current_state == 36:
            return 33
        if current_state == 37:
            return 34
        if current_state == 38:
            return 32
        if current_state == 39:
            return 33
        if current_state == 40:
            return 34
        if current_state == 41:
            return 32
        if current_state == 42:
            return 33
        if current_state == 43:
            return 34
        if current_state == 44:
            return 44
        if current_state == 45:
            return 44
        if current_state == 46:
            return 44
        if current_state == 47:
            return 44
        #p4
        if current_state == 48:
            return 48
        if current_state == 49:
            return 49
        if current_state == 50:
            return 50
        if current_state == 51:
            return 48
        if current_state == 52:
            return 49
        if current_state == 53:
            return 50
        if current_state == 54:
            return 48
        if current_state == 55:
            return 49
        if current_state == 56:
            return 50
        if current_state == 57:
            return 48
        if current_state == 58:
            return 49
        if current_state == 59:
            return 50
        if current_state == 60:
            return 60
        if current_state == 61:
            return 60
        if current_state == 62:
            return 60
        if current_state == 63:
            return 60
    if action == 1 :
        #p1
        if current_state == 0:
            return 9
        if current_state == 1:
            return 10
        if current_state == 2:
            return 11
        if current_state == 3:
            return 6
        if current_state == 4:
            return 7
        if current_state == 5:
            return 8
        if current_state == 6:
            return 9
        if current_state == 7:
            return 10
        if current_state == 8:
            return 11
        if current_state == 9:
            return 9
        if current_state == 10:
            return 10
        if current_state == 11:
            return 11
        if current_state == 12:
            return 15
        if current_state == 13:
            return 14
        if current_state == 14:
            return 15
        if current_state == 15:
            return 15
        #p2
        if current_state == 16:
            return 25
        if current_state == 17:
            return 26
        if current_state == 18:
            return 27
        if current_state == 19:
            return 22
        if current_state == 20:
            return 23
        if current_state == 21:
            return 24
        if current_state == 22:
            return 25
        if current_state == 23:
            return 26
        if current_state == 24:
            return 27
        if current_state == 25:
            return 25
        if current_state == 26:
            return 26
        if current_state == 27:
            return 27
        if current_state == 28:
            return 31
        if current_state == 29:
            return 30
        if current_state == 30:
            return 31
        if current_state == 31:
            return 31
        #p3
        if current_state == 32:
            return 41
        if current_state == 33:
            return 42
        if current_state == 34:
            return 43
        if current_state == 35:
            return 38
        if current_state == 36:
            return 39
        if current_state == 37:
            return 40
        if current_state == 38:
            return 41
        if current_state == 39:
            return 42
        if current_state == 40:
            return 43
        if current_state == 41:
            return 41
        if current_state == 42:
            return 42
        if current_state == 43:
            return 43
        if current_state == 44:
            return 47
        if current_state == 45:
            return 46
        if current_state == 46:
            return 47
        if current_state == 47:
            return 47
        #p4
        if current_state == 48:
            return 57
        if current_state == 49:
            return 58
        if current_state == 50:
            return 59
        if current_state == 51:
            return 54
        if current_state == 52:
            return 55
        if current_state == 53:
            return 56
        if current_state == 54:
            return 57
        if current_state == 55:
            return 58
        if current_state == 56:
            return 59
        if current_state == 57:
            return 57
        if current_state == 58:
            return 58
        if current_state == 59:
            return 59
        if current_state == 60:
            return 63
        if current_state == 61:
            return 62
        if current_state == 62:
            return 63
        if current_state == 63:
            return 63    
    if action == 2 :
        #p1
        if current_state == 0:
            return 0
        if current_state == 1:
            return 1
        if current_state == 2:
            return 2
        if current_state == 3:
            return 3
        if current_state == 4:
            return 4
        if current_state == 5:
            return 5
        if current_state == 6:
            return 3
        if current_state == 7:
            return 4
        if current_state == 8:
            return 5
        if current_state == 9:
            return 6
        if current_state == 10:
            return 7
        if current_state == 11:
            return 8
        if current_state == 12:
            return 12
        if current_state == 13:
            return 13
        if current_state == 14:
            return 13
        if current_state == 15:
            return 14
        #p2
        if current_state == 16:
            return 16
        if current_state == 17:
            return 17
        if current_state == 18:
            return 18
        if current_state == 19:
            return 19
        if current_state == 20:
            return 20
        if current_state == 21:
            return 21
        if current_state == 22:
            return 19
        if current_state == 23:
            return 20
        if current_state == 24:
            return 21
        if current_state == 25:
            return 22
        if current_state == 26:
            return 23
        if current_state == 27:
            return 24
        if current_state == 28:
            return 28
        if current_state == 29:
            return 29
        if current_state == 30:
            return 29
        if current_state == 31:
            return 30
        #p3
        if current_state == 32:
            return 32
        if current_state == 33:
            return 33
        if current_state == 34:
            return 34
        if current_state == 35:
            return 35
        if current_state == 36:
            return 36
        if current_state == 37:
            return 37
        if current_state == 38:
            return 35
        if current_state == 39:
            return 36
        if current_state == 40:
            return 37
        if current_state == 41:
            return 38
        if current_state == 42:
            return 39
        if current_state == 43:
            return 40
        if current_state == 44:
            return 44
        if current_state == 45:
            return 45
        if current_state == 46:
            return 45
        if current_state == 47:
            return 46
        #p4
        if current_state == 48:
            return 48
        if current_state == 49:
            return 49
        if current_state == 50:
            return 50
        if current_state == 51:
            return 51
        if current_state == 52:
            return 52
        if current_state == 53:
            return 53
        if current_state == 54:
            return 51
        if current_state == 55:
            return 52
        if current_state == 56:
            return 53
        if current_state == 57:
            return 54
        if current_state == 58:
            return 55
        if current_state == 59:
            return 56
        if current_state == 60:
            return 60
        if current_state == 61:
            return 61
        if current_state == 62:
            return 61
        if current_state == 63:
            return 62    
