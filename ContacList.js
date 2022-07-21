
const contaclist =[
  { id: 1, name: "Daniela caicedo", number: 3184935937 },
  { id: 2, name: " luis carlos ", number: 3215824691 },
  { id: 3, name: "Daniel flores", number: 3125921353 },
  { id: 4, name: "laura lopez", number: 3185931845 },
  { id: 5, name: "javier mesa", number: 195371525 },
  { id: 6, name: "enrique perez", number: 3257547425 },
]

alert("Añadir Nuevo Contacto")
 contaclist.push({
    id: window.prompt("Ingrese la posición del contacto"),
    Nombre: window.prompt("Nombre"),
    Apellido: window.prompt("Apellido"),
    Numero: window.prompt("Numero"),
    Direción: window.prompt("Dirección"),
    Correo: window.prompt("Correo"),
});
const deletecontact = contaclist.shift();
console.log(contaclist);
const moreinformation = contaclist.push({
    id: 11,
    nombres: "Nombre",
    apellido: "Apellido",
    numero: "Numero",
    direccion: "Dirección",
    correo: "Correo",
})
console.log(contaclist[0]);