def OMS(group):

    for b in group:
        b.append((b[0] + b[1]) / 2)
    
    oms = sig_f = sig_mf = 0
    
    for b in group:
        sig_mf +=  b[2] * b[3]
        sig_f += b[2]
    
    x_bar = sig_mf / sig_f

    for b in group:
        oms += abs(b[2] * (b[3] - x_bar))  
    oms /= sig_f

    print("OMS =",round(oms, 2))

OMS([ [10,20,3], [20,30,6], [30,40,9], [40,50,12], [50,60,15] ])