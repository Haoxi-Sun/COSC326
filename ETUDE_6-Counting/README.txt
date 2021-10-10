Elsie Sun 4468203
Ella Ji 2854080

Run this program: javac CountingIt.java
	              java CountingIt

Notes: If the user type larger numbers, and the result is larger than 64 bits, an error should be happened because overflow, so when overflow happens, the program will shows "Data overflow".
           The idea is shows in README.jpg, which explains my idea with an example.

In this program, we try to make all numbers in the denominator to be 1,

For example:

        46!                      42*43*44*45*46          23*3*11*43*42

    ——————= ——————————=——————————

         5!(46-5)!                1*2*3*4*5
                     
1*1*1*1*1
  
We need to makes 2, 3, 4, 5 in the denominator to be 1, like 1*1*1*1*1, and then we can calculate all numbers in the numerator, and get a result.

In math, the prime numbers 2, 3, and 5 only can be divisible by itself and 1, which is very important!
 
Firstly, all even numbers can be divisible by 2, which means all numbers ending in 2, 4, 6, 8, or 0, which they can be divisible by 2, such as 50, 144, 456, 458, 192.

Furthermore, a number, its digits add up to 3, 6, 9, or multiple of 3, 6, or 9, and it must be divisible by 3, such as 21, 651, 81, 9216.

After that the last prime number 5, all numbers ending in 5 or 0, they can be divisible by 5 as well, such as 95, 155, 205, 600.

So that we know the most numbers can be divisible by these three prime numbers( 2, 3, 5), sure, still have some numbers cannot divisible by 2, 3, or 5, such as 7, 11, 13, 17, and other prime numbers, and then we make to divisible the number by itself in the denominator and get 1 in the denominator as well.

Besides, If you like, we can take more prime numbers in this program, but the most of numbers can be divisible by prime numbers 2, 3, and 5, so I think three prime numbers are enough.
