from Quaternion import Quaternion

x = Quaternion(2,1,1,0)
y = Quaternion(1,-1,1,4)

print(x, type(x))
print(bool(y))

d = Quaternion(-3)
print(f'{d} is real = {d.is_real()}')

print(f'x-1 = {x-1}\nx+1 = {x+1}')
print(f'x*y = {x*y}\ny*x = {y*x}')
print(f'x+y = {x+y}\nx-y = {x-y}')
print(f'x/y = {x/y}\nx**2 = {x**2}\nx**-2 = {x**-2}')
print(f'x^-1 = {round(x.inverse(),4)} = ~x = {round(~x,4)}')
print(f'x.conj() = {x.conjugate()}')
print(f'x.norm() = {x.norm} = abs(x) = {abs(x)}')
print(f'x*4.1 = {x*4.1}')

h,z = +x,+x
h **= 3
z **= -3
print(f'x **= 3: {h}\nx **= -3: {z}')
x *= y
print(f'x *= y: {x}')
print(f'is_unit(y): {y.is_unit()}\nnorm(y): {y.norm}\nnormalize(y): {y.normalize()}')

print(f'h inverse_ip = {h.inverse_ip()}')
print(f'h conjugate_ip = {h.conjugate_ip()}')

c = Quaternion(seq=[1,3,7,-2])
c //= 2
print(f'x//2 : {c}\nx.norm: {c.norm}')

c = Quaternion.randint()
d = c.inverse()
print(f'c = {c}\nc^-1 = {d}\nc*d = {c*d}\nd*c = {d*c}')

x = Quaternion(1.2, 5.0, 2, -1)
y = x % 3
z = x // 3
w = x @ 3

print(f'x = {x}\nx % 3 = {y}\nx // 3 = {z}\nx @ 3 = {w}\nnorm(x @ 3) = {w.norm}')
print(f'x ~ x//3 in HP1? {x.normalize()==z.normalize()}')