#include "Rational.h"

namespace cosc326 {

	Rational::Rational() {
		sign = 1;
		a = Integer("0");
		b = Integer("1");
	}

	// for read the data, if there has '/' or '.' we should make the data to different part
	// and then for calculate
	void Rational::setData(std::string data) {
		sign = 1;

		// initialize
		int indexOfDot = -1;
		int indexOfSep = -1;

		for (size_t i = 0; i < data.size(); i++) {
			// if there is a '/' in the data string
			// take the index where is '/' into indexOfSep
			if (data[i] == '/') {
				indexOfSep = i;
			}

			// if there is a '.' in the data string
			// take the index where is '.' into indexOfDot
			if (data[i] == '.') {
				indexOfDot = i;
			}
		}

		// if there is not '.' in the data string
		if (indexOfDot == -1) {
			// if '/' is in the data string
			if (indexOfSep != -1) {

				a = Integer(data.substr(0, indexOfSep)); // take a part before '/' in the data string
				b = Integer(data.substr(indexOfSep + 1, data.size() - indexOfSep - 1)); // take a part after '/' in the data string

				//std::cout << a << " " << b << "\n";
				// if '/' is not in the data string
				// do it as an integer number
			} else {
				a = Integer(data); 
				b = Integer("1");
				//std::cout << a << " " << b << "\n";
			}

			// if there is '.' in the data string
		} else {
			Integer zero("0");
			// check whether or not the number before the decimal point is less than zero
			Integer w(data.substr(0, indexOfDot));
			if(w < zero){
				w = -w;
				sign = -1;
			}
			
			a = Integer(data.substr(indexOfDot + 1, indexOfSep - indexOfDot)); // take a number between '.' and '/'
			b = Integer(data.substr(indexOfSep + 1, data.size() - indexOfSep - 1)); // take a number after the '/' symbol

			//std::cout << w << " " << a << " " << b << "\n";
			
			//std::cout << data << ": " << w << " " << a << " " << b << " " << a.gcd(a, b) << "\n";

			Integer i = a;
			
			// while the number in the data string is decimal
			// times 10 for each number
			// for example:  3.2 / 2 -> 32/20 
			while(i > Integer(0)){
				w = w * Integer(10);
				b = b * Integer(10);

				i /= Integer(10);
				//std::cout << i << "\n";
			}
			a = w + a;

			//std::cout << w << " " << a << " " << b << " " << a.gcd(a, b) << "\n";
			
			if(sign == -1){
				a = -a; // change to negative number
			}

			//std::cout << w << " " << a << " " << b << " " << a.gcd(a, b) << "\n";
		}

		// reduction of fraction
		this->normalize();
		//std::cout << " " << a << " " << b << " " << a.gcd(a, b) << "\n";
	}
	
	// read data as a string
	Rational::Rational(std::string data) {
		setData(data);
	}

	//streaming insertion operator: <<
	std::ostream& operator<<(std::ostream& os, const Rational& r) {
		
		// a > b
		if (r.a > r.b) {
			// negative
			if (r.sign == -1) {
				os << "-";
			}

			Integer one("1");
			// if b == 1
			if (r.b == one) {
				os << r.a;
			// if b != 1
			} else {

				Integer whole = r.a / r.b;
				Integer mod = r.a % r.b;

				os << whole << "." << mod << "/" << r.b;
			}
		// a < b
		} else {
			// negative
			if (r.sign == -1) {
				os << "-";
			}

			Integer one("1");
			// if b == 1
			if (r.b == one) {
				os << r.a;
			// if b != 1
			} else {
				os << r.a << "/" << r.b;
			}
		}
		return os;
	}
	
	// streaming extraction operator: >>
	std::istream& operator>>(std::istream& is, Rational& r) {
		std::string data;
		is >> data;
		r.setData(data);

		return is;
	}
	
	// execute reduction of fraction
	void Rational::normalize() {
		Integer zero; // 0

		sign = 1; // positive by default
		
		// if a is smaller than 0
		if (a < zero) {
			sign *= -1;
			a = -a;
		}

		// if b is smaller than 0
		if (b < zero) {
			sign *= -1;
			b = -b;
		}
		
		// get the greatest common divisor of two integers
		Integer g = a.gcd(a, b);
		Integer one("1");
		// execute reduction of fraction
		if (g > one) {
			a /= g;
			b /= g;
		}
		if (a == zero) {
			sign = 1;
			b = Integer("1");
		}
	}
	
	// constructors
	Rational::Rational(const Rational& r) {
		sign = r.sign;
		a = r.a;
		b = r.b;
	}

	Rational::Rational(const Integer& a) {
		sign = 1;
		this->a = a;
		b = Integer("1");
		this->normalize();
	}

	Rational::Rational(const Integer& a, const Integer b) {
		sign = 1;
		this->a = a;
		this->b = b;
		this->normalize();
	}

	Rational::Rational(const Integer& a, const Integer b, const Integer c) {
		sign = 1;
		this->a = a * c + b;
		this->b = c;
		this->normalize();
	}

	// deconstructor
	Rational::~Rational() {
	}
	// the assignment operator '='
		Rational& Rational::operator =(const Rational& r) {
		sign = r.sign;
		a = r.a;
		b = r.b;

		return *this;
	}
	// the unary operator '+'
	Rational Rational::operator +() const {
		return *this;
	}
	// the unary operator '-'
	Rational Rational::operator -() const {
		Rational r = *this;
		r.sign *= -1;
		return r;
	}
	// the binary arithmetic operatior '+'
	Rational Rational::operator +(const Rational& r) const {
		Integer down = b * r.b;
		Integer up = a * r.b + r.a * b;
		return Rational(up, down);
	}
	// the binary arithmetic operatior '-'
	Rational Rational::operator -(const Rational& r) const {
		Integer down = b * r.b;
		Integer up = a * r.b - r.a * b;
		return Rational(up, down);
	}
	// the binary arithmetic operatior '*'
	Rational Rational::operator *(const Rational& r) const {
		return Rational(a * r.a, b * r.b);
	}
	// the binary arithmetic operatior '/'
	Rational Rational::operator /(const Rational& r) const {
		return Rational(a * r.b, b * r.a);
	}
	// the compound assignment operatior '+='
	Rational Rational::operator +=(const Rational& r) {
		*this = *this + r;
		return *this;
	}
	// the compound assignment operatior '-='
	Rational Rational::operator -=(const Rational& r) {
		*this = *this - r;
		return *this;
	}
	// the compound assignment operatior '*='
	Rational Rational::operator *=(const Rational& r) {
		*this = *this * r;
		return *this;
	}
	// the compound assignment operatior '/='
	Rational Rational::operator /=(const Rational& r) {
		*this = *this / r;
		return *this;
	}
	// the comparison operatior '=='
	bool Rational::operator ==(const Rational& r) const {
		return a * r.b == r.a * b;
	}
	// the comparison operatior '!='
	bool Rational::operator !=(const Rational& r) const {
		return a * r.b != r.a * b;
	}
	// the comparison operatior '<'
	bool Rational::operator <(const Rational& r) const {
		return a * r.b < r.a * b;
	}
	// the comparison operatior '<='
	bool Rational::operator <=(const Rational& r) const {
		return a * r.b <= r.a * b;
	}
	// the comparison operatior '>'
	bool Rational::operator >(const Rational& r) const {
		return a * r.b > r.a * b;
	}
	// the comparison operatior '>='
	bool Rational::operator >=(const Rational& r) const {
		return a * r.b >= r.a * b;
	}

} /* namespace cosc326 */

