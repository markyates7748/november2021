package java_basics_day_two;

public class Assign2 {

	public static void main(String[] args) {
		
		// TODO Find max number in 2D array
		
		//Create and populate new array with random values
		int rows = 10;
		int columns = 10;
		int[][] createdArray = populate2DArray(rows, columns);
		
		int maxValue = -1;
		int maxValueRow = -1;
		int maxValueColumn = -1;
		
		//Locate the max value and record its location
		for(int i = 0; i < rows; i++) {
			for(int j = 0; j < columns; j++) {
				if(createdArray[i][j] > maxValue) {
					maxValue = createdArray[i][j];
					maxValueRow = i;
					maxValueColumn = j;
				}
			}
		}
		
		System.out.printf("The largest value found is %d at (%d,%d)", maxValue, maxValueRow, maxValueColumn);
		
	}

	//Method to populate 2D array with specified dimensions with randomly generated values between 1 and 100 inclusive
	private static int[][] populate2DArray(int rows, int columns){
		int[][] tempArray;
		tempArray = new int[rows][columns];
		
		for(int i = 0; i < rows; i++) {
			for(int j = 0; j < columns; j++) {
				tempArray[i][j] = ((int) (Math.random() * (100 - 1))) + 1;
			}
		}
		return tempArray;
	}
	
}
