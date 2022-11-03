#No esta funcionando el codigo aqui, pero el codigo esta bueno
import wikipedia as wp

res1 = wp.search('python',results=3,suggestion=True)
res2 = wp.summary('python')
print(res1)
print(res2)