from algorithm import generator, converter, dijkstra, ford_bellman
from time import time
file_1 = open('1(a).txt', 'w')
file_2 = open('1(b).txt', 'w')
file_3 = open('2(a).txt', 'w')
file_4 = open('2(b).txt', 'w')
file_5 = open('3.txt', 'w')
file_6 = open('4(a).txt', 'w')
file_7 = open('4(b).txt', 'w')

for vertex_count in range(1, 10**4 + 2, 100):
    p = 0.2
    edges = generator(p, vertex_count, 1, 10**6)
    adj_matrix = converter(edges, vertex_count)
    d_start = time()
    d = dijkstra(adj_matrix, 0, vertex_count)
    d_end = time() - d_start
    fb_start = time()
    fb = ford_bellman(edges, 0, vertex_count)
    fb_end = time() - fb_start
    file_1.write(str(d_end) + ' ' + str(fb_end) + ' ' + str(vertex_count) + '\n')
    print(vertex_count, 1)

for vertex_count in range(1, 10**4 + 2, 100):
    p = 0.95
    edges = generator(p, vertex_count, 1, 10**6)
    adj_matrix = converter(edges, vertex_count)
    d_start = time()
    d = dijkstra(adj_matrix, 0, vertex_count)
    d_end = time() - d_start
    fb_start = time()
    fb = ford_bellman(edges, 0, vertex_count)
    fb_end = time() - fb_start
    file_2.write(str(d_end) + ' ' + str(fb_end) + ' ' + str(vertex_count) + '\n')
    print(vertex_count, 2)

for vertex_count in range(101, 10**4 + 2, 100):
    p = 200 / vertex_count
    edges = generator(p, vertex_count, 1, 10**6)
    adj_matrix = converter(edges, vertex_count)
    d_start = time()
    d = dijkstra(adj_matrix, 0, vertex_count)
    d_end = time() - d_start
    fb_start = time()
    fb = ford_bellman(edges, 0, vertex_count)
    fb_end = time() - fb_start
    file_3.write(str(d_end) + ' ' + str(fb_end) + ' ' + str(vertex_count) + '\n')
    print(vertex_count, 3)

for vertex_count in range(101, 10**4 + 2, 100):
    p = 2000 / vertex_count
    edges = generator(p, vertex_count, 1, 10**6)
    adj_matrix = converter(edges, vertex_count)
    d_start = time()
    d = dijkstra(adj_matrix, 0, vertex_count)
    d_end = time() - d_start
    fb_start = time()
    fb = ford_bellman(edges, 0, vertex_count)
    fb_end = time() - fb_start
    file_4.write(str(d_end) + ' ' + str(fb_end) + ' ' + str(vertex_count) + '\n')
    print(vertex_count, 4)

for edges_count in range(10**5, 10**7 + 1, 10**5):
     p = (2 * edges_count) / (10**8 + 10**4)
     vertex_count = 10**4 + 1
     edges = generator(p, vertex_count, 1, 10**6)
     adj_matrix = converter(edges, vertex_count)
     d_start = time()
     d = dijkstra(adj_matrix, 0, vertex_count)
     d_end = time() - d_start
     fb_start = time()
     fb = ford_bellman(edges, 0, vertex_count)
     fb_end = time() - fb_start
     file_5.write(str(d_end) + ' ' + str(fb_end) + ' ' + str(edges_count) + '\n')
     print(edges_count, 5)

for q in range(1, 201, 1):
    p = 0.95
    vertex_count = 10 ** 4 + 1
    edges = generator(p, vertex_count, 1, q)
    adj_matrix = converter(edges, vertex_count)
    d_start = time()
    d = dijkstra(adj_matrix, 0, vertex_count)
    d_end = time() - d_start
    fb_start = time()
    fb = ford_bellman(edges, 0, vertex_count)
    fb_end = time() - fb_start
    file_6.write(str(d_end) + ' ' + str(fb_end) + ' ' + str(q) + '\n')
    print(q, 6)

for q in range(1, 201, 1):
    p = 0.2
    vertex_count = 10 ** 4 + 1
    edges = generator(p, vertex_count, 1, q)
    adj_matrix = converter(edges, vertex_count)
    d_start = time()
    d = dijkstra(adj_matrix, 0, vertex_count)
    d_end = time() - d_start
    fb_start = time()
    fb = ford_bellman(edges, 0, vertex_count)
    fb_end = time() - fb_start
    file_7.write(str(d_end) + ' ' + str(fb_end) + ' ' + str(q) + '\n')
    print(q, 7)
