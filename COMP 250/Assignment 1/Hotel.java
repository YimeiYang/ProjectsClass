package travelAgent;

public class Hotel {
	//private fields
	private String nameH;
	private Room[] roomList;
	
	//constructor
	public Hotel(String HotelN, Room[] roomL) {
		nameH = HotelN;
		Room[] newList = new Room[roomL.length];
		for(int i = 0; i<roomL.length; i++) {
			newList[i] = new Room(roomL[i]);
		}
		roomList = newList;
	}
	
	//find the first available room of the corresponding type. If no such room type exist, throw an exception.
	public int reserveRoom(String type) {
		Room fir = Room.findAvailableRoom(roomList, type);
		if(fir != null) {
			fir.changeAvailability();
			return fir.getPrice();
		}
		else{
			throw new IllegalArgumentException("There is no room available.");
		}
	}
	
	//method to cancel the reservation of the room(changing the availability of that room).
	public boolean cancelRoom(String Type) {
		boolean afterCancel = Room.makeRoomAvailable(roomList, Type);
		return afterCancel;
	}
	public static void main(String[] args) {
		
	}

}
