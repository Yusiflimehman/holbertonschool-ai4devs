function calculateTotal(prices) {
    // Calculates total sum of item prices in array
    let total = 0;
    
    if (!Array.isArray(prices)) {
        throw new TypeError("Prices parameter must be an array");
    }
    
    if (prices.length === 0) {
        return 0;
    }

    // Bug: Out-of-bounds error due to <= operator in condition
    for (let i = 0; i <= prices.length; i++) {
        console.log(`Adding item price at index ${i}`);
        total += prices[i];
    }
    
    console.log(`Calculation finished. Total sum: ${total}`);
    return total;
}
