package java_basics_day_two;

public class Circle implements Shape {

	private double radius;
	
	private double area;

	public Circle(double radius) {
		this.radius = radius;
	}

	@Override
	public void calculateArea() {
		this.area = 3.14 * this.radius * this.radius;
	}

	@Override
	public void display() {
		System.out.println(this.area);
	}

	public double getRadius() {
		return radius;
	}

	public void setRadius(double radius) {
		this.radius = radius;
	}

}
