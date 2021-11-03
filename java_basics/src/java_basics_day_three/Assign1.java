package java_basics_day_three;

import java.io.File;

public class Assign1 {
	
	//TODO: get all file/directory names in given directory
	public static void main(String[] args) {
		//Get directory path from CL
		String filePath = args[0];
		System.out.println("Beginning process at " + filePath);
		printFound(filePath);
	}
	
	//Recursive method to list all files found in directories starting in given directory
	private static void printFound(String pathToDirectory) {
		File startingDirectory = new File(pathToDirectory);
		File[] foundItems = startingDirectory.listFiles();
		if(foundItems != null) {
			for(File f : foundItems) {
				if(f.isDirectory()) {
					System.out.println("Starting in new directory: " + f.getName());
					printFound(f.getAbsolutePath());
				}else {
					System.out.println("File Found: " + f.getName());
				}
			}
		}
	}

}
