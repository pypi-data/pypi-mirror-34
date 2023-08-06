def linear_congruence_random_generator(x) :
    """ Function to calculate linear congruences value and computer bet  """    
    a = 22695477
    b=1
    m=2**32
    lnr_val = (a * x + b) % m
    
    if lnr_val <= 2**31 :
        comp_move = 0
               
    else :
        comp_move = 1    
     
    return lnr_val, comp_move


