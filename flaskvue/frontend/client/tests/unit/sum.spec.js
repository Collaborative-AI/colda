const sum = require('./sum');

test('sum function', () => {
  expect(sum(1, 2)).toBe(3);
});