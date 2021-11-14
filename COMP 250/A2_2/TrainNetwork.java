package trainRide;

public class TrainNetwork {
	final int swapFreq = 2;
	TrainLine[] networkLines;

    public TrainNetwork(int nLines) {
    	this.networkLines = new TrainLine[nLines];
    }
    
    public void addLines(TrainLine[] lines) {
    	this.networkLines = lines;
    }
    
    public TrainLine[] getLines() {
    	return this.networkLines;
    }
    
    public void dance() {
    	System.out.println("The tracks are moving!");
    	//YOUR CODE GOES HERE
    	for(int i = 0; i<networkLines.length; i++) {
    		networkLines[i].shuffleLine();
    	}
    }
    
    public void undance() {
    	//YOUR CODE GOES HERE
    	for(int i = 0; i<networkLines.length; i++) {
    		networkLines[i].sortLine();
    	}
    }
    
    public int travel(String startStation, String startLine, String endStation, String endLine) {
    	
    	TrainLine curLine = null; //use this variable to store the current line.
    	TrainStation curStation= null; //use this variable to store the current station. 
    	
    	
    	int hoursCount = 0;
    	System.out.println("Departing from "+startStation);
    	
    	try {
    		this.getLineByName(endLine);
    	}
    	catch(StationNotFoundException e) {
    		hoursCount = 168;
    	}
    	
    	try {
    		this.getLineByName(startLine);
    	}
    	catch(StationNotFoundException e) {
    		hoursCount = 168;;
    	}
    	
    	
    	TrainLine finalLine = this.getLineByName(endLine);
    	TrainLine startingLine = this.getLineByName(startLine);
    	try {
    		finalLine.findStation(endStation);
    	}
    	catch(StationNotFoundException e) {
    		hoursCount = 168;;
    	}
    	
    	try {
    		startingLine.findStation(startStation);
    	}
    	catch(StationNotFoundException e) {
    		hoursCount = 168;;
    	}
    	
    	TrainStation startingStation = startingLine.findStation(startStation);
    	TrainStation preStation = null;
    	curLine = startingLine;
    	curStation = startingStation;
    	
    	
    	
    	
    	
    
    	
    	while(!(curStation.getName()==endStation)) {
    		
    		
    		if(hoursCount == 168) {
    			System.out.println("Jumped off after spending a full week on the train. Might as well walk.");
    			return hoursCount;
    		}
    		
    		//prints an update on your current location in the network.
	    	System.out.println("Traveling on line "+curLine.getName()+":"+curLine.toString());
	    	System.out.println("Hour "+hoursCount+". Current station: "+curStation.getName()+" on line "+curLine.getName());
	    	System.out.println("=============================================");
	    	
	    	TrainStation tmp = curStation;
    		
    		curStation = curLine.travelOneStation(curStation, preStation);
    		curLine = curStation.getLine();
    		preStation = tmp;
    		
    		hoursCount = hoursCount + 1;
    		
    		if(hoursCount%2 == 0 && hoursCount != 0) {
    			dance();
    		}

    		
	    	
    	}
    	
	    	
	    System.out.println("Arrived at destination after "+hoursCount+" hours!");
	    return hoursCount;
    }
    
    
    //you can extend the method header if needed to include an exception. You cannot make any other change to the header.
    public TrainLine getLineByName(String lineName) throws LineNotFoundException{
    	//YOUR CODE GOES HERE
    	int num = networkLines.length;
    	int i;
    	for(i = 0; i<num; i++) {
    		if((networkLines[i].getName().equals(lineName))) {
    			return networkLines[i];
    		}
    		else if(!(networkLines[i].getName().equals(lineName)) && i == num - 1) {
    			throw new LineNotFoundException(lineName);
    		}
    	}
    	return networkLines[i];
    }
    
  //prints a plan of the network for you.
    public void printPlan() {
    	System.out.println("CURRENT TRAIN NETWORK PLAN");
    	System.out.println("----------------------------");
    	for(int i=0;i<this.networkLines.length;i++) {
    		System.out.println(this.networkLines[i].getName()+":"+this.networkLines[i].toString());
    		}
    	System.out.println("----------------------------");
    }
}

//exception when searching a network for a LineName and not finding any matching Line object.
class LineNotFoundException extends RuntimeException {
	   String name;

	   public LineNotFoundException(String n) {
	      name = n;
	   }

	   public String toString() {
	      return "LineNotFoundException[" + name + "]";
	   }
	}