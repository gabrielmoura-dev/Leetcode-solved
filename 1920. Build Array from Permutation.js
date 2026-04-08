var buildArray = function(nums) {
    let ans = [];
    for (let i = 0; i < nums.length;){
     ans[i] = nums[nums[i]];
     i++;
    }
 return ans;
};