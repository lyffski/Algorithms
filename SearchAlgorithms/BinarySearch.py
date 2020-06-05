# The Binary Search is quicker than the linear search
# because all the values are sorted. Because everything
# is sorted once you get to a number larger than what
# you are looking for you can stop the search. Also
# you be able to start searching from the middle 
# which speeds the search. It also works best when 
# there are no duplicates

def binarySearchForValue(value)
    
    lowIndex = 0;
    highIndex = arraySize - 1;
    
    while(lowIndex <= highIndex){
        
        middleIndex = (highIndex + lowIndex) / 2;
        
        if(theArray[middleIndex] < value) lowIndex = middleIndex + 1;
        
        else if(theArray[middleIndex] > value) highIndex = middleIndex - 1;
        
        else {
            
            print("\nFound a Match for " + value + " at Index " + middleIndex);
            
            lowIndex = highIndex + 1;
            
        }   
    }