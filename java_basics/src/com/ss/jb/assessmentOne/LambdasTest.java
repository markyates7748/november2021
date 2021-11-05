package com.ss.jb.assessmentOne;

import static org.junit.Assert.*;

import org.junit.Test;

public class LambdasTest {
	
	@Test
	public void testIsOdd() {
		assertTrue(Lambdas.lambdaFunc(1, Lambdas.isOdd));
		assertFalse(Lambdas.lambdaFunc(2, Lambdas.isOdd));
	}
	
	@Test
	public void testIsPrime() {
		assertTrue(Lambdas.lambdaFunc(3, Lambdas.isPrime));
		assertFalse(Lambdas.lambdaFunc(4, Lambdas.isPrime));
	}
	
	@Test
	public void testIsPalindrome() {
		assertTrue(Lambdas.lambdaFunc(121, Lambdas.isPalindrome));
		assertFalse(Lambdas.lambdaFunc(123, Lambdas.isPalindrome));
	}

}
