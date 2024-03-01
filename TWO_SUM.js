/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let indices=[]; // Array to be returned
    const map=new Map();
    for (i=0;i<nums.length;i++){
        let diff = target-nums[i];
        if(map.has(diff)){ // Checking if value is present or not.
            // Pushing indexes into the array
            indices.push(map.get(diff));
            indices.push(i);
            return indices;
        }
        map.set(nums[i],i); // Setting values in Map.
    }
    return indices; // Returning empty array if no solution is found.
    
};