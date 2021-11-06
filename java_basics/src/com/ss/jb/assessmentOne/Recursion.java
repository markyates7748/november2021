package com.ss.jb.assessmentOne;

public class Recursion {

	public static void main(String[] args) {
		int[] intArray = { 2, 4, 4, 8 };
		int intArrayLength = intArray.length;
		int target = 14;
		System.out.print(groupSumClump(intArrayLength, intArray, target));
	}

	static public Boolean groupSumClump(int intListLength, int[] intList, int target) {
		if (target == 0) {
			return true;
		}
		if (intListLength == 0) {
			return false;
		}
		if (intListLength >= 2) {
			if (intList[intListLength - 1] == intList[intListLength - 2]) {
				return groupSumClump(intListLength - 2, intList, target) 
						|| groupSumClump(intListLength - 2, intList, 
								target - intList[intListLength - 1] - intList[intListLength - 2]);
			}
		}
		return groupSumClump(intListLength - 1, intList, target)
				|| groupSumClump(intListLength - 1, intList, target - intList[intListLength - 1]);
	}
}
