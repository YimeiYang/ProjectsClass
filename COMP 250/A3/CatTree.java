package catCafe;


import java.util.ArrayList;
import java.util.Iterator;
import java.util.NoSuchElementException; 


public class CatTree implements Iterable<CatInfo>{
    public CatNode root;
    
    public CatTree(CatInfo c) {
        this.root = new CatNode(c);
    }
    
    private CatTree(CatNode c) {
        this.root = c;
    }
    
    
    public void addCat(CatInfo c)
    {
        this.root = root.addCat(new CatNode(c));
    }
    
    public void removeCat(CatInfo c)
    {
        this.root = root.removeCat(c);
    }
    
    public int mostSenior()
    {
        return root.mostSenior();
    }
    
    public int fluffiest() {
        return root.fluffiest();
    }
    
    public CatInfo fluffiestFromMonth(int month) {
        return root.fluffiestFromMonth(month);
    }
    
    public int hiredFromMonths(int monthMin, int monthMax) {
        return root.hiredFromMonths(monthMin, monthMax);
    }
    
    public int[] costPlanning(int nbMonths) {
        return root.costPlanning(nbMonths);
    }
    
    
    
    public Iterator<CatInfo> iterator()
    {
        return new CatTreeIterator();
    }
    
    
    class CatNode {
        
        CatInfo data;
        CatNode senior;
        CatNode same;
        CatNode junior;
        
        public CatNode(CatInfo data) {
            this.data = data;
            this.senior = null;
            this.same = null;
            this.junior = null;
        }
        
        public String toString() {
            String result = this.data.toString() + "\n";
            if (this.senior != null) {
                result += "more senior " + this.data.toString() + " :\n";
                result += this.senior.toString();
            }
            if (this.same != null) {
                result += "same seniority " + this.data.toString() + " :\n";
                result += this.same.toString();
            }
            if (this.junior != null) {
                result += "more junior " + this.data.toString() + " :\n";
                result += this.junior.toString();
            }
            return result;
        }
        
        
        public CatNode addCat(CatNode c) {
        	CatNode changeNode = root;
        	//let c becomes the root if the root does not exist
        	if(root == null) {
        		root = c;
        	}
        	//else, compare the seniority of c with that of the root 
        	//if the cat to add is senior to c and c.senior != null
        	else if(c.data.monthHired < changeNode.data.monthHired) {
        		//add the cat 
        		while(changeNode.senior != null && c.data.monthHired < changeNode.data.monthHired) {
        			changeNode = changeNode.senior;
        		}
        		if(c.data.monthHired < changeNode.data.monthHired) {
        			changeNode.senior = c;
        		}
        		else if(c.data.monthHired > changeNode.data.monthHired) {
        			changeNode.junior= c;
        		}
        		//if the cat to add has the same seniority as the one in the subtree and is fluffier, swap
        		else if(c.data.monthHired == changeNode.data.monthHired) {
        			//if the one in the subtree has no same
        			if(changeNode.same == null) {
        				changeNode.same = c;
        			}
        			//if yes, swap
        			else {
        				while(changeNode.same != null && c.data.furThickness < changeNode.data.furThickness) {
    	        			changeNode = changeNode.same;
    	        		}
    	        		//and is fluffier, swap
    	        		if(c.data.furThickness > changeNode.data.furThickness) {
    	        			CatNode tmp = new CatNode(root.data);
    	        			changeNode.data = c.data;
    	        			c.data = tmp.data;
    	        			changeNode.same = c;
    	        		}
    	        		else {
    	        			changeNode.same = c;
    	        		}
        			}
        		}
        	}
        	//if the cat to add is junior to c and c.junior != null
        	else if(c.data.monthHired > root.data.monthHired) {
        		//add the cat
        		while(changeNode.junior != null && c.data.monthHired > changeNode.data.monthHired) {
        			changeNode = changeNode.junior;
        		}
        		if(c.data.monthHired < changeNode.data.monthHired) {
        			changeNode.senior = c;
        		}
        		else if(c.data.monthHired > changeNode.data.monthHired) {
        			changeNode.junior= c;
        		}
        		//if the cat to add has the same seniority as the one in the subtree and is fluffier, swap
        		else if(c.data.monthHired == changeNode.data.monthHired) {
        			if(c.data.furThickness > changeNode.data.furThickness) {
            			CatNode tmp = new CatNode(changeNode.data);
        				changeNode = c;
        				c = tmp;
        				changeNode.same = c;

        			}
        			else {
        				changeNode.same = c;
        			}
        		}
        	}
        	//if the cat to add has the same seniority as c
        	else if(changeNode != null && c.data.monthHired == changeNode.data.monthHired) {
        		while(changeNode.same != null && c.data.furThickness < changeNode.data.furThickness) {
        			changeNode = changeNode.same;
        		}
        		//and is fluffier, swap
        		if(c.data.furThickness > changeNode.data.furThickness && root.data.equals(changeNode.data)) {
        			
        			CatNode tmp = new CatNode(changeNode.data);
        			changeNode.data = c.data;
        			c.data = tmp.data;
        			//if(changeNode.same.same != null) {
        				//CatNode temp = changeNode.same.same;
        				//c.same = temp;
        			//}
        			c.same = changeNode.same;
        			changeNode.same = c;
        			
        			return changeNode;
        		}
        		else if(c.data.furThickness > changeNode.data.furThickness 
        				&& ! root.data.equals(changeNode.data)) {
        			CatNode tmp = new CatNode(changeNode.data);
        			changeNode.data = c.data;
        			c.data = tmp.data;
        			
        			c.same = changeNode.same;
        			changeNode.same = c;
        		}
        		//and is not fluffier, simply add
        		else {
        			c.same = changeNode.same;
        			changeNode.same = c;
        		}
        	} 	
            return root; 
        }
        
        //helper function to find the CatNode with CatInfo
        private CatNode findCat(CatNode r, CatInfo c) {
        	CatNode result = null;
        	if(r != null) {
        		if(r.data.equals(c)) {
        			return r;
        		}
        		else {
        			result = findCat(r.senior, c);
        			result = findCat(r.same, c);
        			result = findCat(r.junior, c);
        		}
        	}
        	return result;
        }
        
        public CatNode removeCat(CatInfo c) {
        	CatNode rootO = new CatNode(root.data);
        	//find the CatNode need to be removed
            CatNode catFind = findCat(root, c);
            //if cat to remove can not be found, do nothing.
            if(catFind == null) {
            	return root;
            }
            //if c.same == null && c.senior == null 
            
            else if(catFind != null && catFind.same == null && catFind.senior == null && catFind.junior != null) {
            	root = catFind.junior;
            }
            //if c.same == null && c.senior != null
            else if(catFind != null && catFind.same == null && catFind.senior != null) {
            	root = catFind.senior;
            	if(catFind.junior != null) {
            		catFind.senior.addCat(catFind.junior);
            	}
            	return root;
            }
            //if c.same != null
            else if(catFind != null && catFind.same != null) {
            	if(catFind != root) {
            		if(catFind.senior != null) {
            			catFind.same.addCat(catFind.senior);
            		}
            		if(catFind.junior != null) {
            			catFind.same.addCat(catFind.junior);
            		}
            		catFind.data = catFind.same.data;
            		catFind.same = catFind.same.same;
            		return root;
            	}
            	else if(catFind == root) {
            		root = catFind.same;
            		if(catFind.senior != null) {
            			catFind.same.addCat(catFind.senior);
            		}
            		if(catFind.junior != null) {
            			catFind.same.addCat(catFind.junior);
            		}
            		return root;
            	}
            }
            return rootO;
        }
        
        
        public int mostSenior() {
            // ADD YOUR CODE HERE
        	//if c.senior exists, continues to look down through the tree.
        	if (this.senior != null) {
        		while(this.senior != null) {
        			this.senior = this.senior.senior;
        		}
        		return this.senior.data.monthHired;
        	}
        	//if c.senior does not exist, return c's monthHired.
        	else if(this.senior == null) {
        		return this.data.monthHired;
        	}
        	return -1;
        }
        
        
        //helper function to find the biggest value in the tree
        private int findFluf(CatNode r) {
        	if(r == null) {
        		return 0;
        	}
        	int rD = r.data.furThickness;
        	int sD = findFluf(r.senior);
        	int jD = findFluf(r.junior);
        	if(sD > rD) {
        		rD = sD;
        	}
        	if(jD > rD) {
        		rD = jD;
        	}
        	return rD;
        }

        
        public int fluffiest() {
        	//find the fluffiest
            int result = findFluf(this); 
            return result;
        }
        
        
        public int hiredFromMonths(int monthMin, int monthMax) {
        	
            //if min>max
        	if( this == null || monthMin > monthMax) {
        		return 0;
        	}
        	//if min<max
        	else {
        		int add = 0;
        		int numJunior = 0;
        		int numSenior = 0;
        		int numSame = 0;
        		if(this.data.monthHired >= monthMin && this.data.monthHired <= monthMax) {
        			add = 1;
        		}
        		if(this.junior != null) {
        			numJunior = this.junior.hiredFromMonths(monthMin, monthMax);
        		}
        		if(this.same != null) {
        			numSame = this.same.hiredFromMonths(monthMin, monthMax);
        		}
        		if(this.senior != null) {
        			numSenior = this.senior.hiredFromMonths(monthMin, monthMax);
        		}
        		int result =  add + numJunior + numSenior + numSame;
        		return result;
        	}
            
        }
        
        public CatInfo fluffiestFromMonth(int month) {
            // ADD YOUR CODE HERE
        	//find if there is any cat hired in specific month
        	int num = hiredFromMonths(month, month);
        	//if no, return null
        	if(num == 0) {
        		return null;
        	}
        	
        	CatInfo rT = null;
        	CatInfo jT = null;
        	CatInfo saT = null;
        	CatInfo seT = null;
        	if(this.data.monthHired == month) {
        		rT = this.data;
        	}
        	if(this.junior != null) {
    			jT = this.junior.fluffiestFromMonth(month);
    		}
    		if(this.same != null) {
    			saT = this.junior.fluffiestFromMonth(month);
    		}
    		if(this.senior != null) {
    			seT = this.junior.fluffiestFromMonth(month);
    		}
    		
    		if(rT != null && jT != null && jT.furThickness > rT.furThickness) {
    			rT = jT;
    		}
    		if(rT != null && saT != null && saT.furThickness > rT.furThickness) {
    			rT = saT;
    		}
    		if(rT != null && seT != null && seT.furThickness > rT.furThickness) {
    			rT = seT;
    		}
            return rT;
        }
        
        public int[] costPlanning(int nbMonths) {
            // ADD YOUR CODE HERE
        	CatTreeIterator iter = new CatTreeIterator();
        	int[] cost = new int[nbMonths];
        	for(int i = 0; i<nbMonths; i++) {
        		int sum = 0;
        		while(iter.hasNext()) {
        			if(iter.next().nextGroomingAppointment == (243 + i)) {
        				sum = sum + iter.next().expectedGroomingCost;
        			}
        		}
        		cost[i] = sum;
        	}
            return cost; 
        }
        
    }
    
    private class CatTreeIterator implements Iterator<CatInfo> {
        // HERE YOU CAN ADD THE FIELDS YOU NEED
    	ArrayList<CatNode> listA = new ArrayList<CatNode> ();
    	
    	public void makeList(CatNode r) {
    		if(r != null) {
    			makeList(r.senior);
    			makeList(r.same);
    			listA.add(r);
    			makeList(r.junior);
    		}
    	}
        CatNode cur;
        public CatTreeIterator() {
        	makeList(root);
        	cur = listA.get(0);
        }
        
        public CatInfo next(){
            CatNode tmp = cur;
            int index = listA.indexOf(cur);
            if(index != listA.size() -1) {
            	cur = listA.get(index+1);
            }
            else {
            	cur = null;
            }
            return tmp.data;
        }
        
        public boolean hasNext() {
            return (cur!= null); 
        }
    }
    
}

