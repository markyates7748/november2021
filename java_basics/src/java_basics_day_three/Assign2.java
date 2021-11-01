package java_basics_day_three;

import java.io.*;

public class Assign2 {
	
	//TODO: Append text to an existing file
	public static void main(String[] args) throws FileNotFoundException {
		
		String fileToAppend = args[0];
		String textToAdd = "Simple Test";
		
		try {
			FileWriter fw = new FileWriter(fileToAppend, true);
			fw.append(textToAdd);
			fw.close();
		}catch(IOException e) {
			
		}
		
	}

}
