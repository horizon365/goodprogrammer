{
    let num = 10;
    num = 100;
    console.log(num);
}

for (let i=0; i<10; i++){
    console.log(i);
    console.log(i);
}

const arr = ['a', 'b'];
for (let i in arr){
    console.log(i);
}

class Person2 {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    showName(){
        return this.name
    }
}