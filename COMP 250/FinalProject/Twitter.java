package twitter;

import java.util.ArrayList;

public class Twitter {
	
	//ADD YOUR CODE BELOW HERE
	private ArrayList<Tweet> Tws;
	private ArrayList<String> sW;
	MyHashTable<String,Tweet> authorTweet;
	MyHashTable<String,ArrayList<Tweet>> DateTweet;
	MyHashTable<String, Integer> wordsTweet;
	
	//ADD CODE ABOVE HERE 
	
	// O(n+m) where n is the number of tweets, and m the number of stopWords
	public Twitter(ArrayList<Tweet> tweets, ArrayList<String> stopWords) {
		//ADD YOUR CODE BELOW HERE
		Tws = tweets;
		sW = stopWords;
		
		this.authorTweet = new MyHashTable<String, Tweet>(Tws.size());
		this.DateTweet = new MyHashTable<String, ArrayList<Tweet>>(Tws.size());
		this.wordsTweet = new MyHashTable<String, Integer>(Tws.size());
		
		for(int i = 0; i<Tws.size(); i++) {
			addTweet(Tws.get(i));
		}
		
	}
	
	
    /**
     * Add Tweet t to this Twitter
     * O(1)
     */
	public void addTweet(Tweet t) {
		String author = t.getAuthor();
		String date = t.getDateAndTime();
		//add tweet to authorTweet table
		//if the new tweet is later than the older tweet, put; otherwise, continue.
		
		if(authorTweet.get(author)!=null && !this.authorTweet.isEmpty()) {
			if(authorTweet.get(author).compareTo(t)<0) {
				authorTweet.put(author, t);
			}
		}
		else {
			authorTweet.put(author, t);
		}
		
		//add tweet to dateTweet table
		if(DateTweet.get(date.substring(0,10))==null){
			ArrayList<Tweet> tweetsDate = new ArrayList<Tweet>();
			tweetsDate.add(t);
			DateTweet.put(date.substring(0,10), tweetsDate);
		}
		else {
			DateTweet.get(date.substring(0,10)).add(t);
		}
		
		//add tweet to wordsTweet table
		String message = t.getMessage();
		ArrayList<String> wordsI = getWords(message);
		ArrayList<String> words = new ArrayList<String>();
		for (int i = 0; i<wordsI.size(); i++) {
			words.add(wordsI.get(i).toLowerCase());
		}
		//ArrayList<String> allWords = wordsTweet.keys();
		for(int i = 0; i<words.size(); i++) {
			if(wordsTweet.get(words.get(i)) == null) {
				wordsTweet.put(words.get(i).toLowerCase(), 1);
			}
			else if(wordsTweet.get(words.get(i)) != null && words.indexOf(words.get(i).toLowerCase())== i) {
				wordsTweet.put(words.get(i).toLowerCase(), wordsTweet.get(words.get(i).toLowerCase())+1);
			}
		}
	}
	

    /**
     * Search this Twitter for the latest Tweet of a given author.
     * If there are no tweets from the given author, then the 
     * method returns null. 
     * O(1)  
     */
    public Tweet latestTweetByAuthor(String author) {
        //ADD CODE BELOW HERE
    	Tweet result = authorTweet.get(author);
    	return result;
    }


    /**
     * Search this Twitter for Tweets by `date' and return an 
     * ArrayList of all such Tweets. If there are no tweets on 
     * the given date, then the method returns null.
     * O(1)
     */
    public ArrayList<Tweet> tweetsByDate(String date) {
    	ArrayList<Tweet>tweetDate = DateTweet.get(date);
    	return tweetDate;
    	
    }
    
	/**
	 * Returns an ArrayList of words (that are not stop words!) that
	 * appear in the tweets. The words should be ordered from most 
	 * frequent to least frequent by counting in how many tweet messages
	 * the words appear. Note that if a word appears more than once
	 * in the same tweet, it should be counted only once. 
	 */
    public ArrayList<String> trendingTopics() {
    	for(int j = 0; j<sW.size(); j++) {
			wordsTweet.remove(sW.get(j));
		}
    	ArrayList<String> keys = MyHashTable.fastSort(wordsTweet);	
    	return keys;
    }
    
    
    
    /**
     * An helper method you can use to obtain an ArrayList of words from a 
     * String, separating them based on apostrophes and space characters. 
     * All character that are not letters from the English alphabet are ignored. 
     */
    private static ArrayList<String> getWords(String msg) {
    	msg = msg.replace('\'', ' ');
    	String[] words = msg.split(" ");
    	ArrayList<String> wordsList = new ArrayList<String>(words.length);
    	for (int i=0; i<words.length; i++) {
    		String w = "";
    		for (int j=0; j< words[i].length(); j++) {
    			char c = words[i].charAt(j);
    			if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z'))
    				w += c;
    			
    		}
    		wordsList.add(w);
    	}
    	return wordsList;
    }

    

}
