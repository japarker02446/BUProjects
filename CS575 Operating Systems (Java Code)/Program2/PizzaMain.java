import java.util.Random;

public class PizzaMain {
	
	// Get the number of customers, up to 20.
	static Random rand = new Random();
	static final int CUSTOMERCOUNT = rand.nextInt(21);
	
	public static void main(String[] args) {
		
		// Initialize our thread and restaurant objects.
		SynchronizedRestaurant pizzaShop = new SynchronizedRestaurant();
		pizzaShop.init();
		
		System.out.println("Create one chef thread.");
		ChefThread chef = new ChefThread(pizzaShop);
		chef.start();
		
		System.out.println("Create " + CUSTOMERCOUNT + " customer threads.");
		CustomerThread[] customers = new CustomerThread[CUSTOMERCOUNT];
		for(int i = 0; i < CUSTOMERCOUNT; i ++) {
			customers[i] = new CustomerThread(i, pizzaShop);
			customers[i].start();
		}
		
		// Wait for everyone to eat.
		for(int i = 0; i < CUSTOMERCOUNT; i ++) {
			try {customers[i].join();}
			catch (InterruptedException e) {e.printStackTrace();}
		}
		
		// Let the chef clock out.
		try {chef.join();}
		catch (InterruptedException e) {e.printStackTrace();}
		
		// Exit
		System.out.println("There are " + pizzaShop.pizzasAvailable() + " pizzas left.");
		System.out.println("Thank you for eating at our pizza shop.");
	}
}
