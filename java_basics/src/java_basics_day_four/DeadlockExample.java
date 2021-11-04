package java_basics_day_four;

public class DeadlockExample {

	private static Object resourceA = new Object();
	private static Object resourceB = new Object();

	public static void main(String[] args) {
		//Create a deadlock between two threads
		SampleThreadOne thread1 = new SampleThreadOne();
		SampleThreadTwo thread2 = new SampleThreadTwo();

		thread1.start();
		thread2.start();
	}

	private static class SampleThreadOne extends Thread {
		@Override
		public void run() {
			synchronized (resourceA) {
				System.out.println("Thread One holding Resource A and waiting for Resource B");
				synchronized (resourceB) {
					System.out.println("Thread One has Resource A and Resource B");
				}
			}
		}
	}

	private static class SampleThreadTwo extends Thread {
		@Override
		public void run() {
			synchronized (resourceB) {
				System.out.println("Thread Two holding Resource B and waiting for Resource A");
				synchronized (resourceA) {
					System.out.println("Thread Two has Resource B and Resource A");
				}
			}
		}
	}

}
