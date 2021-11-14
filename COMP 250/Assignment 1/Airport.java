package travelAgent;

public class Airport {
	//private fields
	private int xC;
	private int yC;
	private int fC;
	
	//build constructors
	public Airport(int xCor, int yCor, int feeC) {
		xC = xCor;
		yC = yCor;
		fC = feeC;
	}
	
	//getfees method, return price
	public int getFees() {
		return fC;
	}
	
	//calculate the distance between airport a and b
	public static int getDistance(Airport a, Airport b) {
		double distance = Math.sqrt(Math.pow(a.xC - b.xC, 2)+Math.pow(a.yC - b.yC, 2));
		int iDistance = (int) Math.ceil((distance));
		return iDistance;
	}
	
	public static void main(String[] args) {
		
	}
}
