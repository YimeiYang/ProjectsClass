package travelAgent;

public class Room {
	//private fields
	private String roomT;
	private int price;
	private boolean roomA;
	
	//room constructor
	public Room(String Type) {
		this.roomT = Type;
		//if the room type does not fit, throw an exception, or, initialize the price.
		if((!Type.equals("double"))&&(!Type.equals("queen"))&&(!Type.equals("king"))) {
			throw new IllegalArgumentException("No room of such type can be created.");
		}
		else{
			if(Type.equals("double")) {
				this.price = 9000;
			}
			else if(Type.equals("queen")) {
				this.price = 11000;
			}
			else {
				this.price = 15000;
			}
		}
		this.roomA = true;
	}

	//the other constructor
	public Room(Room a) {
		this.roomT = a.roomT;
		this.price = a.price;
		this.roomA = a.roomA;
		
	}
	
	//method getType, returning the type of the room
	public String getType() {
		return this.roomT;
	}
	
	//method getType, returning the price of the room
	public int getPrice() {
		return this.price;
	}
	
	//method changeAvailability, changing the availability of the room.
	public void changeAvailability() {
		this.roomA = !this.roomA;
	}
	
	//find the first available room with corresponding type
	public static Room findAvailableRoom(Room[] roomList, String Type) {
		
		for(int i = 0; i<roomList.length; i++ ) {
			if((roomList[i].roomT).equals(Type) && roomList[i].roomA) {
				int newI = i;
				i = roomList.length;
				return roomList[newI];
			}
			else if(i == roomList.length-1 && ((!roomList[i].roomT.equals(Type)) || (roomList[i].roomA == false))) {
				return null;
			}
		}
		return null;
		
	}
	
	//change the availability of the first room to the corresponding type.
	public static boolean makeRoomAvailable(Room[] roomList, String Type) {
		for(int i = 0; i<roomList.length; i++) {
			if((roomList[i].roomT).equals(Type) && (roomList[i].roomA == false)) {
				roomList[i].roomA = true;
				i = roomList.length;
				return true;
			}
			else if(i == roomList.length-1 && ((!roomList[i].roomT.equals(Type)) || (roomList[i].roomA == true))) {
				return false;
			}
		}
		return false;
	}
	
	public static void main(String[] args) {
		
	}
}
