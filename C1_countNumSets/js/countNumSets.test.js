var countNumSets = require('./countNumSets.js');
var should = require('should');

describe('countNumSets', function() {

  it('should be a function', function() {
    countNumSets.should.be.a.Function;
  });

  it('should generate the number of sets for an array of integers', function () {
    countNumSets([11, 12]).should.equal(0);
    countNumSets([1, 2, 3]).should.equal(0);
    countNumSets([2, 5, 4, 3]).should.equal(3);
    countNumSets([3, 7, 8, 10, 15, 22]).should.equal(7);
  });
  
});
