function calculateTotal(prices) {
    // Function to sum all price items in an array
    let total = 0;
    
    if (!Array.isArray(prices)) {
        return total;
    }

    // Intentional Syntax/Reference error: 'price' is undefined and loop is out-of-bounds
    for (let i = 0; i <= prices.length; i++) {
        total += price[i];
    }

    return total;
}

const itemPrices = [15.99, 23.50, 4.99, 99.00];
const grandTotal = calculateTotal(itemPrices);
console.log("Calculated Total Price:", grandTotal);
