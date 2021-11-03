#!/usr/bin/env python3
import matplotlib.pyplot as plt
from integer import Integer
from time import perf_counter as pc

def fib_py(i):
	if i <= 1:
		return i
	else:
		return(fib_py(i-1) + fib_py(i-2))


def main():
	f = Integer(30)
	#print(f.get())
	#f.set(7)
	#print(f.get())
	measured_n =[]
	times_cpp = []
	times_py =	[]
	n1=30
	n=46
	for i in range(n1,n):
		start_p = pc()
		fibo_py = fib_py(i)
		end_p =pc()
		t_p =round(end_p-start_p,4)
		times_py.append(t_p)
		print(f'FIB Python for: {i} took {t_p} sec; Result:{fibo_py}')

		start_cpp = pc()
		f.set(i)
		fibo_cpp = i.fib()
		end_cpp =pc()
		t_cpp=round(end_cpp-start_cpp,4)
		times_cpp.append(t_cpp)
		print(f'FIB C++ for: {i} took {t_cpp} sec; Result:{fibo_cpp}')

		measured_n.append(i)
	
	plt.title('Fib times Python vs C++')
	plt.xlabel('n')
	plt.ylabel('time in sec')
	plt.plot(measured_n,times_py, 'b-',measured_n,times_cpp,'g-')
	plt.savefig('Times_MA4')
	
	f.set(47)
	fib_47 = f.fib_cpp()
	print(f'FIB c++ of 47: {fib_47}')


if __name__ == '__main__':
	main()