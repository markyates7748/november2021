/**
 * 
 */
package java_basics_day_five;

import java.time.*;

/**
 * @author myate
 *
 */
public class DateAndTimeDemo {
	
	//Class to store birthday in years/months/days/seconds/nanoseconds
	private LocalDateTime birthday = LocalDateTime.of(1990, Month.JANUARY, 1, 12, 30);
	
	//Find previous Thursday of a random date
	static public LocalDate previousThursday(LocalDate randomDate) {
		do {
			randomDate = randomDate.minusDays(1);
		} while(randomDate.getDayOfWeek() != DayOfWeek.THURSDAY);
		return randomDate;
	}
	
	//ZoneId or ZoneOffset
	/**
	 * ZoneId includes an identifier for a time zone and rules for converting
	 *  between and Instant and a LocalDiteTime
	 *  
	 * ZoneOffset gives the time offset from the UTC time zone 
	 */
	
	//Convert Instant to ZonedDateTime and ZonedDateTime to Instant
	/**
	 * The Instant class includes a method named .atZone() which takes a ZoneId
	 * object of the desired time zone which can be called on the Instant object
	 * and returns a ZonedDateTime object
	 * 
	 * The ZonedDateTime class inherits a method named .toInstant() that may be
	 * called on the ZonedDateTime object and returns an Instant object
	 */
	
	//Report length of months in given year
	static public void monthLength(int givenYear) {
		LocalDate adjustedYear = LocalDate.of(givenYear, Month.JANUARY, 1);
		while(adjustedYear.getMonth() != Month.DECEMBER) {
			System.out.println("Length of " + adjustedYear.getMonth() + ": " + adjustedYear.lengthOfMonth());
			adjustedYear = adjustedYear.plusMonths(1);
		}
		
	}
	
	//List all Mondays for given month in current year
	static public void listAllMondays(Month givenMonth) {
		LocalDate tempName = LocalDate.of(LocalDate.now().getYear(), givenMonth, 1);
		int i = 1;
		while(i <= tempName.lengthOfMonth()) {
			if(tempName.getDayOfWeek() == DayOfWeek.MONDAY) {
				System.out.println(tempName);
			}
			tempName = tempName.plusDays(1);
			i++;
		}
		
	}
	
	//Test if given date occurs on Friday the 13th
	static public void checkFriday13(LocalDate checkMe) {
		if(checkMe.getDayOfMonth() == 13 && checkMe.getDayOfWeek() == DayOfWeek.FRIDAY) {
			System.out.println("Given date falls on Friday the 13th");
		}else {
			System.out.println("Given date does not fall on Friday the 13th");
		}
	}

}
