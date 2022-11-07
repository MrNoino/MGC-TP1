import matplotlib.pyplot as plt

def plot3D(data):

    #"fatia" o array apenas com a coluna 0
    Xs = data[:,0]
    #"fatia" o array apenas com a coluna 1
    Ys = data[:,1]
    #"fatia" o array apenas com a coluna 2
    Zs = data[:,2]

    #cria a figura necessária à projeção do gráfico
    fig = plt.figure()
    #define os eixos como 3D
    ax = plt.axes(projection='3d')
    #cria o gráfico 3D
    ax.plot_trisurf(Xs, Ys, Zs)
    #mostra o gráfico 3D
    plt.show()