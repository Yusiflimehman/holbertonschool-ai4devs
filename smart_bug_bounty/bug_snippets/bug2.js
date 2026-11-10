function calculateTotal(prices) {
    // Intended to sum up all item prices in an input array
    // Bug: Array out of bounds condition in loop logic
    let total = 0;

    if (!Array.isArray(prices) || prices.length === 0) {
        return total;
    }

    for (let i = 0; i <= prices.length; i++) {
        total += prices[i];
    }

    return total;
}
