package java_basics_day_one;

import java.util.Scanner;

public class Assign2 {

	public static void main(String[] args) {
		
		int correctNumber = ((int) (Math.random() * (100 - 1))) + 1;
		Scanner sc = new Scanner(System.in);
		int guessedNumber = -1;
		Boolean userCorrect = false;
		int totalGuesses = 0;
		
		while(!userCorrect && totalGuesses < 5) {
			System.out.print("Guess a number between 1 and 100: ");
			guessedNumber = sc.nextInt();
			totalGuesses++;
			if(guessedNumber <= (correctNumber + 10) && guessedNumber >= (correctNumber - 10)) {
				userCorrect = true;
			}else {
				System.out.println("Not close enough");
			}
		}
		
		if(userCorrect) {
			System.out.printf("You were close enough! The correct number was: %d\n", correctNumber);
		}else {
			System.out.printf("Sorry! The correct number was: %d\n", correctNumber);
		}
		
		sc.close();
		
	}

}
