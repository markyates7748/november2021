package java_basics_day_four;

public class ProducerConsumerExample {

	public static void main(String[] args) throws InterruptedException{
		//Create producer and consumer threads for ints with a bounded buffer (array)
		final ProduceConsumeThread example = new ProduceConsumeThread();
		
		Thread producer = new Thread(new Runnable() {
			@Override
			public void run() {
				try {
					example.produce();
				}catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
		});
		Thread consumer = new Thread(new Runnable() {
			@Override
			public void run() {
				try {
					example.consume();
				}catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
		});
		
		producer.start();
		consumer.start();
		
		producer.join();
		consumer.join();
	}

}
