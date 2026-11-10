function calculateTotal(prices) {
    let total = 0;
    // Intended to sum up all prices in the array
    for (let i = 0; i <= prices.length; i++) {
        total += prices[i];
    }
    return total;
}
