package java_basics_day_two;

public class Rectangle implements Shape {
	
	private double height;
	private double length;
	
	public Rectangle(double height, double length) {
		this.height = height;
		this.length = length;
	}

	@Override
	public double calculateArea() {
		// TODO Auto-generated method stub
		return this.height * this.length;
	}

	@Override
	public void display() {
		// TODO Auto-generated method stub

	}

	public double getHeight() {
		return height;
	}

	public void setHeight(double height) {
		this.height = height;
	}

	public double getLength() {
		return length;
	}

	public void setLength(double length) {
		this.length = length;
	}

}
