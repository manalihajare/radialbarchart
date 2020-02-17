

def kex(N):
    alpha=2*np.pi/N
    alphas = alpha*np.arange(N)
    coordX = np.cos(alphas)
    coordY = np.sin(alphas)

    return np.c_[coordX, coordY, alphas]

N = wedges
r = bottom*.995
points = kex(N)
#ax.scatter(points[:,0], points[:,1])

for i in range(0,wedges):
    a = points[i,2] 
    x,y = (r*np.cos(a), r*np.sin(a))
    if points[i,0] < 0: a = a - np.pi
    ax.text(x,y, "-", rotation = np.rad2deg(a), transform=ax.transData._b, ha="center", va="center",
                   )
