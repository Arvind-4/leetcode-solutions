// https://leetcode.com/problems/sort-by

function sortBy(arr: any[], fn: Function): any[] {
    return arr.sort((a, b) => fn(a) - fn(b));
};