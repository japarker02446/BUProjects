import java.util.Random;

public class CustomerThread extends Thread {
	
	// Initialize Thread variables
	private int threadId;
	private static SynchronizedRestaurant restaurant;
	
	// Set the customer eating time.
	private Random rand = new Random();
	private final int EATTIME = rand.nextInt(11);
	
	public CustomerThread (int customerNumber, SynchronizedRestaurant newRestaurant) {
		threadId = customerNumber;
		restaurant = newRestaurant;
		
		System.out.println("Customer " + customerNumber + " has arrived.");
	}
	
	public void run() {
		
		try {restaurant.wantPizza();} 
		catch (InterruptedException e) {e.printStackTrace();}
		
		// Get a pizza
		try {
			restaurant.getPizza();
			System.out.println(
					"Customer " + threadId + " got a pizza.  " +
					"There are " + restaurant.pizzasAvailable() + " pizzas remaining."
			);
		} catch (InterruptedException e) {e.printStackTrace();}
		
		// Get a seat
		try {
			restaurant.getSeat();
			System.out.println(
					"Customer " + threadId + " got a seat.  " +
					"There are " + restaurant.seatsAvailable() + " seats remaining."
			);
		} catch (InterruptedException e) {e.printStackTrace();}
		
		// Eat
		try {
			Thread.sleep(EATTIME * 500);
			System.out.println("Customer " + threadId + " ate their pizza in " + EATTIME + " minutes.");
		} catch (InterruptedException e) {e.printStackTrace();}
		
		// Leave
		try {
			restaurant.leaveSeat();
			System.out.println(
					"Customer " + threadId + " left their seat.  " +
					"There are " + restaurant.seatsAvailable() + " seats available."
			);
		} catch (InterruptedException e) {e.printStackTrace();}
	}
}
