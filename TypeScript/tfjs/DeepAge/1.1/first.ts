const tf = require('@tensorflow/tfjs-node');
// const tf = require('@tensorflow/tfjs');

const a = tf.tensor1d([1, 2, 3]);
a.print();

a.mul(3).print();
a.add(2).print();

const b = tf.tensor1d([2, 2, 0]);

tf.add(a, b).print();
tf.div(a, b).print();
tf.mul(a, b).print();
tf.dot(a, b).print();

tf.range(0, 10).print();
tf.range(0, 10, 2).print();

tf.linspace(0, 10, 15).print();

const c = tf.tensor2d([[1, 2, 3], [4, 5, 6]]);
c.print();

console.log(c.shape);

const d = tf.tensor3d([
  [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
  ],
  [
    [13, 14, 15],
    [16, 17, 18],
    [19, 20, 21],
    [22, 23, 24]
  ]
]);
d.print();

console.log(d.shape);

tf.sum(c).print();
tf.sum(c, 1).print();

c.reshape([3, 2]).print();
c.reshape([6, 1]).print();

c.transpose().print();
tf.transpose(c).print();

tf.randomNormal([1]).print();
tf.rand([1], Math.random).print();

tf.randomNormal([2, 3]).print();

a.print();
a.slice([0], [1]).print();
a.slice([2], [1]).print();

const x = tf.variable(a);
x.assign(tf.tensor1d([1, 3, 3]));
x.print();

c.print();
c.slice([0, 0], [1, 1]).print();
c.slice([0, 2], [1, 1]).print();
c.slice([1, 2], [1, 1]).print();

const e = tf.tensor1d([0, 5, 2, 7, 1, 9]);
e.slice([1], [4]).print();
e.slice([1], [2]).print();

e.reverse().print();

a.print();
c.print();

tf.add(a, c).print();
tf.mul(a, c).print();

const calculateTime = () => {
  const a = tf.randomNormal([100000]);
  const b: number[] = a.arraySync();

  const startTensor = Date.now();
  for (let i = 0; i < 1000; i++) {
    const sum1 = a.sum();
  }
  console.log(`Using Tensor: ${(Date.now() - startTensor) / 1000} sec`);

  const startArray = Date.now();
  for (let i = 0; i < 1000; i++) {
    const sum2 = b.reduce((sum, element) => sum + element, 0);
  }
  console.log(`Using NumberArray: ${(Date.now() - startArray) / 1000} sec`);
}

calculateTime();
