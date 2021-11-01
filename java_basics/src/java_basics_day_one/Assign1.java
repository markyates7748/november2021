package java_basics_day_one;

public class Assign1 {

	public static void main(String[] args) {
		//Part 1
		System.out.println("Part 1:");
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j <= i; j++) {
				System.out.print("*");
			}
			System.out.println("");
		}
		
		//Part 2
		System.out.println("Part 2:");
		for(int i = 0; i < 4; i++) {
			for(int j = 4; j > i; j--) {
				System.out.print("*");
			}
			System.out.println("");
		}
		
		//Part 3		
		System.out.println("Part 3:");
		for(int i = 1; i <= 4; i++) {
			for(int j = 4; j > i; j--) {
				System.out.print(" ");
			}
			for(int j = 0; j < (i * 2) - 1; j++) {
				System.out.print("*");
			}
			System.out.println("");
		}

		
		//Part 4
		System.out.println("Part 4:");
		for(int i = 4; i > 0; i--) {
			for(int j = 0; j < (i * 2) - 1; j++) {
				System.out.print("*");
			}
			System.out.println("");
			for(int j = 4; j >= i; j--) {
				System.out.print(" ");
			}
		}

	}

}
