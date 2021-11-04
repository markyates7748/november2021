package java_basics_day_four;

//Implement Singleton with double checked locking

public class Singleton {
	
	private static volatile Singleton instance = null;
	
	private Singleton() {
		
	}
	
	public static Singleton getInstance() {
		if(instance == null) {
			synchronized(Singleton .class) {
				if(instance == null) {
					instance = new Singleton();
				}
			}
		}
		return instance;
	}

}
