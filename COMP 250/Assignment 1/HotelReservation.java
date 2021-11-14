package travelAgent;

public class HotelReservation extends Reservation{
	private Hotel wR;
	private String rT;
	private int numOfNight;
	private int pricePerNight;
	
	public HotelReservation(String name, Hotel a, String rTn, int numNight) {
		super(name);
		this.wR = a;
		this.rT = rTn;
		this.pricePerNight = a.reserveRoom(rTn);
		this.numOfNight = numNight;
	}
	
	public int getNumOfNights() {
		return this.numOfNight;
	}
	
	public int getCost() {
		return this.pricePerNight * this.numOfNight;
	}
	
	public boolean equals(Object a) {
		if(a instanceof HotelReservation) {
			if(this.reservationName() == ((Reservation) a).reservationName() 
					&& (this.wR == ((HotelReservation) a).wR) 
					&& (this.rT == ((HotelReservation) a).rT)
					&& (this.numOfNight == ((HotelReservation) a).numOfNight)
					&& (this.getCost() == ((HotelReservation) a).getCost())){
				return true;
			}
			else {
				return false;
			}
		}
		else {
			return false;
		}
	}
	public static void main(String[] args) {
		
	}

}
