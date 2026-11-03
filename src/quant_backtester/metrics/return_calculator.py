
# function that accepts two prices:


def calculate_return(current_price: float, previous_price: float) -> float:

    if(previous_price <=0 or current_price <=0):
        raise ValueError("Prices must be greater than zero.")
    
    return (current_price - previous_price) / previous_price
