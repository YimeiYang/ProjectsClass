package trainRide;

import java.util.Arrays;
import java.util.Random;

public class TrainLine {

	private TrainStation leftTerminus;
	private TrainStation rightTerminus;
	private String lineName;
	private boolean goingRight;
	public TrainStation[] lineMap;
	public static Random rand;

	public TrainLine(TrainStation leftTerminus, TrainStation rightTerminus, String name, boolean goingRight) {
		this.leftTerminus = leftTerminus;
		this.rightTerminus = rightTerminus;
		this.leftTerminus.setLeftTerminal();
		this.rightTerminus.setRightTerminal();
		this.leftTerminus.setTrainLine(this);
		this.rightTerminus.setTrainLine(this);
		this.lineName = name;
		this.goingRight = goingRight;

		this.lineMap = this.getLineArray();
	}

	public TrainLine(TrainStation[] stationList, String name, boolean goingRight)
	/*
	 * Constructor for TrainStation input: stationList - An array of TrainStation
	 * containing the stations to be placed in the line name - Name of the line
	 * goingRight - boolean indicating the direction of travel
	 */
	{
		TrainStation leftT = stationList[0];
		TrainStation rightT = stationList[stationList.length - 1];

		stationList[0].setRight(stationList[stationList.length - 1]);
		stationList[stationList.length - 1].setLeft(stationList[0]);

		this.leftTerminus = stationList[0];
		this.rightTerminus = stationList[stationList.length - 1];
		this.leftTerminus.setLeftTerminal();
		this.rightTerminus.setRightTerminal();
		this.leftTerminus.setTrainLine(this);
		this.rightTerminus.setTrainLine(this);
		this.lineName = name;
		this.goingRight = goingRight;

		for (int i = 1; i < stationList.length - 1; i++) {
			this.addStation(stationList[i]);
		}

		this.lineMap = this.getLineArray();
	}

	public TrainLine(String[] stationNames, String name,
			boolean goingRight) {/*
									 * Constructor for TrainStation. input: stationNames - An array of String
									 * containing the name of the stations to be placed in the line name - Name of
									 * the line goingRight - boolean indicating the direction of travel
									 */
		TrainStation leftTerminus = new TrainStation(stationNames[0]);
		TrainStation rightTerminus = new TrainStation(stationNames[stationNames.length - 1]);

		leftTerminus.setRight(rightTerminus);
		rightTerminus.setLeft(leftTerminus);

		this.leftTerminus = leftTerminus;
		this.rightTerminus = rightTerminus;
		this.leftTerminus.setLeftTerminal();
		this.rightTerminus.setRightTerminal();
		this.leftTerminus.setTrainLine(this);
		this.rightTerminus.setTrainLine(this);
		this.lineName = name;
		this.goingRight = goingRight;
		for (int i = 1; i < stationNames.length - 1; i++) {
			this.addStation(new TrainStation(stationNames[i]));
		}

		this.lineMap = this.getLineArray();

	}

	// adds a station at the last position before the right terminus
	public void addStation(TrainStation stationToAdd) {
		TrainStation rTer = this.rightTerminus;
		TrainStation beforeTer = rTer.getLeft();
		rTer.setLeft(stationToAdd);
		stationToAdd.setRight(rTer);
		beforeTer.setRight(stationToAdd);
		stationToAdd.setLeft(beforeTer);

		stationToAdd.setTrainLine(this);

		this.lineMap = this.getLineArray();
	}

	public String getName() {
		return this.lineName;
	}
	
	public int getSize() {

		// YOUR CODE GOES HERE
		int count = 1;

		if(rightTerminus != null) {
			TrainStation ChangeStation = this.rightTerminus;
			while(! ChangeStation.equals(this.leftTerminus)){
				ChangeStation = ChangeStation.getLeft();
				count = count + 1;
			}
				
		}
		else {
			return 0;
		}
		return count;
		
	}

	public void reverseDirection() {
		this.goingRight = !this.goingRight;
	}

	// You can modify the header to this method to handle an exception. You cannot make any other change to the header.
	public TrainStation travelOneStation(TrainStation current, TrainStation previous) 
			throws StationNotFoundException{

		// YOUR CODE GOES HERE
		findStation(current.getName());
		TrainStation transfer;
		
	
		if(current.hasConnection && (!current.getTransferStation().equals(previous))) {
			transfer = current.getTransferStation();
		}
		else if(current.hasConnection && previous == null) {
			transfer = current.getTransferStation();
		}
		else {
			transfer = getNext(current);
		}
		return transfer; // change this!

	}


	// You can modify the header to this method to handle an exception. You cannot make any other change to the header.
	public TrainStation getNext(TrainStation station) throws StationNotFoundException{

		// YOUR CODE GOES HERE
		findStation(station.getName());
		if(station.equals(rightTerminus) && goingRight) {
			reverseDirection();
			return station.getLeft();
		}
		else if(station.equals(leftTerminus) && !(goingRight)) {
			reverseDirection();
			return station.getRight();
		}
		else if(goingRight) {
			return station.getRight();
		}
		return station.getLeft();
	}

	// You can modify the header to this method to handle an exception. You cannot make any other change to the header.
	public TrainStation findStation(String name) throws StationNotFoundException{

		// YOUR CODE GOES HERE
		TrainStation ChangeStation = this.rightTerminus;
		while(!ChangeStation.equals(this.leftTerminus)) {
			if((ChangeStation.getName()).equals(name)) {
				return ChangeStation;
			}
			ChangeStation = ChangeStation.getLeft();
			if((ChangeStation.getName()).equals(name)) {
				return ChangeStation;
			}
			else if((ChangeStation.getLeft().equals(leftTerminus))&& 
					(!((ChangeStation.getLeft()).getName()).equals(name))) {
				throw new StationNotFoundException(name.toString());
			}
		}
		return ChangeStation;
	}

	public void swap(TrainStation x, TrainStation y) {
		TrainStation tmp =x;
		y = x;
		x= tmp;
	}
	
	public void sortLine() {

		// YOUR CODE GOES HERE
		int num = getSize();
		int count = 0;
		
		boolean terminate = false;
		while(terminate != true) {
			count = count + 1;
			for(int i = 0; i<num-1; i++) {
				if((this.getLineArray()[i].getName().compareTo
						(this.getLineArray()[i+1].getName())>0)) {
					swap(this.getLineArray()[i], this.getLineArray()[i+1]);
					
					terminate = true;
				}	
			}
		}
		this.lineMap = this.getLineArray();
		lineMap[0].setLeftTerminal();
		lineMap[0].setLeft(null);
		lineMap[0].setRight(lineMap[1]);
		leftTerminus = lineMap[0];
		
		for(int i = 1; i<lineMap.length-1; i++) {
			lineMap[i].setLeft(lineMap[i-1]);
			lineMap[i].setRight(lineMap[i+1]);
			lineMap[i].setNonTerminal();
		}
		
		lineMap[lineMap.length - 1].setRightTerminal();
		lineMap[lineMap.length - 1].setLeft(lineMap[lineMap.length - 2]);
		lineMap[lineMap.length - 1].setRight(null);
		rightTerminus = lineMap[lineMap.length - 1];
		
	}


	public TrainStation[] getLineArray() {

		// YOUR CODE GOES HERE
		int num = this.getSize();
		TrainStation[] newArray= new TrainStation [num];
		TrainStation ChangeStation = leftTerminus;
		for(int i = 0; i<num; i++) {
			if(!ChangeStation.equals(rightTerminus)) {
				newArray[i] = ChangeStation;
				ChangeStation = ChangeStation.getRight();
			}
			else if(ChangeStation.equals(rightTerminus)) {
				newArray[newArray.length - 1] = ChangeStation;
				break;
			}
		}
		return newArray;	
	}

	private TrainStation[] shuffleArray(TrainStation[] array) {
		Random rand = new Random();
		rand.setSeed(11);

		for (int i = 0; i < array.length; i++) {
			int randomIndexToSwap = rand.nextInt(array.length);
			TrainStation temp = array[randomIndexToSwap];
			array[randomIndexToSwap] = array[i];
			array[i] = temp;
		}
		this.lineMap = array;
		return array;
	}

	public void shuffleLine() {

		// you are given a shuffled array of trainStations to start with
		TrainStation[] lineArray = this.getLineArray();
		TrainStation[] shuffledArray = shuffleArray(lineArray);
		// YOUR CODE GOES HER
		this.lineMap = shuffledArray;
		lineMap[0].setLeftTerminal();
		lineMap[0].setLeft(null);
		lineMap[0].setRight(lineMap[1]);
		leftTerminus = lineMap[0];
		
		for(int i = 1; i<lineMap.length-1; i++) {
			lineMap[i].setLeft(lineMap[i-1]);
			lineMap[i].setRight(lineMap[i+1]);
			lineMap[i].setNonTerminal();
		}
		
		lineMap[lineMap.length - 1].setRightTerminal();
		lineMap[lineMap.length - 1].setLeft(lineMap[lineMap.length - 2]);
		lineMap[lineMap.length - 1].setRight(null);
		rightTerminus = lineMap[lineMap.length - 1];
	}

	public String toString() {
		TrainStation[] lineArr = this.getLineArray();
		String[] nameArr = new String[lineArr.length];
		for (int i = 0; i < lineArr.length; i++) {
			nameArr[i] = lineArr[i].getName();
		}
		return Arrays.deepToString(nameArr);
	}

	public boolean equals(TrainLine line2) {

		// check for equality of each station
		TrainStation current = this.leftTerminus;
		TrainStation curr2 = line2.leftTerminus;

		try {
			while (current != null) {
				if (!current.equals(curr2))
					return false;
				else {
					current = current.getRight();
					curr2 = curr2.getRight();
				}
			}

			return true;
		} catch (Exception e) {
			return false;
		}
	}

	public TrainStation getLeftTerminus() {
		return this.leftTerminus;
	}

	public TrainStation getRightTerminus() {
		return this.rightTerminus;
	}
}

//Exception for when searching a line for a station and not finding any station of the right name.
class StationNotFoundException extends RuntimeException {
	String name;

	public StationNotFoundException(String n) {
		name = n;
	}

	public String toString() {
		return "StationNotFoundException[" + name + "]";
	}
}
