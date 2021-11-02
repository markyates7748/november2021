package java_basics_day_two;

public class Rectangle implements Shape {
	
	private double height;
	private double length;
	
	private double area;
	
	public Rectangle(double height, double length) {
		this.height = height;
		this.length = length;
	}

	@Override
	public void calculateArea() {
		this.area = this.height * this.length;
	}

	@Override
	public void display() {
		System.out.println(this.area);
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
