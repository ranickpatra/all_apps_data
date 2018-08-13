#include <iostream>
#include <stdlib.h>
#include <string.h>


using namespace std;


class Stack
{
	private:
		char *data;
		int top, max_size;
	
	public:
		void init(int len)
		{
			data = (char *) malloc(len);
			top = -1;
			max_size = len;
		}
		
		
		void push(char data)
		{
			if(top >= max_size-1)
				return;
				
			this->data[++top] = data;
		}
		
		char pop()
		{
			if(is_empty())
				return '\0';
			
			
			return data[top--];
		}
		
		
		bool is_empty()
		{
			if(top == -1)
				return true;
			else
				return false;
		}
		
		int get_top()
		{
			return top;
		}
		
		
		
};

class Validation : Stack
{
	public:
		void init(char *data)
		{
			int len = strlen(data);
			length = len;
			inp_str = (char *) malloc(len);
			this->inp_str = data;
			Stack::init(len);
			
		}
		
		
		bool is_valid()
		{
			for(int i = 0; i < length; i++)
			{
				if(inp_str[i] == '(')
				{
					this->push(inp_str[i]);
				}
				else if(inp_str[i] == ')')
				{
					if(!this->is_empty())
						this->pop();
					else
						return false;
				}
				else if(is_in_operators(inp_str[i]))
				{
					if(i == length-1)
						return false;
					else if(i == 0)
						return false;
					else if(inp_str[i+1] == ')')
						return false;
					else if(is_in_operators(inp_str[i+1]))
					return false;
					
				}
				
			
			}
			
			if(get_top() != -1)
				return false;
				
			return true;
		}
		
		bool is_in_operators(char ch)
		{
			int l = strlen(opert);
			for (int i=0; i<l; i++)
			{
				if(opert[i] == ch)
					return true;
			}
			
			return false;
		}
		
		
		
	private:
		char *inp_str;
		int length;
		char *opert= "+-*/^";
};



int main()
{

	Validation v;
	char inp_data[100];
	cin >> inp_data;
	v.init(inp_data);
	
	
	if(v.is_valid())
		cout << "Valid" << endl;
	else
		cout << "not valid" << endl;
	

	
	
}
