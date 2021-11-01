package java_basics_day_two;

public class Assign2 {

	public static void main(String[] args) {
		
		// TODO Find max number in 2D array
		
		//Create and populate new array with random values
		int[][] tempArray;
		tempArray = new int[10][10];
		
		for(int i = 0; i < 10; i++) {
			for(int j = 0; j < 10; j++) {
				tempArray[i][j] = ((int) (Math.random() * (100 - 1))) + 1;
			}
		}
		
		int maxValue = -1;
		int maxValueRow = -1;
		int maxValueColumn = -1;
		
		//Locate the max value and record its location
		for(int i = 0; i < 10; i++) {
			for(int j = 0; j < 10; j++) {
				if(tempArray[i][j] > maxValue) {
					maxValue = tempArray[i][j];
					maxValueRow = i;
					maxValueColumn = j;
				}
			}
		}
		
		System.out.printf("The largest value found is %d at (%d,%d)", maxValue, maxValueRow, maxValueColumn);
		
	}

}
