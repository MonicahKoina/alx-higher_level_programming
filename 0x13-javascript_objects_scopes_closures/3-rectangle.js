#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }
}

<<<<<<< HEAD
module.exports = Rectangl
=======
module.exports = Rectangle;
>>>>>>> d4127cbd4176461bc3eba3910f45d0faab30a4db
