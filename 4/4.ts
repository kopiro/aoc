let count = 0;

const criteriaOne = n => {
  let p = -Infinity;
  return n.every(e => {
    const r = +e >= p;
    p = +e;
    return r;
  });
};

const criteriaTwo = n => {
  const digits = {};
  for (let i = 0; i < n.length; i++) {
    if (n[i] == n[i + 1]) {
      digits[n[i]] = digits[n[i]] || 1;
      digits[n[i]]++;
    }
  }
  // return Object.keys(digits).length > 0;
  return Object.entries(digits).some(([, value]) => value === 2);
};

for (let i = 264360; i <= 746325; i++) {
  if (
    [criteriaOne, criteriaTwo].map(c => c(String(i).split(""))).every(e => e)
  ) {
    count++;
  }
}

count;
