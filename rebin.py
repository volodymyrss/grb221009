import numpy as np

def rebin_in_bins(t, x, T, agg=np.mean):
    # i =
    X = []
    for _t1, _t2 in zip(T[:-1], T[1:]):
        m = (t > _t1) & (t <= _t2)
        X.append(agg(x[m]))

    return np.array(X)


def rebin_bins_in_bins(t, dt, x, dx, Tb):
    T = []
    dT = []
    X = []
    dX = []    
    for _t1, _t2 in zip(Tb[:-1], Tb[1:]):        
        m = (t > _t1) & (t <= _t2)
        if np.sum(m) > 0:
            T.append((np.max(t[m] + dt[m]) + np.min(t[m] - dt[m]))/2)
            dT.append((np.max(t[m] + dt[m]) - np.min(t[m] - dt[m]))/2)
            X.append(np.sum(x[m]*dt[m])/dT[-1])
            dX.append(
                np.sum((dx[m]*dt[m])**2)**0.5/dT[-1]
                )

    return np.array(T), np.array(dT), np.array(X), np.array(dX)
