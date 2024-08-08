function pascal_triangle(n) {
    if (n <= 0) {
        return [];
    }
    function createRow(index) {
        if (index === 0) {
            return [1];
        }

        const previousLevel = createRow(index - 1);
        const currentRow = [1];

        for (let k = 1; k < previousLevel.length; k++) {
            currentRow.push(previousLevel[k - 1] + previousLevel[k]);
        }

        currentRow.push(1);
        return currentRow;
    }

    const pascalTriangle = [];
    for (let i = 0; i < n; i++) {
        pascalTriangle.push(createRow(i));
    }

    return pascalTriangle;
}
