#include "Integer.h"

namespace cosc326 {
	//default constructor
	Integer::Integer() {
		sign = true;
		nums.push_back(0);
	}

	Integer::Integer(int i){
		sign = true;
		while(i > 0){
			nums.insert(nums.begin() + 0, i%10);
			i /= 10;
		}

		if(nums.size() == 0){
			nums.push_back(0);
		}
	}

	Integer Integer::abs() const {
		if (sign) {
			return *this;
		} else {
			return Integer(!sign, nums);
		}
	}

	Integer::Integer(bool sign, const std::vector<int> nums) {
		this->sign = sign;
		this->nums = nums;
	}
	//Determine the number of positive and negative by finding '+' and '-'
	void Integer::setData(std::string s) {
		if (s.size() > 0) {
			sign = true;

			for (size_t i = 0; i < s.size(); i++) {
				char ch = s[i];
				if (ch >= '0' && ch <= '9') {
					nums.push_back(ch - '0');
				} else if (i == 0 && ch == '+') {
					sign = true;
				} else if (i == 0 && ch == '-') {
					sign = false;
				}
			}
		} else {
			sign = true;
			nums.push_back(0);
		}
	}

	//set the data
	Integer::Integer(std::string s) {
		setData(s);
	}
	//copy constructor
	Integer::Integer(const Integer& integer) {
		sign = integer.sign;
		nums = integer.nums;
	}

	//streaming insertion and extraction operators: << and >>
	// execute the operator "insertion"
	std::ostream& operator<<(std::ostream& os, const Integer& integer) {
		if (!integer.sign) {
			os << "-";
		}

		for (size_t i = 0; i < integer.nums.size(); i++) {
			os << integer.nums[i];
		}
		return os;
	}
	// execute the operator "extraction"
	std::istream& operator>>(std::istream& is, Integer& integer) {
		std::string str;
		is >> str;

		integer.setData(str);
		return is;
	}
	//destructor
	Integer::~Integer(){
	}
	//the assignment operator =
	Integer& Integer::operator =(const Integer& integer) {
		sign = integer.sign;
		nums = integer.nums;
		return *this;
	}
	//the unary operator +
	Integer Integer::operator +() const {
		return Integer(sign, nums);
	}
	//the unary operator -
	Integer Integer::operator -() const {
		return Integer(!sign, nums);
	}

	//for removing the zero in the front
	std::vector<int> Integer::removeLeadingZero(const std::vector<int>& nums) const {
		std::vector<int> result;

		int start = -1;
		for (size_t i = 0; i < nums.size(); i++) {
			if (nums[i] != 0) {
				start = i;
				break;
			}
		}

		if (start == -1) {
			result.push_back(0);
		} else {
			for (size_t i = start; i < nums.size(); i++) {
				result.push_back(nums[i]);
			}
		}

		return result;
	}
	//compare the two integers
	int Integer::compare(const std::vector<int>& a,const std::vector<int>& b) const {
		if (a.size() == b.size()) {
			for (size_t i = 0; i < a.size(); i++) {
				if (a[i] > b[i]) {
					return 1;
				} else if (a[i] < b[i]) {
					return -1;
				}
			}
			return 0;
		} else {
			if (a.size() > b.size()) {
				return 1;
			} else {
				return -1;
			}
		}
	}

	std::vector<int> Integer::reverse(const std::vector<int>& nums) const {
		std::vector<int> result;
		for (int i = nums.size() - 1; i >= 0; i--) {
			result.push_back(nums[i]);
		}
		return result;
	}

	//add for addition
	//two integers a and b, wo start the calculation from last to begin
	//at the start of the calculation
	//there is an example, we have integer a = 25 and b = 25
	//more description see the code below
	//and then do the next two values with carry = 1
	//2+2+1 = 5, witch is final result
	std::vector<int> Integer::add(const std::vector<int>& a,const std::vector<int>& b) const {
		std::vector<int> result;

		int carry = 0;
		int i = a.size() - 1;
		int j = b.size() - 1;
		while (i >= 0 && j >= 0) {
			//more description:
			//at the start, the sum is equal to 10,which is 5+5+0,0 is carry at start
			//there is no remainder of sum%10, witch is v
			//and use sum/10 to get the carry value, which in this example is 1
			//and the add the value v to the result
			int sum = a[i] + b[j] + carry;
			int v = sum % 10;
			carry = sum / 10;
			result.push_back(v);

			i--;
			j--;
		}

		while (i >= 0) {
			int sum = a[i] + carry;
			int v = sum % 10;
			carry = sum / 10;
			result.push_back(v);

			i--;
		}

		while (j >= 0) {
			int sum = b[j] + carry;
			int v = sum % 10;
			carry = sum / 10;
			result.push_back(v);

			j--;
		}

		if (carry > 0) {
			result.push_back(carry);
		}

		result = reverse(result);
		return result;
	}

	//substraction
	//similar for addition, in the case, there is a value called borrow, means borrow
	//one from the last value to do the calculation
	//eg 27 - 18, in this example, 7 is less than 8, so it need to borrow 1 from 2,make itself to 17
	//and then do the substrsct 17 - 8, get the result is 9
	//and then for the next calculation, 2 is already borrowed 1 by 7 so it comes to 1
	//and do the calculation about 1 - 1 = 0, (first 1 is from 27, second 1 from 18)add this result with last result 9
	//get the final result 9 of this example 
	std::vector<int> Integer::sub(const std::vector<int>& a,const std::vector<int>& b) const {
		std::vector<int> result;

		int borrow = 0;
		int i = a.size() - 1;
		int j = b.size() - 1;
		while (i >= 0 && j >= 0) {
			int diff = a[i] - borrow - b[j];

			if (diff < 0) {
				borrow = 1;
				int v = 10 + diff;
				result.push_back(v);
			} else {
				borrow = 0;
				int v = diff;
				result.push_back(v);
			}

			i--;
			j--;
		}

		while (i >= 0) {
			int diff = a[i] - borrow - 0;

			if (diff < 0) {
				borrow = 1;
				int v = 10 + diff;
				result.push_back(v);
			} else {
				borrow = 0;
				int v = diff;
				result.push_back(v);
			}

			i--;
		}

		result = reverse(result);
		result = removeLeadingZero(result);
		return result;
	}
	//the binary arithmetic operation +
	Integer Integer::operator +(const Integer& integer) const {
		if ((sign && integer.sign) || (!sign && !integer.sign)) {
			std::vector<int> nums_result = add(nums, integer.nums);
			//std::cout << "size: " << nums_result.size() << std::endl;

			Integer result;
			if (!sign && !integer.sign) {
				result.sign = false;
			}
			result.nums = nums_result;

			if(result.nums.size()==1 && result.nums[0] == 0){
				result.sign = true;
			}
			return result;
		} else if (sign && !integer.sign) {
			return this->operator -(-integer);
		} else {
			return integer.operator -(-(*this));
		}
	}
	//the binary arithmetic operation -
	Integer Integer::operator -(const Integer& integer) const {
		if ((sign && !integer.sign)) {
			return this->operator +(-integer);
		} else if ((!sign && integer.sign)) {
			return -(integer.operator +(-(*this)));
		} else if (sign && integer.sign) {
			if (*this >= integer) {
				Integer result;
				result.sign = true;
				result.nums = sub(this->nums, integer.nums);

				return result;
			} else {
				Integer result;
				result.sign = false;
				result.nums = sub(integer.nums, this->nums);

				if(result.nums.size()==1 && result.nums[0] == 0){
					result.sign = true;
				}
				return result;
			}
		} else {
			Integer temp = -integer;
			return temp.operator -(*this);
		}
	}
	//the binary arithmetic operation *
	Integer Integer::operator *(const Integer& integer) const {
		Integer a = this->abs();
		Integer b = integer.abs();

		Integer zero;
		Integer one("1");
		//std::cout << "b: " << b << std::endl;
		Integer result;
		while (b > zero) {
			result += a;
			b -= one;

			//std::cout << "b: " << b << std::endl;
			//std::cout << "result: " << result << std::endl;
		}

		if (sign && integer.sign) {
			return result;
		} else if (!sign && !integer.sign) {
			return result;
		} else {
			if(result.nums.size()==1 && result.nums[0] == 0){
				return result;
			}else{
				result.sign = false;
				return result;
			}
		}
	}
	//the binary arithmetic operation /
	Integer Integer::operator /(const Integer& integer) const {

		Integer result; // store the result
		Integer temp; // store the mediam

		// clear
		result.nums.clear();
		temp.nums.clear();

		// set a sign
		// if two signs are same, is positive
		// otherwise, negative
		result.sign = this->sign && integer.sign;

		// absloute value for division
		Integer a = this->abs();
		Integer b = integer.abs();

		// execute division
		// for example, 175/6, execute 17/6=2...5, and then 55/6=9...1, so the result is 59
		for (int i = 0, k = 0; i < a.nums.size(); i++) {
			temp.nums.push_back(a.nums[i]);
			if (temp >= b) {
				int r = 0;
				while (temp >= b) {
					temp = temp - b;
					r++;
				}
				result.nums.push_back(r);
			}
		}
		return result;
	}


	//the binary arithmetic operation %
	Integer Integer::operator %(const Integer& integer) const {
		Integer iabs = integer.abs();

		Integer result = this->abs();
		while (result >= iabs) {
			result -= iabs;
		}

		if (sign && integer.sign) {
			return result;
		} else if (!sign && !integer.sign) {
			return result;
		} else {
			if(result.nums.size()==1 && result.nums[0] == 0){
				return result;
			}else{
				result.sign = false;
				return result;
			}
		}
	}
	//the compound assigment operators +=
	Integer Integer::operator +=(const Integer& integer) {
		Integer result = *this + integer;
		this->sign = result.sign;
		this->nums = result.nums;
		return result;
	}
	//the compound assigment operators -=
	Integer Integer::operator -=(const Integer& integer) {
		Integer result = *this - integer;
		this->sign = result.sign;
		this->nums = result.nums;
		return result;
	}
	//the compound assigment operators *=
	Integer Integer::operator *=(const Integer& integer) {
		Integer result = *this * integer;
		this->sign = result.sign;
		this->nums = result.nums;
		return result;
	}
	//the compound assigment operators /=
	Integer Integer::operator /=(const Integer& integer) {
		Integer result = *this / integer;
		this->sign = result.sign;
		this->nums = result.nums;
		return result;
	}
	//the compound assigment operators %=
	Integer Integer::operator %=(const Integer& integer) {
		Integer a = this->abs();
		while (a > integer) {
			a -= integer;
		}

		a.sign = sign;
		return a;
	}
	//the comparison operator ==
	bool Integer::operator ==(const Integer& integer) const {
		return compare(nums, integer.nums) == 0 && sign == integer.sign;
	}
	//the comparison operator !=
	bool Integer::operator !=(const Integer& integer) const {
		return !this->operator ==(integer);
	}
	//the comparison operator <
	bool Integer::operator <(const Integer& integer) const {
		if (sign && integer.sign) {
			return compare(nums, integer.nums) < 0;
		} else if (!sign && !integer.sign) {
			return compare(nums, integer.nums) > 0;
		} else if (sign && !integer.sign) {
			return false;
		} else {
			return true;
		}
	}
	//the comparison operator <=
	bool Integer::operator <=(const Integer& integer) const {
		return *this < integer || *this == integer;
	}
	//the comparison operator >
	bool Integer::operator >(const Integer& integer) const {
		return !(*this < integer) && *this != integer;
	}
	//the comparison operator >=
	bool Integer::operator >=(const Integer& integer) const {
		return !(*this < integer);
	}


	//A function returns the greatest common divisor of two integers
	Integer Integer::gcd(const Integer& integer1, const Integer& integer2) const{
		if(integer2 == Integer("0")) {
			return integer1;
		}
		return gcd(integer2, integer1 % integer2);
	}


} /* namespace cosc326 */