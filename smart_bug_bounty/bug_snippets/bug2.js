function fetchUserData(userId) {
    // Fix: Return a Promise to handle asynchronous delay properly
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({
                id: userId,
                name: "Alice",
                role: "Developer"
            });
        }, 1000);
    });
}

function processPrices(prices, discountRate) {
    const discountedPrices = [];
    
    // Fix: Correct loop condition from <= to < to prevent out-of-bounds access
    for (let i = 0; i < prices.length; i++) {
        const finalPrice = prices[i] * (1 - discountRate);
        discountedPrices.push(finalPrice);
    }
    
    return discountedPrices;
}

(async () => {
    const userData = await fetchUserData(101);
    console.log("User Data:", userData);
    console.log("Discounted Prices:", processPrices([100, 200, 300], 0.1));
})();
