const moveZeros = (nums) => {
  let numOfZeros = 0;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] == 0) numOfZeros++;
    else if (numOfZeros > 0) {
      let temp = nums[i];
      nums[i] = 0;
      nums[i - numOfZeros] = temp;
    }
  }
  console.log(nums);
};

moveZeros([0, 1, 0, 3, 12]);
