
#include <stdio.h>

#include <stack>
class MyQueue {
public:
    MyQueue() {
    }
    void push(int x) {
    	_input.push(x);
    }
    int pop() {
    	adjust();
    	int x = _output.top();
    	_output.pop();
        return x;
    }
    int peek() {
    	adjust();
        return _output.top();
    }
    bool empty() {
        return _input.empty() && _output.empty();
    }
private:
	void adjust(){
		if (!_output.empty()){
			return;
		}
		while(!_input.empty()){
			_output.push(_input.top());
			_input.pop();
		}
	}
	std::stack<int> _input;
	std::stack<int> _output;
};

int main(){
	MyQueue Q;
	Q.push(1);
	Q.push(2);
	Q.push(3);
	Q.push(4);
	printf("%d\n", Q.peek());
	Q.pop();
	printf("%d\n", Q.peek());	
	return 0;
}
