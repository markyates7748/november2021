package com.ss.jb.assessmentOne;

public class Lambdas {

	public static void main(String[] args) {
		int totalTests = Integer.parseInt(args[0]);
		int i = 1;
		try {
			while (i <= (totalTests * 2)) {
				switch (Integer.parseInt(args[i])) {
				case 1:
					if (lambdaFunc(Integer.parseInt(args[i + 1]), isOdd)) {
						System.out.println("ODD");
					} else {
						System.out.println("EVEN");
					}
					break;
				case 2:
					if (lambdaFunc(Integer.parseInt(args[i + 1]), isPrime)) {
						System.out.println("PRIME");
					} else {
						System.out.println("COMPOSITE");
					}
					break;
				case 3:
					if (lambdaFunc(Integer.parseInt(args[i + 1]), isPalindrome)) {
						System.out.println("PALINDROME");
					} else {
						System.out.println("NONPALINDROME");
					}
					break;
				default:
					System.out.println("Invalid test type");
				}
				i += 2;
			}
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println("Input indicates more tests than provided");
		}
	}

	static public Boolean lambdaFunc(int a, PerformOperation lambdaOperation) {
		return lambdaOperation.operation(a);
	}

	static PerformOperation isOdd = (a) -> {
		return (a % 2 == 0) ? false : true;
	};

	static PerformOperation isPrime = (a) -> {
		for (int i = 2; i < a; i++) {
			if (a % i == 0) {
				return false;
			}
		}
		return true;
	};

	static PerformOperation isPalindrome = (originalNumber) -> {
		int remainder;
		int reversed = 0;
		int tempOriginal = originalNumber;
		while (tempOriginal != 0) {
			remainder = tempOriginal % 10;
			reversed = (reversed * 10) + remainder;
			tempOriginal /= 10;
		}
		return (originalNumber == reversed) ? true : false;
	};

}
