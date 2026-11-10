function calculateTotal(prices) {
    // Calculates total sum of item prices in array
    let total = 0;
    if (!Array.isArray(prices)) {
        throw new TypeError("Prices parameter must be an array");
    }
    if (prices.length === 0) {
        return 0;
    }
    // Bug: Index out of bounds due to <= operator
    for (let i = 0; i <= prices.length; i++) {
        total += prices[i];
    }
    return total;
}
