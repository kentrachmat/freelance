package lab3;
import java.util.*;

/**
 * Overview: Queue0fDistinctStringsare mutable, bounded 
 * collection of distinct strings that operate in 
 * FIFO (First-In-First-Out) order.
 */
public class Queue0fDistinctStrings {

    // A) The abstraction function is: 
    // represents the the collection of strings with
    // a spesification position (front and end).


    // B) The rep invariant is: 
    // this.items.size() cannot be empty
    // this.items.get(0) != this.items.get(1) != ... != this.items.get(this.items.size()-1)
    // the strings on the list must be distinct (unique)

    private ArrayList<String> items;

    /**
     * Constructor
     * EFFECTS : Creates a new Queue0fDistinctStrings object
     */
    public Queue0fDistinctStrings(){
        this.items = new ArrayList<String>();
    }

    /**
     * MODIFIES: this 
     * EFFECTS: Appends the element at the end of the queue
     * if the element is not in the queue, otherwise 
     * does nothing.
     */
    public void enqueue(String element) throws Exception { 
        if(element == null) throw new Exception(); 
        if(false == items.contains(element)) 
            items.add(element); 
    } 

    /**
     * MODIFIES: this 
     * EFFECTS: Removes an element from the front of the queue 
     */
    public String dequeue() throws Exception { 
        if (items.size() == 0) throw new Exception(); 
            return items.remove(0); 
    } 

    /**
     * EFFECTS: Returns true if the rep invariant holds for this 
     * object; otherwise returns false 
     */
    public boolean repOK() { 
        if (items.size() == 0) return false;
        
        Set<String> newL =  new HashSet<String>(this.items); 
        return (newL.size() == this.items.size()); 
    }

    /**
     * EFFECTS: Returns a string that contains the strings in the 
     * queue, the front element and the end element.
     * Implements the abstraction function. 
     */
    public String toString(){
        return "Strings : " + this.items + ", front : " + this.items.get(0) + ", end : " + this.items.get(this.items.size() - 1);
    }

    /**
     * Test the code (Addition)
     */
    public static void main(String[] args) throws Exception{
        Queue0fDistinctStrings liste = new Queue0fDistinctStrings();

        liste.enqueue("ab");
        liste.enqueue("cd");
        liste.enqueue("ef");
        liste.enqueue("gh");
        liste.enqueue("ij");

        System.out.println(liste);
        System.out.println("Rep Invariant check : "+liste.repOK());
    }
}
