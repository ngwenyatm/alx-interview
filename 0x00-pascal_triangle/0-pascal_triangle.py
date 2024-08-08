function pascal_triangle(n) {
    // If n < or = to 0, return an empty array
    if (n <= 0) {
        return [];
    }

    // Recursive function to generate row at given idx
    function createRow(idx) {
        // Base case: The first row is always [1]
        if (idx === 0) {
            return [1];
        }

        //  get the previous row (Recursive)
        const previousLevel = createRow(idx - 1);
        // Start current row with 1
        const currentRow = [1];

        // fill the current row with sum adjacent elements in the previous row
        for (let k = 1; k < previousLevel.length; k++) {
            currentRow.push(previousLevel[k - 1] + previousLevel[k]);
        }

        // End current row with a 1
        currentRow.push(1);
        return currentRow;
    }

    // Initialize empty array to hold the whole Triangle
    const pascalTriangle = [];

    // Generate each row  add it to the Triangle
    for (let i = 0; i < n; i++) {
        pascalTriangle.push(createRow(i));
    }

    // Return complete Triangle
    return pascalTriangle;
}
