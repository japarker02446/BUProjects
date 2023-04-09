import java.io.File;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.ListIterator;
import java.util.Scanner;

public class jshell {

	// Create private class variables.
	private static ArrayList<String> history = new ArrayList<String>(); // Command history list.
	private static String nextArg;										// User input argument.
	
	// Integer values to track command 'Types' as constants.
	private static final int historyCommand = 1;
	private static final int changeDirCommand = 2;
	private static final int backCommand = 3;
	private static final int multiCommand = 4;
	private static final int pipeCommand = 5;
	private static final int regCommand = 6;
	
	// Method to implement an instance of jshell program from command line.
	public static void main(String[] args) {
		
		// Creat Scanner object to read keyboard input.
		final Scanner keyboard = new Scanner (System.in);
				
		// Prompt the user for input.
		System.out.println("Welcome to jshell.");
		System.out.println("jshell can manage all of your shell command needs.");
		System.out.println("Tyope HISTORY to see last 10 commands.");
		System.out.println("Type EXIT to exit.");
		
		//Loop through input until EXIT command is given.
		do {
			
			// Print the shell prompt, get user input and process the argument.
			System.out.print("jshell:>");
			nextArg = keyboard.nextLine().trim();
			int commType = getCommandType(nextArg);
			
			switch(commType) {
				case historyCommand: printHistory(); break;
				case changeDirCommand: changeDirectory(nextArg); break;
				case backCommand: runBackgroundProcess(nextArg); break;
				case multiCommand: runMultipleProcess(nextArg); break;
				case pipeCommand: runPipeCommand(nextArg); break;
				case regCommand: runProcess(nextArg); break;
			}			
		} while (!nextArg.equalsIgnoreCase("EXIT"));
		
		// Cleanup on exit.
		keyboard.close();
		System.out.println("Good Bye.");

	}
	
	// Catchall exceptions
	private static void catchExceptions (Exception e) {
		e.notify();
		System.out.println("oops, so sorry");
	}
	
	// Change current working directory.
	// From www.javacodex.com/Files/Set-The-Current-Working-Directory
	private static void changeDirectory(String arg) {
		
		// Parse the target directory.
		String targetDir = System.getProperty("user.dir");
		
//		System.out.println("Pre CD: System out is " + targetDir);
		
		// Handle different case options.
		// From https://stackoverflow.com/questions/5054995/how-to-replace-case-insensitive-literal-substrings-in-java
		if(arg.toUpperCase().contains("CD ")) {targetDir = arg.replaceAll("(?i)cd ","");}
		
		// Test if targetDir exists.  If not, send a message.
		// From https:\\stackoverflow.com/questions/12780446/check-if-a-path-represents-a-file-or-a-folder/12780471
		File file = new File(targetDir);
		if(file.isDirectory()) {System.setProperty("user.dir", targetDir);}
		else {System.out.println("Directory " + targetDir + " does not exist.");}
		
//		targetDir = System.getProperty("user.dir");
//		System.out.println("Post CD: System out is " + targetDir);
		
		// Add the command to the shell history.
		history.add(arg);
	}
	
	// Parse the input argument to a class specific type.
	private static int getCommandType (String arg) {
		
//		System.out.println("Getting command type for " + arg);
		
		if (arg.equalsIgnoreCase("EXIT")) {return (0);}
		else if(arg.equalsIgnoreCase("HISTORY")) {return (historyCommand);}
		else if(arg.toUpperCase().contains("CD")) {return (changeDirCommand);}
		else if(arg.contains(";")) {return (multiCommand);}
		else if(arg.contains("|")) {return (pipeCommand);}
		else if(arg.contains("&")) {return (backCommand);}
		else {return (regCommand);}
	}
	
	// Print last ten, or fewer, shell commands.
	private static void printHistory() {
		
		// Print the last ten items (or less) from the history list.
		if(history.size() >= 10) {
			ListIterator<String> histIterator = history.listIterator(history.size() - 10);
			while (histIterator.hasNext()) {
				System.out.println(histIterator.next());
			}
		}
		else {
			ListIterator<String> histIterator = history.listIterator();
			while (histIterator.hasNext()) {
				System.out.println(histIterator.next());
			}
		}
	}
	
	// Execute the process, don't wait for it to complete.
	private static void runBackgroundProcess (String arg) {
		try{Process proc = Runtime.getRuntime().exec(new String[] {"/bin/sh", "-c", arg});}
		catch(Exception e) {catchExceptions(e);}
		
//		System.out.println("In background process " + arg);
		// Add the command to the shell history.
		history.add(arg);
	}
	
	private static void runMultipleProcess (String arg) {
		
		// Split the method input into a String array of commands.
		String [] argumentList = arg.split(";");
		
		// Execute each command.
		for (String nextMultiArg : argumentList) {
			
			nextMultiArg = nextMultiArg.trim();
//			System.out.println("In multi command process " + nextMultiArg);
			
			int commType = getCommandType(nextMultiArg);
			switch(commType) {
				case historyCommand: printHistory(); break;
				case changeDirCommand: changeDirectory(nextMultiArg); break;
				case backCommand: runBackgroundProcess(nextMultiArg); break;
				case pipeCommand: runPipeCommand(nextMultiArg); break;
				case regCommand: runProcess(nextMultiArg); break;
			}	
		}
	}

	// From https://www.developer.com/java/data/understanding-java-process-and-java-processbuilder.html
	private static void runPipeCommand (String arg) {
		
		// Parse arg into pre and post pipe commands, trimming any white space.
		String arg1 = arg.substring(0, arg.indexOf("|")).trim();
		String arg2 = arg.substring(arg.indexOf("|") +1, arg.length()).trim();
		
//		System.out.println("In pipe command1 " + arg1);
//		System.out.println("In pipe command2 " + arg2);
		
		Process proc1 = null;
		Process proc2 = null;
		
		// Execute Process 1 (the Pre-pipe process).
		// The output of Process 1 is captured from its InputStream (so intuitive).
		try{
			proc1 = Runtime.getRuntime().exec(new String[] {"/bin/sh", "-c", arg1});
		}
		catch(Exception e) {catchExceptions(e);}
		InputStream procIn = proc1.getInputStream();
		
		// Execute Process 2 using the output of Process 1 (in the Process 1 InputStream) as input.
		try{
			proc2 = Runtime.getRuntime().exec(new String[] {"/bin/sh", "-c", arg2, procIn.toString()});
			proc2.waitFor();
		}
		catch(Exception e) {catchExceptions(e);}
		
		// Add the command to the shell history.
		history.add(arg);
	}
	
	// Execute the process, wait for it to complete and return the exit value of subprocess.
	// From https://coderanch.com/t/538967/java/Running-commands-Runtime-getRuntime-exec
	// From https://stackoverflow.com/questions/17972380/wait-for-process-to-finish-before-proceeding-in-java
	private static void runProcess (String arg) {
		try{int proc = Runtime.getRuntime().exec(new String[] {"/bin/sh", "-c", arg}).waitFor();}
		catch(Exception e) {catchExceptions(e);}
	
//		System.out.println("In regular process " + arg);
		
		// Add the command to the shell history.
		history.add(arg);
	}
}
