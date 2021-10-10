#ifndef INTEGER_H_
#define INTEGER_H_

#include <vector>
#include <string>
#include <iostream>

namespace cosc326 {

	class Integer {
	private:
		bool sign;
		std::vector<int> nums;

	private:
		Integer(bool sign, const std::vector<int> nums);
		Integer abs() const;
		void setData(std::string);
		std::vector<int> removeLeadingZero(const std::vector<int>& nums) const;
		std::vector<int> reverse(const std::vector<int>& nums) const;
		int compare(const std::vector<int>& a, const std::vector<int>& b) const;
		std::vector<int> add(const std::vector<int>& a, const std::vector<int>& b) const;
		std::vector<int> sub(const std::vector<int>& a, const std::vector<int>& b) const; //assume a > b
	public:
		Integer();

		Integer(int i);

		Integer(std::string);

		//copy constructor
		Integer(const Integer& integer);

		~Integer();

		//assignment operator: =
		Integer& operator=(const Integer& integer);	// j = i

		//override operators
		//unary operators: + and -
		Integer operator+() const; 	//-j
		Integer operator-() const;	//+j

		//binary arithmetic operators: +, -, *, /, and %
		Integer operator+(const Integer& integer) const;
		Integer operator-(const Integer& integer) const;
		Integer operator*(const Integer& integer) const;
		Integer operator/(const Integer& integer) const;
		Integer operator%(const Integer& integer) const;

		//compound assignment operators: +=, -=, *=, /=, and %=
		Integer operator+=(const Integer& integer);
		Integer operator-=(const Integer& integer);
		Integer operator*=(const Integer& integer);
		Integer operator/=(const Integer& integer);
		Integer operator%=(const Integer& integer);

		//comparison operators: ==, !=,<,<=,>, and >=
		bool operator==(const Integer& integer) const;
		bool operator!=(const Integer& integer) const;
		bool operator<(const Integer& integer) const;
		bool operator<=(const Integer& integer) const;
		bool operator>(const Integer& integer) const;
		bool operator>=(const Integer& integer) const;

		//streaming insertion and extraction operators: << and >>
		friend std::ostream& operator<<(std::ostream& os, const Integer& integer); 	// std::cout << i << std::endl;
		friend std::istream& operator>>(std::istream& is, Integer& integer);		// std::cin >> i;

		//returns the greatest common divisor of two Integers
		Integer gcd(const Integer& integer1, const Integer& integer2) const;
	};

} /* namespace cosc326 */

#endif /* INTEGER_H_ */
