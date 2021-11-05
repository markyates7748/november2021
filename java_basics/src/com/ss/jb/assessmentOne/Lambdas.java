package com.ss.jb.assessmentOne;

public class Lambdas {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(lambdaFunc(1, isOdd));

	}
	
	static public Boolean lambdaFunc(int a, PerformOperation lambdaOperation) {
		return lambdaOperation.operation(a);
	}
	
	static PerformOperation isOdd = (a) -> {
		return (a % 2 == 0) ? false : true;
	};
	
	static PerformOperation isPrime = (a) -> {
		for(int i = 2; i < a; i++) {
			if(a % i == 0) {
				return false;
			}
		}
		return true;
	};
	
	static PerformOperation isPalindrome = (originalNumber) -> {
		int remainder;
		int reversed = 0;
		int tempOriginal = originalNumber;
		while(tempOriginal != 0) {
			remainder = tempOriginal % 10;
			reversed = (reversed * 10) + remainder;
			tempOriginal /= 10;
		}
		return (originalNumber == reversed) ? true : false;
	};

}
