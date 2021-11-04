package java_basics_day_five;

import static org.junit.Assert.fail;
import static org.junit.jupiter.api.Assertions.*;

import java.time.LocalDate;
import java.time.Month;

import org.junit.jupiter.api.Test;

public class DateAndTimeDemoTest {

	@Test
	public void testPreviousThursday() {
		System.out.println(DateAndTimeDemo.previousThursday(LocalDate.parse("2007-12-03")));
		fail("Not yet implemented");
	}
	
	@Test
	public void testMonthLength() {
		DateAndTimeDemo.monthLength(2000);
		fail("Not yet implemented");
	}
	
	@Test
	public void testListAllMondays() {
		DateAndTimeDemo.listAllMondays(Month.NOVEMBER);
		fail("Not yet implemented");
	}
	
	@Test
	public void testCheckFriday13() {
		DateAndTimeDemo.checkFriday13(LocalDate.parse("2021-08-13"));
		fail("Not yet implemented");
	}

}
