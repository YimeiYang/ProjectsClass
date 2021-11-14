package travelAgent;

public class Basket {
	private Reservation[] reserveList;
	
	public Basket() {
		this.reserveList = new Reservation[0];
	}

	public Reservation[] getProducts() {
		Reservation[] newList = this.reserveList.clone();
		return newList;
	}
	
	public int add(Reservation a) {
		int nowList = this.reserveList.length;
		Reservation[] newList = new Reservation[nowList+1];
		for(int i = 0; i<nowList; i++) {
			newList[i] = this.reserveList[i];
		}
		newList[nowList] = a;
		int newNumList = newList.length;
		this.reserveList = newList;
		return newNumList;
	}
	
	public boolean remove(Reservation b) {
		int nowList = this.reserveList.length;
		for(int i = 0; i<nowList; i++) {
			if(this.reserveList[i].equals(b)) {
				Reservation[] newList = new Reservation[nowList-1];
				
				for(int j = 0; j<i; j++) {
					newList[j] = this.reserveList[j];
				}
				for(int j = i + 1; j<nowList; j++) {
					newList[j-1] = this.reserveList[j];
				}
				this.reserveList = newList;
				return true;
			}
	
		}
		return false;
	}
	
	public void clear() {
		Reservation[] newClear = new Reservation[0];
		this.reserveList = newClear;
	}
	
	public int getNumOfReservations() {
		int reserveL = this.reserveList.length;
		return reserveL;
	}
	
	public int getTotalCost() {
		int totalCost = 0;
		int numReserve = this.reserveList.length;
		for(int i = 0; i<numReserve; i++) {
			totalCost = totalCost + this.reserveList[i].getCost();
		}
		return totalCost;
	}
	
	public static void main(String[] args) {
		
	}

}
