#!/usr/bin/node

module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let symbol = '';
        for (let j = 0; j < this.width; j++) symbol += c;
        console.log(symbol);
      }
    }
  }
};
