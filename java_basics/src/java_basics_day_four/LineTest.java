package java_basics_day_four;

import static org.junit.Assert.*;

import org.junit.Test;

public class LineTest {

	@Test
	public void testGetSlope() {
		Line line1 = new Line(1, 3, 3, 9);
		assertEquals(line1.getSlope(), 3, .0001);
		assertNotEquals(line1.getSlope(), 1, .0001);
	}
	
	@Test
	public void testGetDistance() {
		Line line1 = new Line(1, 3, 3, 9);
		assertEquals(line1.getDistance(), Math.sqrt(40), .0001);
		assertNotEquals(line1.getDistance(), 1, .0001);
	}
	
	@Test
	public void testParallelTo() {
		Line line1 = new Line(1, 3, 3, 9);
		Line line1Par = new Line(2, 4, 4, 10);
		Line line1NotPar = new Line(9, 3, 3, 1);
		assertTrue(line1.parallelTo(line1Par));
		assertFalse(line1.parallelTo(line1NotPar));
	}

}
