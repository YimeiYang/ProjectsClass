package twitter;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;


public class MyHashTable<K,V> implements Iterable<HashPair<K,V>>{
    // num of entries to the table
    private int numEntries;
    // num of buckets 
    private int numBuckets;
    // load factor needed to check for rehashing 
    private static final double MAX_LOAD_FACTOR = 0.75;
    // ArrayList of buckets. Each bucket is a LinkedList of HashPair
    private ArrayList<LinkedList<HashPair<K,V>>> buckets; 
    
    // constructor
    public MyHashTable(int initialCapacity) {
        // ADD YOUR CODE BELOW THIS
        numBuckets = initialCapacity;
        numEntries = 0;
        //ADD YOUR CODE ABOVE THIS
        buckets = new ArrayList<LinkedList<HashPair<K,V>>>(initialCapacity);
        for(int i = 0; i<initialCapacity; i++) {
        	this.buckets.add(new LinkedList<HashPair<K,V>>());
        }
    }
    
    public int size() {
        return this.numEntries;
    }
    
    public boolean isEmpty() {
        return this.numEntries == 0;
    }
    
    public int numBuckets() {
        return this.numBuckets;
    }
    
    /**
     * Returns the buckets variable. Useful for testing  purposes.
     */
    public ArrayList<LinkedList< HashPair<K,V> > > getBuckets(){
        return this.buckets;
    }
    
    /**
     * Given a key, return the bucket position for the key. 
     */
    public int hashFunction(K key) {
        int hashValue = Math.abs(key.hashCode())%this.numBuckets;
        return hashValue;
    }
    
    /**
     * Takes a key and a value as input and adds the corresponding HashPair
     * to this HashTable. Expected average run time  O(1)
     */
    public V put(K key, V value) {
    	V oldValue = null;
    	int hashValue = hashFunction(key);
    	LinkedList<HashPair<K, V>> List = buckets.get(hashValue);
    	HashPair<K, V> newPair = new HashPair<K, V>(key, value);
    	if(List == null) {
    		return null;
    	}
    		for(int i = 0; i<List.size(); i++) {
    			HashPair<K, V> found = List.get(i);
    			if(found != null && found.getKey().equals(key)) {
    				oldValue = found.getValue();
    				found.setValue(value);
    				return oldValue;
    			}
    		}
    		this.numEntries = this.numEntries + 1;
			
    		int localFactor = this.numEntries/this.numBuckets;
			if(localFactor > MAX_LOAD_FACTOR) {
				rehash();
				this.buckets.get(hashValue).addLast(newPair);
				return null;
			}
			
			List.addLast(newPair);
			
    	return null;
    }
    
    
    /**
     * Get the value corresponding to key. Expected average runtime O(1)
     */
    
    public V get(K key) {
        //ADD YOUR CODE BELOW HERE
    	int hashValue = hashFunction(key);
    	
    	LinkedList<HashPair<K, V>> List = this.buckets.get(hashValue);
    	if(List == null) {
    		return null;
    	}
    		for(int i = 0; i<List.size(); i++) {
    			HashPair<K, V> found = List.get(i);
    			if(found.getKey().equals(key)) {
    				return found.getValue();
    			}
    		}
    	return null;
    	
    }
    
    /**
     * Remove the HashPair corresponding to key . Expected average runtime O(1) 
     */
    public V remove(K key) {
        //ADD YOUR CODE BELOW HERE
    	V oldValue = null;
    	int hashValue = hashFunction(key);
    	int i = 0;
    	LinkedList<HashPair<K, V>> List = buckets.get(hashValue);
    	if(List == null) {
    		return null;
    	}
    		for(i = 0; i<List.size(); i++) {
    			HashPair<K, V> found = List.get(i);
    			if(found.getKey().equals(key)) {
    				oldValue = found.getValue();
    				List.remove(i);
    				numEntries = numEntries - 1;
    				break;
    			}
    		}
    	return oldValue;
    }
    
    
    /** 
     * Method to double the size of the hashtable if load factor increases
     * beyond MAX_LOAD_FACTOR.
     * Made public for ease of testing.
     * Expected average runtime is O(m), where m is the number of buckets
     */
    public void rehash() {
    	
        int tempE = this.numEntries;
        ArrayList<LinkedList<HashPair<K,V>>> temp = this.buckets;
        this.numBuckets = 2*this.numBuckets;
        this.buckets = new ArrayList<LinkedList<HashPair<K,V>>>(this.numBuckets);
        
        for(int i = 0; i<this.numBuckets; i++) {
        	this.buckets.add(new LinkedList<HashPair<K,V>>());
        }
        int i = 0;
        for(i = 0; i<temp.size(); i++) {
        	for(int a = 0; a<temp.get(i).size(); a++) {
        		this.put(temp.get(i).get(a).getKey(), temp.get(i).get(a).getValue());
        	}
        }
        this.numEntries = tempE;
        
    }
    
    
    /**
     * Return a list of all the keys present in this hashtable.
     * Expected average runtime is O(m), where m is the number of buckets
     */
    
    public ArrayList<K> keys() {
        ArrayList<K> keys = new ArrayList<K>(100);
        int i = 0;
        for(i = 0; i<this.numBuckets; i++) {
        	for(int j = 0; j<this.buckets.get(i).size(); j++) {
        		K key = buckets.get(i).get(j).getKey();
        		keys.add(key);	
        	}
        }
        
    	return keys;
    	
    }
    
    /**
     * Returns an ArrayList of unique values present in this hashtable.
     * Expected average runtime is O(m) where m is the number of buckets
     */
    public ArrayList<V> values() {
        MyHashTable values = new MyHashTable(100);
        int i = 0;
        for(i=0; i<this.numBuckets; i++) {
        	for(int j = 0; j<this.buckets.get(i).size(); j++) {
        		V value = buckets.get(i).get(j).getValue();
        		values.put(value, 1);
        		}
        }
        
    	return values.keys();
    }
    
    
	/**
	 * This method takes as input an object of type MyHashTable with values that 
	 * are Comparable. It returns an ArrayList containing all the keys from the map, 
	 * ordered in descending order based on the values they mapped to. 
	 * 
	 * The time complexity for this method is O(n^2), where n is the number 
	 * of pairs in the map. 
	 */
    public static <K, V extends Comparable<V>> ArrayList<K> slowSort (MyHashTable<K, V> results) {
        ArrayList<K> sortedResults = new ArrayList<>();
        for (HashPair<K, V> entry : results) {
			V element = entry.getValue();
			K toAdd = entry.getKey();
			int i = sortedResults.size() - 1;
			V toCompare = null;
        	while (i >= 0) {
        		toCompare = results.get(sortedResults.get(i));
        		if (element.compareTo(toCompare) <= 0 )
        			break;
        		i--;
        	}
        	sortedResults.add(i+1, toAdd);
        }
        return sortedResults;
    }
    
    
	/**
	 * This method takes as input an object of type MyHashTable with values that 
	 * are Comparable. It returns an ArrayList containing all the keys from the map, 
	 * ordered in descending order based on the values they mapped to.
	 * 
	 * The time complexity for this method is O(n*log(n)), where n is the number 
	 * of pairs in the map. 
	 */
    
    private static <K, V extends Comparable<V>> ArrayList<HashPair<K,V>> merge(ArrayList<HashPair<K,V>> fir, ArrayList<HashPair<K,V>> sec) {
    	ArrayList<HashPair<K,V>> newList = new ArrayList<HashPair<K,V>>();
    	while(!fir.isEmpty() && ! sec.isEmpty()) {
    		V value1 = fir.get(0).getValue();
    		V value2 = sec.get(0).getValue();
    		if(value1.compareTo(value2) >= 0) {
    			newList.add(fir.remove(0));
    		}
    		else {
    			newList.add(sec.remove(0));
    		}
    	}
    	while(!fir.isEmpty()) {
    		newList.add(fir.remove(0));
    	}
    	while(!sec.isEmpty()) {
    		newList.add(sec.remove(0));
    	}
    	return newList;
    }
    
    private static <K, V extends Comparable<V>> ArrayList<HashPair<K,V>> mergeSort(ArrayList<HashPair<K,V>> sort){
    	ArrayList<HashPair<K,V>> list1 = new ArrayList<HashPair<K,V>>();
        ArrayList<HashPair<K,V>> list2 = new ArrayList<HashPair<K,V>>();
        if(sort.size() == 1) {
        	return sort;
        }
        else {
        	int mid = (sort.size()-1)/2;
        	for(int i = 0; i<mid+1; i++) {
        		list1.add(sort.get(i));
        	}
        	for(int i = mid+1; i<sort.size(); i++) {
        		list2.add(sort.get(i));
        	}
        	list1 = mergeSort(list1);
        	list2 = mergeSort(list2);
        	return merge(list1, list2);
        }
    }
    
    public static <K, V extends Comparable<V>> ArrayList<K> fastSort(MyHashTable<K, V> results) {
    	ArrayList<HashPair<K,V>> allPair = new ArrayList<HashPair<K,V>>();
    	ArrayList<K> keySet = new ArrayList<K>();
    	for(int i = 0; i<results.numBuckets; i++) {
    		for(int j = 0; j<results.buckets.get(i).size(); j++) {
    			allPair.add(results.buckets.get(i).get(j));
    		}
    	}
    	allPair = mergeSort(allPair);
    	for(int a = 0; a<allPair.size(); a++) {
    		keySet.add(allPair.get(a).getKey());
    	}
    	return keySet;
    }

    
    
    @Override
    public MyHashIterator iterator() {
        return new MyHashIterator();
    }   
    
    private class MyHashIterator implements Iterator<HashPair<K,V>> {
        //ADD YOUR CODE BELOW HERE
    	int cur;
    	ArrayList<HashPair<K,V>> newListPair = createList();;
    	
    	private ArrayList<HashPair<K,V>> createList(){
        	ArrayList<HashPair<K,V>> allPair = new ArrayList<HashPair<K,V>>();
        	for(int i = 0; i<numBuckets; i++) {
        		for(int j = 0; j<buckets.get(i).size(); j++) {
        			allPair.add(buckets.get(i).get(j));
        		}
        	}
        	return allPair;
        }
    	
    	
    	/**
    	 * Expected average runtime is O(m) where m is the number of buckets
    	 */
        private MyHashIterator() {
            cur = 0;
        }
        
        @Override
        /**
         * Expected average runtime is O(1)
         */
        public boolean hasNext() {
        	return (cur<newListPair.size()-1 && newListPair.get(cur) != null);	
        }
        
        @Override
        /**
         * Expected average runtime is O(1)
         */
        public HashPair<K,V> next() {
        	return newListPair.get(cur++);
        }    
    }
}
