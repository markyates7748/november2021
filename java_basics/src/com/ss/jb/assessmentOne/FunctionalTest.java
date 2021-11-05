package com.ss.jb.assessmentOne;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Arrays;
import org.junit.jupiter.api.Test;

class FunctionalTest {

	@Test
	void testRightDigit() {
		Functional func = new Functional();
		assertEquals(func.rightDigit(Arrays.asList(1,22,93)), Arrays.asList(1,2,3));
	}

	@Test
	void testDoubling() {
		Functional func = new Functional();
		assertEquals(func.doubling(Arrays.asList(1,22,93)), Arrays.asList(2,44,186));
	}

	@Test
	void testNoX() {
		Functional func = new Functional();
		assertEquals(func.noX(Arrays.asList("xeno","rax","axe")), Arrays.asList("eno","ra","ae"));
	}

}
