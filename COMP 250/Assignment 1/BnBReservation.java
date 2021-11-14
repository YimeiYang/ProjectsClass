package travelAgent;

public class BnBReservation extends HotelReservation{
	
	public BnBReservation(String name, Hotel a, String rType, int numN) {
		super(name, a, rType, numN);
	}
	
	public int getCost() {
		int numNights = super.getNumOfNights();
		int costNoB = super.getCost();
		int costBft = numNights*1000;
		int totalCost = costBft + costNoB;
		return totalCost;
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		}

}
