import matplotlib.pyplot as plt

mode = int(input('Введите 1 - 7\n'))

if mode == 1:
    with open('1(a).txt', 'r') as input_file:
        d_y, fb_y, x = [], [], []
        for line in input_file:
            d_y.append(float(line.split()[0]))
            fb_y.append(float(line.split()[1]))
            x.append(int(line.split()[2]))
    plt.scatter(x, d_y, c='g')
    plt.scatter(x, fb_y, c='r')
    plt.annotate('''
    $q=1$
    $r=10^6$
    $m=n^2/10$
    ''', xy=(0, 20))
    fig1 = plt.figure(1)
    fig1.text(0.44, 0.95, 'алг. Дeйкстры,', color='g')
    fig1.text(0.41, 0.90, 'алг. Форда-Беллмана', color='r')
    plt.xlabel("Число вершин")
    plt.ylabel("Время")
    plt.show()

elif mode == 2:
    with open('1(b).txt', 'r') as input_file:
        d_y, fb_y, x = [], [], []
        for line in input_file:
            d_y.append(float(line.split()[0]))
            fb_y.append(float(line.split()[1]))
            x.append(int(line.split()[2]))
    plt.scatter(x, d_y, c='g')
    plt.scatter(x, fb_y, c='r')
    plt.annotate('''
       $q=1$
       $r=10^6$
       $m=n^2$
       ''', xy=(0, 100))
    fig1 = plt.figure(1)
    fig1.text(0.44, 0.95, 'алг. Дeйкстры,', color='g')
    fig1.text(0.41, 0.90, 'алг. Форда-Беллмана', color='r')
    plt.xlabel("Число вершин")
    plt.ylabel("Время")
    plt.show()

elif mode == 3:
    with open('2(a).txt', 'r') as input_file:
        d_y, fb_y, x = [], [], []
        for line in input_file:
            d_y.append(float(line.split()[0]))
            fb_y.append(float(line.split()[1]))
            x.append(int(line.split()[2]))
    plt.scatter(x, d_y, c='g')
    plt.scatter(x, fb_y, c='r')
    plt.annotate('''
       $q=1$
       $r=10^6$
       $m=100*n$
       ''', xy=(0, 5))
    fig1 = plt.figure(1)
    fig1.text(0.44, 0.95, 'алг. Дeйкстры,', color='g')
    fig1.text(0.41, 0.90, 'алг. Форда-Беллмана', color='r')
    plt.xlabel("Число вершин")
    plt.ylabel("Время")
    plt.show()

elif mode == 4:
    with open('2(b).txt', 'r') as input_file:
        d_y, fb_y, x = [], [], []
        for line in input_file:
            d_y.append(float(line.split()[0]))
            fb_y.append(float(line.split()[1]))
            x.append(int(line.split()[2]))
    plt.scatter(x, d_y, c='g')
    plt.scatter(x, fb_y, c='r')
    plt.annotate('''
       $q=1$
       $r=10^6$
       $m=1000*n$
       ''', xy=(0, 15))
    fig1 = plt.figure(1)
    fig1.text(0.44, 0.95, 'алг. Дeйкстры,', color='g')
    fig1.text(0.41, 0.90, 'алг. Форда-Беллмана', color='r')
    plt.xlabel("Число вершин")
    plt.ylabel("Время")
    plt.show()

elif mode == 5:
    with open('3.txt', 'r') as input_file:
        d_y, fb_y = [], []
        for line in input_file:
            d_y.append(float(line.split()[0]))
            fb_y.append(float(line.split()[1]))
    x = [i for i in range(10 ** 5, 10 ** 7 + 1, 10 ** 5)]
    plt.scatter(x, d_y, c='g')
    plt.scatter(x, fb_y, c='r')
    plt.annotate('''
       $q=1$
       $r=10^6$
       $n=10^4+1$
       ''', xy=(0, 20))
    fig1 = plt.figure(1)
    fig1.text(0.44, 0.95, 'алг. Дeйкстры,', color='g')
    fig1.text(0.41, 0.90, 'алг. Форда-Беллмана', color='r')
    plt.xlabel("Число ребер")
    plt.ylabel("Время")
    plt.show()

elif mode == 6:
    with open('4(a).txt', 'r') as input_file:
        d_y, fb_y = [], []
        for line in input_file:
            d_y.append(float(line.split()[0]))
            fb_y.append(float(line.split()[1]))
    x = [i for i in range(1, 201)]
    plt.scatter(x, d_y, c='g')
    plt.scatter(x, fb_y, c='r')
    plt.annotate('''
       $q=1$
       $m=n^2$
       $n=10^4+1$
       ''', xy=(150, 20))
    fig1 = plt.figure(1)
    fig1.text(0.44, 0.95, 'алг. Дeйкстры,', color='g')
    fig1.text(0.41, 0.90, 'алг. Форда-Беллмана', color='r')
    plt.xlabel("Верхняя граница весов ребер")
    plt.ylabel("Время")
    plt.show()

elif mode == 7:
    with open('4(b).txt', 'r') as input_file:
        d_y, fb_y = [], []
        for line in input_file:
            d_y.append(float(line.split()[0]))
            fb_y.append(float(line.split()[1]))
    x = [i for i in range(1, 201)]
    plt.scatter(x, d_y, c='g')
    plt.scatter(x, fb_y, c='r')
    plt.annotate('''
       $q=1$
       $m=1000*n$
       $n=10^4+1$
       ''', xy=(0, 12))
    fig1 = plt.figure(1)
    fig1.text(0.44, 0.95, 'алг. Дeйкстры,', color='g')
    fig1.text(0.41, 0.90, 'алг. Форда-Беллмана', color='r')
    plt.xlabel("Верхняя граница весов ребер")
    plt.ylabel("Время")
    plt.show()