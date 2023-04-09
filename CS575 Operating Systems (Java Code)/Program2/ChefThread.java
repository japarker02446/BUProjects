import java.util.concurrent.locks.ReentrantLock;

public class ChefThread extends Thread {
	
	private static ReentrantLock chefLock = new ReentrantLock();
	private static SynchronizedRestaurant restaurant;
	
	public ChefThread (SynchronizedRestaurant newRestaurant) {
		restaurant = newRestaurant;
	}
	
	public void run() {
		// Make at least one pizza
		try {
			do {
				Thread.sleep(5 * 500);
				
				// Lock the Threads until the pizza is cooked.
				chefLock.lock();
				restaurant.makePizza();
				System.out.println(
					"Chef made a pizza.  " +
					"There are " + restaurant.pizzasAvailable() + " pizzas available."
				);
				chefLock.unlock();
			} while(restaurant.pizzasWanted() > 0);
		} catch (InterruptedException e) {e.printStackTrace();}		
	}
}
