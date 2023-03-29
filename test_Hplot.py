from Quaternion import Quaternion
from Hplot import Hplot
from multiprocessing import Process

def specialPrint(L:list):
    for i in range(len(L)):
        ans = ''
        for j in range(len(L)):
            if L[i][j]:
                ans += f'({i},{j}) -> true\t\t'
        print(ans)



if __name__ == '__main__':
    
    L = [Quaternion.random() for _ in range(50)]
    # L = [Quaternion(1), Quaternion(1,1,0,0), Quaternion(1,0,1,0), Quaternion(1,0,0,1)]
    
#     r = Process(target=Hplot.pathplot, args=(L,))
#     r.start()
#     s = Process(target=Hplot.plot, args=(L,))
#     s.start()
#     t = Process(target=Hplot.distplot, args=(L,))
#     t.start()
#     t.join()
#     r.join()
#     s.join()

    # x = Hplot.getPaths(L)
    # specialPrint(x)

    Hplot.plot(L)
    # Hplot.pathplot(L)
    # Hplot.stereo_pjrN(L)
    # Hplot.stereo_prjS(L)