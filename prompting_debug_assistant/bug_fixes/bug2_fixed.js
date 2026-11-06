function calculateTotal(prices) {
    let total = 0;
    if (!Array.isArray(prices)) {
        return total;
    }
    for (let i = 0; i < prices.length; i++) {
        total += prices[i];
    }
    return total;
}

const testPrices = [10, 20, 30];
const total = calculateTotal(testPrices);
console.log("Test Output:", total);
if (total !== 60) {
    throw new Error(`Test Failed: Expected 60, got ${total}`);
}
