let color=['pink','yellow','purple','red','blue','yellow','green'];
let a=[1,2,3,4,5];
console.log(color.length);
color.push('black');
console.log(color);
console.log(color.length);
color.splice(0,2,'lavender','brown')
console.log(color);
let c1=color.concat(a);
console.log(c1);
color.unshift(1,2);
console.log(color);
console.log(color.pop());
console.log(color.shift());
console.log(color);
delete color[2];
console.log(color);
console.log(color.toString());
console.log(color.join(':)'));
console.log(color.reverse());
console.log(color.sort());
console.log(color.slice(2,5));
console.log(color.indexOf('green'));
console.log(color.indexOf('orange'));
console.log(color.lastIndexOf('yellow'));




/*const a=[1,2,3];
console.log(color);
console.log(a);
color[0]=['red'];
console.log(color);*/