package java_basics_day_four;

import java.util.LinkedList;

public class ProduceConsumeThread {
	
	protected LinkedList<Integer> itemList = new LinkedList<Integer>();
	private int listCapacity = 3;
	private int itemNumber = 0;
	
	public void produce() throws InterruptedException{
		while(true) {
			synchronized(this) {
				while(itemList.size() == listCapacity) {
					wait();
				}
				itemList.add(itemNumber++);
				System.out.println("Item Produced -> " + itemNumber);
				notify();
			}
		}
	}
	
	public void consume() throws InterruptedException{
		while(true) {
			synchronized(this) {
				while(itemList.size() == 0) {
					wait();
				}
				itemList.removeFirst();
				System.out.println("Item Consumed -> " + itemNumber);
				itemNumber--;
				notify();
			}
		}
	}
	
}
