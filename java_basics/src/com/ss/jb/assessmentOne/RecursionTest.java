package com.ss.jb.assessmentOne;

import static org.junit.Assert.*;

import org.junit.Test;

public class RecursionTest {

	@Test
	public void testOne() {
		int[] intArray = {2,4,8};
		assertTrue(Recursion.groupSumClump(intArray.length, intArray, 10));
	}
	
	@Test
	public void testTwo() {
		int[] intArray = {1,2,4,8,1};
		assertTrue(Recursion.groupSumClump(intArray.length, intArray, 14));
	}
	
	@Test
	public void testThree() {
		int[] intArray = {2,4,4,8};
		assertFalse(Recursion.groupSumClump(intArray.length, intArray, 14));
	}

}
