#ifndef RATIONAL_H_
#define RATIONAL_H_

#include "Integer.h"

namespace cosc326 {

	class Rational {
	private:
		Integer a;
		Integer b;
		int sign;
	private:
		void normalize();
		void setData(std::string data);
	public:
		//default constructor that creates Rational with a value of 0
		Rational();

		//copy constructor that duplicates the provided Rational
		Rational(const Rational& r);

		//Constructors taking one, two, or three Integers
		Rational(const Integer& a);
		Rational(const Integer& a, const Integer b);
		Rational(const Integer& a, const Integer b, const Integer c);
		
		//constructor that takes a std::string parameters.
		Rational(std::string data);
		~Rational();

		//assignment operator: =
		Rational& operator=(const Rational& r); // =r

		//override operators
		//unary operators: + and -
		Rational operator+() const; // +r
		Rational operator-() const; // -r

		//binary arithmetic operators: +, -, *, /, and %
		Rational operator+(const Rational& r) const; // binary +r
		Rational operator-(const Rational& r) const; // binary -r
		Rational operator*(const Rational& r) const; // binary *r
		Rational operator/(const Rational& r) const; // binary /r

		//compound assignment operators: +=, -=, *=, /=, and %=
		Rational operator+=(const Rational& r); // += r
		Rational operator-=(const Rational& r); // -= r
		Rational operator*=(const Rational& r); // *= r
		Rational operator/=(const Rational& r); // /= r

		//comparison operators: ==, !=,<,<=,>, and >=
		bool operator==(const Rational& r) const; // == r
		bool operator!=(const Rational& r) const; // != r
		bool operator<(const Rational& r) const; // < r
		bool operator<=(const Rational& r) const; // <= r
		bool operator>(const Rational& r) const; // > r
		bool operator>=(const Rational& r) const; // >= r

		//streaming insertion and extraction operators: << and >>
		// 'friend' for protecting these two functions
		friend std::ostream& operator<<(std::ostream& os, const Rational& r); // std::cout << r << std::endl
		friend std::istream& operator>>(std::istream& is, Rational& r); // std::cin >> r

	};

} /* namespace cosc326 */

#endif /* RATIONAL_H_ */
