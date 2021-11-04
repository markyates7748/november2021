package java_basics_day_two;

public class Assign1 {

	public static void main(String[] args) {

		// Take values from the command line and add them together
		int sum = 0;

		for(String s : args) {
			try {
				sum += Integer.parseInt(s);
			} catch (NumberFormatException nfe) {
				System.out.printf("Input '%s' ignored: not an int\n", s);
			}
		}

		System.out.println("Sum = " + sum);

	}

}
