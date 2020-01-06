/**
 * Looking for a mathematical bound on how many steps it would take to go from some number(smaller) to some other number(higher) using:
 * +1 and x2 as operations 
 * example
 * 4 to 17
 * Has a solution in 3 steps:
 * 4[x 2, x 2, + 1]=17 but also has a non-optimal solution (4 + 1 + 1 + 1 x 2 + 1 + 1 + 1)
 * 
 * This class is a simple tree search to test hypothetical bounds by finding the shortest sequence of operations between the numbers
 */

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;
public class ArithmeticWalk {

	public static void main(String[] args){
		
		//get the smaller numbers
		Scanner input = new Scanner(System.in);
		int smallN = input.nextInt();
		int bigN = input.nextInt();
		input.close();
		
		//run a BFS
		//using the +1 and x2 as operations you are guaranteed to find a solution, note this is not a guarantee for all combinations of operations
		SearchPath(smallN, bigN);
	}
	
	//Runs a BFS and returns the shortest path.
	private static void SearchPath(int smallN, int bigN) {
		if(smallN >= bigN){
			System.out.println("Bad input for search path function");
			return;
		}
		
		Queue<Node> Q = new ArrayDeque<>();
		
		Node start = new Node(smallN);
		Q.add(start);
		boolean foundSolution = false;
		Node solution = null;
		
		//bfs, each node on creation gets its parents history plus the operation used to create it.
		while(!foundSolution){
			Node currentNode = Q.poll();
			if(currentNode.value == bigN){
				foundSolution = true;
				solution = currentNode;
			}
			Node childopp1 = new Node(currentNode.value + 1, new ArrayList<>(currentNode.History));
			Node childopp2 = new Node(currentNode.value*2, new ArrayList<>(currentNode.History));
			
			childopp1.addToHistory("+ 1");
			childopp2.addToHistory("x 2");
			
			Q.add(childopp1);
			Q.add(childopp2);
			
		}
		
		System.out.println("Found a solution in "+ solution.History.size()+" steps:");
		System.out.print("" + smallN + solution.History.toString() + "=" + solution.value);
		
	}
	
	//small class to maintain the history of operations
	private static class Node{
		private int value;
		private List<String> History = new ArrayList<String>(); 
		
		Node(int value){
			this.value = value;
		}
		
		Node(int value, List<String> History){
			this.value = value;
			this.History = History;
		}
		
		void addToHistory(String operation){
			History.add(operation);
		}
		
	}
	
	
}

