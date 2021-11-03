package java_basics_day_three;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Assign3 {
	
	//TODO: Count number of times a char appears in a file
	public static void main(String[] args) throws FileNotFoundException {
		
		String fileToRead = args[0];
		String characterToCheck;
		try {
			characterToCheck = args[1];
		} catch(Exception e) {
			System.out.print("Please enter a character to check: ");
			characterToCheck = new Scanner(System.in).nextLine();
		}
		int numberOfCharacters = 0;
		List<String> fileLines = new ArrayList<String>();
		
		try {
			BufferedReader br = new BufferedReader(new FileReader(fileToRead));
			for(String tempLine ; (tempLine = br.readLine()) != null;) {
				fileLines.add(tempLine);
			}
			br.close();
			for(String str: fileLines) {
				for(int i = 0; i < str.length(); i++) {
					if(str.charAt(i) == characterToCheck.charAt(0)) {
						numberOfCharacters++;
					}
				}
			}
			System.out.printf("The character %s was found %d times", characterToCheck, numberOfCharacters);
		}catch(IOException e) {
			e.printStackTrace();
		}
		
	}

}
