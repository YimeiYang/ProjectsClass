package travelAgent;

public class Customer {
	private String nameC;
	private int Balance;
	private Basket reserveList;

	public Customer(String name, int firBalance){
		this.nameC = name;
		this.Balance = firBalance;
		this.reserveList = new Basket();
	}
	
	public String getName() {
		return this.nameC;
	}
	
	public int getBalance() {
		return this.Balance;
	}
	
	public Basket getBasket() {
		return this.reserveList;
	}
	
	public int addFunds(int newM) {
		if(newM<0) {
			throw new IllegalArgumentException("The fund added is negative.");
		}
		else {
			Balance = Balance + newM;
		}
		return Balance;
	}
	
	public int addToBasket(Reservation a) {
		if(a.reservationName() == this.getName()) {
			return this.reserveList.add(a);
		}
		else {
			throw new IllegalArgumentException("Names do not match.");
		}
	}
	
	public int addToBasket(Hotel a, String roomT, int NumOfNights, boolean BorN) {
		Reservation Add;
		if(BorN == true) {
			Add = new BnBReservation(this.getName(), a, roomT, NumOfNights);
		}
		else {
			Add = new HotelReservation(this.getName(), a, roomT, NumOfNights);
		}
		int newListLen = this.addToBasket(Add);
		return newListLen;
	}
	
	public int addToBasket(Airport a, Airport b) {
		Reservation Addflight = new FlightReservation(this.getName(), a, b);
		int newListNum = this.addToBasket(Addflight);
		return newListNum;
	}
	
	public boolean removeFromBasket(Reservation a) {
		boolean result = this.reserveList.remove(a);
		return result;	
	}
	
	public int checkOut() {
		int totalCost = this.reserveList.getTotalCost();
		if(this.Balance < totalCost) {
			throw new IllegalArgumentException("There is not enough money.");
		}
		else {
			Balance = Balance - totalCost;
			this.reserveList.clear();
		}
		return Balance;
	}
	public static void main(String[] args) {
		
	}
}
