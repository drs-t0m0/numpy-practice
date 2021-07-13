import numpy as np

a = np.random.randn(3, 4)

np.savetxt('sample.txt', a)
b = np.loadtxt('sample.txt')
print(a)
print("-" * 30)
print(b)
print("-" * 30)

# csv形式でも対応してる
np.savetxt('sample.csv', a)
c = np.loadtxt('sample.csv')
print(c)
print("-" * 30)

# dat形式でも大丈夫
np.savetxt('sample.dat', a)
d = np.loadtxt('sample.dat')
print(d)
print("#" * 30)

np.savetxt('sample2.txt', a, delimiter=',')
e = np.loadtxt('sample2.txt', delimiter=',')
print(e)
print("#" * 30)

np.savetxt('sample3.txt', a, fmt='%.2e')
np.savetxt('sample4.txt', a, fmt='%.2f')

f = np.array([[10.1 + 3.21j, 100 + 32.1j], [20.0 + 0.2j, 22.1 - 1j]])
np.savetxt('sample6.txt', f, fmt=['%.3e + %.3ej', '%.1e + %.1ej'])

# 0,2列目だけを使う。
print(np.loadtxt('sample4.txt', usecols=(0, 2)))
print("-" * 30)

# 0行目をとばす
print(np.loadtxt('sample4.txt', skiprows=1))
print("#" * 30)

np.savetxt('sample7.txt', a, fmt='%.3e', header='this is a header', footer='this is a footer')
np.savetxt('sample8.txt', a, fmt='%.3e', header='this is a header', footer='this is a footer', comments='>>>')

print(np.loadtxt('sample8.txt', comments='>>>'))
print("#" * 30)

# 8バイトのint、10バイトのstr, 8バイトのfloat,10バイトのstrの順に指定している
print(np.loadtxt('foo.csv', dtype=[('col1', 'i8'), ('col2', 'S10'), ('col3', 'f8'), ('col4', 'S10')]))
print("#" * 30)

print(np.loadtxt('foo.csv', dtype=[('col1', 'i8'), ('col2', 'S10'), ('col3', 'f8'), ('col4', 'S10')], unpack=True))
print("#" * 30)

age, gender, tall, driver_lisense = np.loadtxt('foo.csv',
                                               dtype=[('col1', 'i8'), ('col2', 'S10'), ('col3', 'f8'), ('col4', 'S10')],
                                               unpack=True)
print(age)
print("-" * 30)
print(gender)
print("-" * 30)
print(tall)
print("-" * 30)
print(driver_lisense)
print("#" * 30)


def driver_lisense(str):
    if str == b'Yes':
        return 1
    else:
        return -1


def gender(str):
    if str == b'male':
        return 1
    else:
        return -1


print(np.loadtxt('foo.csv', converters={1: lambda s: gender(s), 3: lambda s: driver_lisense(s)}))

