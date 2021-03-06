#include <cstdlib>
// Integer class 
//Kieran checked on the 03.11.21
class Integer{
	public:
		Integer(int);
		int get();
		void set(int);
		int fib();
		int _fib(int);
	private:
		int val;
	};
 
Integer::Integer(int n){
	val = n;
	}
 
int Integer::get(){
	return val;
	}
 
void Integer::set(int n){
	val = n;
	}

int	Integer::fib(){
	return _fib(val);
	}

int Integer::_fib(int x){
	if ((x==0) || (x==1)){
		return x;}
	else{
		return _fib(x-1) + _fib(x-2);}
	}


extern "C"{
	Integer* Integer_new(int n) {return new Integer(n);}
	int Integer_get(Integer* integer) {return integer->get();}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	int Integer_fib(Integer* integer, int n) {return integer->fib();}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}