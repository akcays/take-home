var numberInEnglish = require('./numberInEnglish.js');
var should = require('should');

describe('numberInEnglish', function() {

  it('should be a function', function() {
    numberInEnglish.should.be.a.Function;
  });

  it('should write single digits', function () {
    numberInEnglish(0).should.equal('zero');
    numberInEnglish(1).should.equal('one');
    numberInEnglish(2).should.equal('two');
    numberInEnglish(-3).should.equal('negative three');
    numberInEnglish(4).should.equal('four');
    numberInEnglish(-5).should.equal('negative five');
    numberInEnglish(6).should.equal('six');
    numberInEnglish(-7).should.equal('negative seven');
    numberInEnglish(8).should.equal('eight');
    numberInEnglish(-9).should.equal('negative nine');
  });

  it('should write teens', function () {
    numberInEnglish(11).should.equal('eleven');
    numberInEnglish(-12).should.equal('negative twelve');
    numberInEnglish(13).should.equal('thirteen');
    numberInEnglish(14).should.equal('fourteen');
    numberInEnglish(-15).should.equal('negative fifteen');
    numberInEnglish(16).should.equal('sixteen');
    numberInEnglish(17).should.equal('seventeen');
    numberInEnglish(18).should.equal('eighteen');
    numberInEnglish(-19).should.equal('negative nineteen');
  });

  it('should write tens', function () {
    numberInEnglish(10).should.equal('ten');
    numberInEnglish(20).should.equal('twenty');
    numberInEnglish(-30).should.equal('negative thirty');
    numberInEnglish(40).should.equal('forty');
    numberInEnglish(50).should.equal('fifty');
    numberInEnglish(60).should.equal('sixty');
    numberInEnglish(-70).should.equal('negative seventy');
    numberInEnglish(80).should.equal('eighty');
    numberInEnglish(-90).should.equal('negative ninety');
    numberInEnglish(44).should.equal('forty four');
    numberInEnglish(-67).should.equal('negative sixty seven');
    numberInEnglish(99).should.equal('ninety nine');
  });

  it('should write hundreds', function () {
    numberInEnglish(-100).should.equal('negative one hundred');
    numberInEnglish(200).should.equal('two hundred');
    numberInEnglish(300).should.equal('three hundred');
    numberInEnglish(400).should.equal('four hundred');
    numberInEnglish(-500).should.equal('negative five hundred');
    numberInEnglish(600).should.equal('six hundred');
    numberInEnglish(700).should.equal('seven hundred');
    numberInEnglish(800).should.equal('eight hundred');
    numberInEnglish(-900).should.equal('negative nine hundred');
    numberInEnglish(125).should.equal('one hundred twenty five');
    numberInEnglish(-468).should.equal('negative four hundred sixty eight');
    numberInEnglish(910).should.equal('nine hundred ten');
  });

  it('should write thousands', function () {
    numberInEnglish(-1000).should.equal('negative one thousand');
    numberInEnglish(2000).should.equal('two thousand');
    numberInEnglish(-3000).should.equal('negative three thousand');
    numberInEnglish(4000).should.equal('four thousand');
    numberInEnglish(5000).should.equal('five thousand');
    numberInEnglish(-6000).should.equal('negative six thousand');
    numberInEnglish(7000).should.equal('seven thousand');
    numberInEnglish(-8000).should.equal('negative eight thousand');
    numberInEnglish(9000).should.equal('nine thousand');
    numberInEnglish(50000).should.equal('fifty thousand');
    numberInEnglish(-2125).should.equal('negative two thousand one hundred twenty five');
    numberInEnglish(9468).should.equal('nine thousand four hundred sixty eight');
    numberInEnglish(-76392).should.equal('negative seventy six thousand three hundred ninety two');
    numberInEnglish(505720).should.equal('five hundred five thousand seven hundred twenty');
  });

  it('should write large numbers', function () {
    numberInEnglish(1000000).should.equal('one million');
    numberInEnglish(-1986655).should.equal('negative one million nine hundred eighty six thousand six hundred fifty five');
    numberInEnglish(3560078).should.equal('three million five hundred sixty thousand seventy eight'); 
    numberInEnglish(-2385024).should.equal('negative two million three hundred eighty five thousand twenty four');
    numberInEnglish(12000043).should.equal('twelve million forty three');
    numberInEnglish(-10526633).should.equal('negative ten million five hundred twenty six thousand six hundred thirty three');
    numberInEnglish(999999999).should.equal('nine hundred ninety nine million nine hundred ninety nine thousand nine hundred ninety nine');
    numberInEnglish(-998310022).should.equal('negative nine hundred ninety eight million three hundred ten thousand twenty two');
    numberInEnglish(1000000000).should.equal('one billion');
    numberInEnglish(-1000000000).should.equal('negative one billion');
  });

});
