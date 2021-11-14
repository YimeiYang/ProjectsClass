package travelAgent;

public class FlightReservation extends Reservation{
	private Airport pD;
	private Airport pA;
	
	public FlightReservation(String name, Airport d, Airport a) {
		super(name);
		if(d.equals(a)) {
			throw new IllegalArgumentException("The place of departure and the place of arrival are the same.");
		}
		else {
			this.pD = d;
			this.pA = a;
		}
	}
	public int getCost() {
		int totalDistance = Airport.getDistance(pD, pA);
		double numGallon = totalDistance/167.52;
		double fuelCost = numGallon*124;
		int airportFd = this.pD.getFees();
		int airportFa = this.pA.getFees();
		int airportCost = airportFd + airportFa;
		int tax = 5375;
		int totalFee = (int)Math.ceil(fuelCost + airportCost + tax);
		return totalFee;
	}
	
	public boolean equals(Object a) {
		
		if(a instanceof FlightReservation) {
			if(this.reservationName() == ((Reservation) a).reservationName() && (this.pD == (((FlightReservation) a).pD))){
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
