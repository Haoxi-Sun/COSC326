import java.util.Scanner;
/**
 * Author: Elsie Sun & Ella Ji
 * the combination found from
 * https://en.wikipedia.org/wiki/Combination
 */
public class CountingIt{
    private static long[] numerator;
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        while(scan.hasNextLine() && scan.hasNext()){
            Long n = scan.nextLong();
            Long k = scan.nextLong();
            // the integer numbers n and k must be positive
            if(n < 0 || k < 0){
                System.out.println("The integer N or K must be positive");
                break;
            }else if(n != 0 && k != 0){
                countAll(n, k);
            }
        }
    }
    /**
     * create an numerator list for storing values from n to (n-k+1)
     * and then divides the denominator
     * and then, values at primes 2,3, and 5 and cancels them out from the numerator
     * choose primes 2, 3, 5, because they the most numbers can be divided by one of them
     * also if a number cannot be divided by 2/3/5
     * choose to divided itself in the denominator if a numerator can be divided it as well
     * @param n n must be bigger than or equals k
     * @param k k must be bigger than or equals zero
     */
    private static void countAll(long n, long k){
        numerator = new long[(int)k];
        long total = 0;
        for(int i = 0; i < k; i++) numerator[i] = n-i;
        
        for(int i = 2; i <= k; i++){
            int num = i;
            // if one of numbers in denominator can be divided by 2, and the remainder is 0
            // try to traverse all numbers in the numberator
            // if one of numbers in the numberator can be divided by 2, and the remainder is 0 as well
            // which two numbers can be deleted, just replace numbers by 1
            while(num != 0 & num %2 == 0){
                num /= 2;
                for (int j = 0; j < numerator.length; j++) {
                    if (numerator[j] % (long)2 == 0) {
                        numerator[j] /= (long)2;
                        break;
                    }
                }
            }
             // if one of numbers in denominator can be divided by 3, and the remainder is 0
            // try to traverse all numbers in the numberator
            // if one of numbers in the numberator can be divided by 3, and the remainder is 0 as well
            // which two numbers can be deleted, just replace numbers by 1
            while(num != 0 & num %3 == 0){
                num /= 3;
                for (int j = 0; j < numerator.length; j++) {
                    if (numerator[j] % (long)3 == 0) {
                        numerator[j] /= (long)3;
                        break;
                    }
                }
            }
            // if one of numbers in denominator can be divided by 5, and the remainder is 0
            // try to traverse all numbers in the numberator
            // if one of numbers in the numberator can be divided by 5, and the remainder is 0 as well
            // which two numbers can be deleted, just replace numbers by 1
            while(num != 0 & num %5 == 0){
                num /= 5;
                for (int j = 0; j < numerator.length; j++) {
                    if (numerator[j] % (long)5 == 0) {
                        numerator[j] /= (long)5;
                        break;
                    }
                }
            }
            // if one of numbers in denominator is bigger than 1, and can not divided by 2, 3, 5, and the remainder is not 0
            // try to traverse all numbers in the numberator
            // if one of numbers in the numberator can be divided by 2, and the remainder is 0 as well
            // which two numbers can be deleted, just replace numbers by 1
            if (num>1){
                for (int j = 0; j < numerator.length; j++) {
                    if (numerator[j] % (long)num == 0) {
                        numerator[j] /= (long)num;
                        break;
                    }
                }
            }
        }
        total += numerator[0];
        for(int p =1; p<k; p++) total *= numerator[p];
        if (total < 0) System.out.println("Data Overflow");
        else System.out.println(total);
    }
}