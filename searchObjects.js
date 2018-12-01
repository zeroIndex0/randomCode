

const objects = [
  { name: "firework", name: "code" },
  { name: "hi, i'm johnny" }
]

//searching terms in objects

const term = "john";

const result = (term) => { return objects.filter((el) => el.name.toLowerCase().indexOf(term.toLowerCase()) > -1); }

console.log(objects[1].name.toLowerCase());


console.log(result(term));