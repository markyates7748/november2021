package java_basics_day_two;

public class Triangle implements Shape {
	
	private double base;
	private double height;
	
	private double area;

	public Triangle(double base, double height) {
		this.base = base;
		this.height = height;
	}

	@Override
	public void calculateArea() {
		this.area = (this.base * this.height) * 0.5;
	}

	@Override
	public void display() {
		System.out.println(this.area);
	}

	public double getBase() {
		return base;
	}

	public void setBase(double base) {
		this.base = base;
	}

	public double getHeight() {
		return height;
	}

	public void setHeight(double height) {
		this.height = height;
	}

}
