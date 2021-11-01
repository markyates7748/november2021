package java_basics_day_two;

public class Assign1 {

	public static void main(String[] args) {
		
		// TODO take values from the command line and add them together
		int sum = 0;
		
		for(String s: args) {
			sum += Integer.parseInt(s);
		}
		
		System.out.println(sum);

	}

}
