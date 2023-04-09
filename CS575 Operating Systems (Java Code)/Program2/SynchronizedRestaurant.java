import java.util.Scanner;

public class SynchronizedRestaurant {
	
	// Initialize pizza shop parameters, number of Seats and Plates to hold pizzas.
	private static int maxSeats = 11;	
	private static int openSeats = 0;

	private static int maxPlates = 11;
	private static int pizzaCount = 0;
	private static int pizzaWant = 0;
	
	// Get user input for the number of seats and plates.
	public synchronized void init() {
		
		// Creatr a scanner to read user input.
		Scanner in = new Scanner(System.in);
		
		// Get the number of plates M, between 1 and 10.
		while(maxPlates <= 0 | maxPlates > 10){
			System.out.println("Please enter a number M");
			maxPlates = in.nextInt();		
			if(maxPlates > 10) {System.out.println("Please choose a smaller number");}
			if(maxPlates <= 0) {System.out.println("Please choose a larger number");}
		}
		
		// Get the number of seats N, between 1 and 10.
		while(maxSeats <= 0 | maxSeats > 10){
			System.out.println("Please enter a number N");
			maxSeats = in.nextInt();		
			if(maxSeats > 10) {System.out.println("Please choose a smaller number");}
			if(maxSeats <= 0) {System.out.println("Please choose a larger number");}
		}
		openSeats = maxSeats;
		 
		 // Close the Scanner.
		 in.close();
	}
	
	// Get a seat if there is a seat to get.
	public synchronized void getSeat() throws InterruptedException {
		while(openSeats == 0) {wait();}
		notifyAll(); // Alert waiting customers that a seat is available.
		openSeats --;
		
		// Too many customers are in the restaurant.
		if(openSeats < 0){System.out.println("Please wait until there are more seats!");}
	}
	
	// Done eating?  Get out.
	public synchronized void leaveSeat() throws InterruptedException {
		openSeats ++;
		notifyAll();	// Alert waiting CustomerThreads that a seat is available.
		if(openSeats > maxSeats){
			int overSeats = maxSeats - openSeats; 
			System.out.println("Warning, restaurant is consuming negative space " + overSeats);
		}
	}
	
	// Customers want a pizza when they show up.
	public synchronized void wantPizza() throws InterruptedException {
		pizzaWant ++;
		notifyAll();  // CHEF! We want pizza!
	}
	
	// Get a pizza if there is a pizza to get, one per customer.
	public synchronized void getPizza() throws InterruptedException {		
		while(pizzaCount == 0) {wait();}
		notifyAll();	// Alert waiting ChefThread that a plate is available.
		pizzaCount --;
		pizzaWant --;
				
		// Too many pizzas have been taken.
		if(pizzaCount < 0) {System.out.println("HEY! No sharing pizzas!");}		
	}
	
	// Chef makes pizzas to fill plates.
	public synchronized void makePizza() throws InterruptedException{
		while(pizzaCount == maxPlates) {wait();}
		pizzaCount ++;
		notifyAll();	// Alert waiting CustomerThreads that pizza is available.
		
		// Pizzas are going on the floor.
		int overPizzas = maxPlates - pizzaCount;
		if(pizzaCount > maxPlates) {System.out.println("Whoops, chef made " + overPizzas + " pizzas too many.");}
	}
	
	// How many seats are open?
	public synchronized int seatsAvailable() {return openSeats;}
	
	// How many pizzas and plates are wanted or available?
	public synchronized int pizzasAvailable() {return pizzaCount;}
	
	public synchronized int pizzasWanted() {return pizzaWant;}
	
	public synchronized int platesAvailable() {return maxPlates - pizzaCount;}
}
